/**
 * Intel Console — Main controller
 *
 * Boot sequence:
 *   1. Show loading screen
 *   2. Load full graph data + branch assignments
 *   3. Preload entity photos
 *   4. Build Cytoscape radial map — 11 branches, no center entity
 *   5. Dismiss loading screen
 *   6. Click any node → show dossier; click again → ego mode
 *   7. Breadcrumb navigation for ego mode traversal
 */

(async function () {
    // ---- Loading screen helpers ----
    const loadingScreen = document.getElementById('loading-screen');
    const loadingStatus = document.getElementById('loading-status');
    const loadingBarFill = document.getElementById('loading-bar-fill');

    function setProgress(msg, pct) {
        if (loadingStatus) loadingStatus.textContent = msg;
        if (loadingBarFill) loadingBarFill.style.width = pct + '%';
    }

    function dismissLoading() {
        if (!loadingScreen) return;
        setProgress('SYSTEMS ONLINE', 100);
        setTimeout(() => {
            loadingScreen.classList.add('done');
            setTimeout(() => { loadingScreen.style.display = 'none'; }, 500);
        }, 600);
    }

    function showLoadingError(msg) {
        if (loadingStatus) {
            loadingStatus.textContent = msg;
            loadingStatus.style.color = '#f87171';
        }
    }

    // ---- Preload images ----
    function preloadImages(urls, onProgress) {
        let loaded = 0;
        const total = urls.length;
        if (total === 0) return Promise.resolve();

        return new Promise((resolve) => {
            urls.forEach(url => {
                const img = new Image();
                img.onload = img.onerror = () => {
                    loaded++;
                    if (onProgress) onProgress(loaded, total);
                    if (loaded >= total) resolve();
                };
                img.src = url;
            });
            // Safety timeout — don't block forever on slow images
            setTimeout(resolve, 8000);
        });
    }

    // ---- Boot ----
    setProgress('INITIALIZING...', 5);

    // Ensure Cytoscape map is initialized before anything else
    initMap();
    Dossier.init();
    Search.init();
    Navigator.init();

    // ---- Toolbar button refs (must be before updateBreadcrumb) ----
    const btnReset = document.getElementById('btn-reset');
    const btnZoomIn = document.getElementById('btn-zoom-in');
    const btnZoomOut = document.getElementById('btn-zoom-out');
    const btnConnections = document.getElementById('btn-connections');
    const btnBackToMap = document.getElementById('btn-back-to-map');
    const btnViewToggle = document.getElementById('btn-view-toggle');

    // ---- Node click handler (registered on cytomap.js) ----
    window._onMapNodeClick = async (nodeId) => {
        if (hubMode) {
            // First click on radial map: show dossier + enter ego mode
            navStack = [nodeId];
            await recenterOn(nodeId);
            updateBreadcrumb();
            Dossier.show(nodeId);
        } else if (egoMode && nodeId !== currentCenterId) {
            // Ego mode: click another node → recenter on it
            navStack.push(nodeId);
            await recenterOn(nodeId);
            updateBreadcrumb();
            Dossier.show(nodeId);
        } else {
            // Already centered on this node — just show dossier
            Dossier.show(nodeId);
        }
    };

    // ---- Background click ----
    window._onMapBgClick = () => {
        Dossier.close();
    };

    // ---- Load data and boot ----
    let graphLoaded = false;
    try {
        setProgress('LOADING DATA...', 15);

        // Load graph data and branch assignments in parallel
        const [data, assignments] = await Promise.all([
            API.getGraphFull('speculative'),
            API.getBranchAssignments(),
        ]);

        storeGraphData(data);
        setBranchAssignments(assignments);
        Navigator.build(data.nodes, assignments);
        graphLoaded = true;

        setProgress('BUILDING MAP...', 40);

        // Init type filters from data — all types visible by default
        const types = [...new Set(data.nodes.map(n => n.entity_type))].sort();
        Filters.init(types);

        // Load stats
        try {
            const stats = await API.getStats();
            let statsHtml = `
                <span class="stat-item"><span class="stat-value">${stats.entities}</span> entities</span>
                <span class="stat-item"><span class="stat-value">${stats.relationships}</span> relationships</span>
                <span class="stat-item"><span class="stat-value">${stats.sources}</span> sources</span>`;
            if (stats.signals) {
                statsHtml += `
                <span class="stat-item"><span class="stat-value">${stats.signals}</span> signals</span>`;
            }
            document.getElementById('stats-bar').innerHTML = statsHtml;
        } catch (e) { console.warn('Stats load failed:', e); }

        // Init timeline slider
        Timeline.init();

        // Boot into radial map
        buildRadialMap();
        updateBreadcrumb();

        setProgress('LOADING IMAGES...', 55);

        // Preload entity photos (real photos only, skip SVG icons)
        const photoUrls = data.nodes
            .filter(n => n.photo_url && !n.photo_url.startsWith('data:'))
            .map(n => n.photo_url);

        await preloadImages(photoUrls, (loaded, total) => {
            const imgPct = 55 + Math.round((loaded / total) * 40);
            setProgress(`LOADING IMAGES... ${loaded}/${total}`, imgPct);
        });

        // ---- Hash routing: #entity/ID deep links ----
        try {
            await handleEntityHash();
        } catch (e) {
            console.error('Hash routing failed:', e);
        }
        window.addEventListener('hashchange', handleEntityHash);

        // Dismiss loading screen
        dismissLoading();

        // Show branch directory unless deep-linked to an entity
        if (!window.location.hash) {
            Navigator.open();
        }

    } catch (err) {
        console.error('Boot error:', err);
        if (!graphLoaded) {
            showLoadingError('FAILED TO LOAD DATA');
        }
    }

    // ---- Keyboard shortcuts ----
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            if (Navigator.isOpen) { Navigator.close(); return; }
            Dossier.close();
        }
        if (e.key === '/' && document.activeElement !== Search.input) {
            e.preventDefault();
            Search.input.focus();
        }
        if (e.key === 'Backspace' && document.activeElement !== Search.input) {
            e.preventDefault();
            navigateBack();
        }
        if (e.key === 'i' && document.activeElement !== Search.input) {
            Navigator.toggle();
        }
    });

    // ---- Toolbar button listeners ----
    if (btnReset) btnReset.addEventListener('click', resetView);
    if (btnZoomIn) btnZoomIn.addEventListener('click', zoomIn);
    if (btnZoomOut) btnZoomOut.addEventListener('click', zoomOut);

    if (btnConnections) {
        btnConnections.addEventListener('click', () => {
            const on = toggleConnections();
            btnConnections.classList.toggle('active', on);
        });
    }

    if (btnBackToMap) {
        btnBackToMap.addEventListener('click', () => {
            navStack = [];
            Dossier.close();
            buildRadialMap();
            updateBreadcrumb();
        });
    }

    if (btnViewToggle) {
        btnViewToggle.addEventListener('click', () => {
            toggleView();
        });
    }

    const btnIndex = document.getElementById('btn-index');
    if (btnIndex) {
        btnIndex.addEventListener('click', () => Navigator.toggle());
    }



    /* ---- Breadcrumb management ---- */

    function updateBreadcrumb() {
        const bar = document.getElementById('breadcrumb-bar');

        // Show/hide back-to-map button
        if (btnBackToMap) {
            btnBackToMap.style.display = egoMode ? '' : 'none';
        }

        if (hubMode) {
            bar.innerHTML = `<span class="breadcrumb-current">Network Overview</span>`;
            return;
        }

        if (navStack.length === 0) {
            bar.innerHTML = '';
            return;
        }

        let html = '';
        html += `<span class="breadcrumb-item" data-hub="true">Hub</span>`;
        html += `<span class="breadcrumb-sep">&rsaquo;</span>`;

        navStack.forEach((id, i) => {
            const name = getEntityName(id);
            if (i < navStack.length - 1) {
                html += `<span class="breadcrumb-item" data-id="${id}">${esc(name)}</span>`;
                html += `<span class="breadcrumb-sep">&rsaquo;</span>`;
            } else {
                html += `<span class="breadcrumb-current">${esc(name)}</span>`;
            }
        });
        bar.innerHTML = html;

        // Click handlers on breadcrumb items
        bar.querySelectorAll('.breadcrumb-item[data-id]').forEach(el => {
            el.addEventListener('click', async () => {
                const id = parseInt(el.getAttribute('data-id'));
                const idx = navStack.indexOf(id);
                if (idx >= 0) {
                    navStack = navStack.slice(0, idx + 1);
                }
                await recenterOn(id);
                updateBreadcrumb();
                Dossier.show(id);
            });
        });

        // Hub link handler
        const hubLink = bar.querySelector('[data-hub]');
        if (hubLink) {
            hubLink.addEventListener('click', () => {
                navStack = [];
                Dossier.close();
                buildRadialMap();
                updateBreadcrumb();
            });
        }
    }

    async function navigateBack() {
        if (hubMode) return;

        if (navStack.length <= 1) {
            navStack = [];
            Dossier.close();
            buildRadialMap();
            updateBreadcrumb();
            return;
        }

        navStack.pop();
        const prevId = navStack[navStack.length - 1];
        await recenterOn(prevId);
        updateBreadcrumb();
    }

    function getEntityName(id) {
        if (!graphData) return `#${id}`;
        const node = graphData.nodes.find(n => n.id === id);
        return node ? node.name : `#${id}`;
    }

    // ---- Hash routing ----
    async function handleEntityHash() {
        var hash = window.location.hash.slice(1);
        if (!hash) return;
        // Support #entity/ID format
        var match = hash.match(/^entity\/(\d+)$/);
        if (!match) return;
        var entityId = parseInt(match[1]);
        if (!graphData) { console.warn('[hash] no graphData'); return; }
        var node = graphData.nodes.find(n => n.id === entityId);
        if (!node) { console.warn('[hash] entity not found:', entityId); return; }
        // Navigate to entity
        console.log('[hash] navigating to entity', entityId, node.name);
        navStack = [entityId];
        await recenterOn(entityId);
        updateBreadcrumb();
        Dossier.show(entityId);
    }

    // Expose for other modules
    window.navigateBack = navigateBack;
    window.updateBreadcrumb = updateBreadcrumb;
})();
