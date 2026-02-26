/**
 * Intel Console — Main controller
 *
 * Boot sequence:
 *   1. Load full graph data (for reference)
 *   2. Build radial SVG map — Epstein at center, 7 branches
 *   3. Click any node → show dossier; click again or double-click → ego mode
 *   4. Breadcrumb navigation for ego mode traversal
 */

(async function () {
    // Ensure SVG map is initialized before anything else
    initMap();
    Dossier.init();
    Search.init();

    // ---- Node click handler (registered on map.js) ----
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
        const data = await API.getGraphFull('speculative');
        storeGraphData(data);
        graphLoaded = true;

        // Init type filters from data
        const types = [...new Set(data.nodes.map(n => n.entity_type))].sort();
        Filters.init(types);

        // Load stats
        try {
            const stats = await API.getStats();
            document.getElementById('stats-bar').innerHTML = `
                <span class="stat-item"><span class="stat-value">${stats.entities}</span> entities</span>
                <span class="stat-item"><span class="stat-value">${stats.relationships}</span> relationships</span>
                <span class="stat-item"><span class="stat-value">${stats.sources}</span> sources</span>
            `;
        } catch (e) { console.warn('Stats load failed:', e); }

        // Init timeline slider
        Timeline.init();

        // Boot into radial map
        buildRadialMap();
        updateBreadcrumb();

    } catch (err) {
        console.error('Boot error:', err);
        if (!graphLoaded) {
            const errDiv = document.createElement('div');
            errDiv.id = 'load-error';
            errDiv.style.cssText = 'color:#f87171;padding:40px;text-align:center;font-family:monospace;position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);z-index:500;pointer-events:none';
            errDiv.textContent = 'Failed to load graph data. Is the server running?';
            document.body.appendChild(errDiv);
        }
    }

    // ---- Keyboard shortcuts ----
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
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
    });

    // ---- Toolbar buttons ----
    const btnReset = document.getElementById('btn-reset');
    const btnZoomIn = document.getElementById('btn-zoom-in');
    const btnZoomOut = document.getElementById('btn-zoom-out');
    const btnConnections = document.getElementById('btn-connections');
    const btnBackToMap = document.getElementById('btn-back-to-map');

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

    // Expose for other modules
    window.navigateBack = navigateBack;
    window.updateBreadcrumb = updateBreadcrumb;
})();
