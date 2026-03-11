/**
 * Intel Console — Cytoscape.js Transformation Map Engine
 *
 * Three view modes:
 *   1. Radial (default): Pre-computed positions, 11 branches, 3 rings
 *   2. Force: fcose layout for exploring cross-branch connections
 *   3. Ego: BFS depth-2 neighborhood in concentric layout
 *
 * Exports the same global API surface as the old map.js so that
 * app.js, dossier.js, search.js, and timeline.js work unchanged.
 */

// ---- Constants ----
const TYPE_COLORS = {
    person:       '#4a9eff',
    organization: '#a78bfa',
    agency:       '#f87171',
    program:      '#fb923c',
    contract:     '#34d399',
    shell_company:'#f472b6',
    foundation:   '#fbbf24',
    event:        '#94a3b8',
    legislation:  '#6ee7b7',
    facility:     '#c084fc',
    publication:  '#38bdf8',
};

const TIER_COLORS = {
    documented:  '#34d399',
    credible:    '#fbbf24',
    inference:   '#fb923c',
    speculative: '#f87171',
};

// Radial layout distances (scaled for Cytoscape coordinate space)
const RING_DISTANCES = [0, 300, 520, 740, 960];
const NODE_SIZES = { 1: 44, 2: 28, 3: 20 };
const EGO_RING_DISTANCES = [0, 240, 440];
const EGO_NODE_SIZES = [50, 28, 18];

// Opacity
const DIM_OPACITY = 0.08;
const LINE_DEFAULT_OPACITY = 0.12;
const LINE_HIGHLIGHT_OPACITY = 0.65;

// ---- State ----
let graphData = null;
let currentCenterId = null;
let navStack = [];
let egoMode = false;
let hubMode = true;
let isRecentering = false;

let cy = null;
let currentView = 'radial'; // 'radial' | 'force' | 'ego'
let branchAssignments = null;

const filterState = {
    activeTiers: new Set(['documented', 'credible', 'inference', 'speculative']),
    activeTypes: null,
    yearMin: null,
    yearMax: null,
    showUndated: true,
    showConnections: true,
};


// ---- Initialize ----

function initMap() {
    const container = document.getElementById('cy-container');
    if (!container) return;

    cy = cytoscape({
        container: container,
        style: getCytoscapeStyle(),
        elements: [],
        layout: { name: 'preset' },
        minZoom: 0.08,
        maxZoom: 6,
        wheelSensitivity: 0.3,
        boxSelectionEnabled: false,
        selectionType: 'single',
        pixelRatio: 'auto',
    });

    // Node click
    cy.on('tap', 'node', (evt) => {
        const node = evt.target;
        if (node.hasClass('title-badge')) return;

        const nodeId = parseInt(node.id());
        if (window._onMapNodeClick) {
            window._onMapNodeClick(nodeId);
        }
    });

    // Background click
    cy.on('tap', (evt) => {
        if (evt.target === cy) {
            if (window._onMapBgClick) {
                window._onMapBgClick();
            }
        }
    });

    // Hover highlights
    cy.on('mouseover', 'node', (evt) => {
        const node = evt.target;
        if (node.hasClass('title-badge')) return;
        hoverHighlight(node);
    });

    cy.on('mouseout', 'node', (evt) => {
        hoverClear();
    });
}


function storeGraphData(data) {
    graphData = data;
}


// ---- Cytoscape Stylesheet ----

function getCytoscapeStyle() {
    return [
        // Node base
        {
            selector: 'node',
            style: {
                'label': 'data(label)',
                'font-family': "'SF Mono', 'Monaco', 'Cascadia Code', 'Fira Code', monospace",
                'font-size': 8,
                'color': 'rgba(255,255,255,0.7)',
                'text-valign': 'bottom',
                'text-halign': 'center',
                'text-margin-y': 6,
                'text-max-width': '80px',
                'text-wrap': 'ellipsis',
                'text-outline-width': 2,
                'text-outline-color': '#0a0a0f',
                'text-outline-opacity': 0.8,
                'width': 'data(size)',
                'height': 'data(size)',
                'background-color': 'data(color)',
                'border-width': 1.5,
                'border-color': 'data(borderColor)',
                'border-opacity': 0.6,
                'transition-property': 'opacity, width, height',
                'transition-duration': '0.2s',
                'min-zoomed-font-size': 6,
            }
        },
        // Photo nodes
        {
            selector: 'node[photo_url]',
            style: {
                'background-image': 'data(photo_url)',
                'background-fit': 'cover',
                'background-clip': 'node',
            }
        },
        // Title badge (center)
        {
            selector: 'node.title-badge',
            style: {
                'label': 'INTEL\nCONSOLE',
                'font-size': 10,
                'font-weight': 'bold',
                'color': 'rgba(255,255,255,0.35)',
                'text-valign': 'center',
                'text-halign': 'center',
                'text-wrap': 'wrap',
                'width': 80,
                'height': 80,
                'background-color': '#0a0a0f',
                'border-width': 1,
                'border-color': 'rgba(255,255,255,0.12)',
                'border-style': 'dashed',
                'shape': 'ellipse',
                'text-margin-y': 0,
                'events': 'no',
                'z-index': 0,
            }
        },
        // Branch anchor nodes
        {
            selector: 'node.branch-anchor',
            style: {
                'label': 'data(branchLabel)',
                'font-size': 7,
                'font-weight': 'bold',
                'color': 'data(color)',
                'text-valign': 'center',
                'text-halign': 'center',
                'text-wrap': 'wrap',
                'text-max-width': '90px',
                'width': 50,
                'height': 50,
                'background-color': '#0a0a0f',
                'border-width': 2,
                'border-color': 'data(color)',
                'shape': 'ellipse',
                'text-margin-y': 0,
                'z-index': 5,
            }
        },
        // Edge base
        {
            selector: 'edge',
            style: {
                'curve-style': 'bezier',
                'width': 0.8,
                'line-color': 'data(tierColor)',
                'line-opacity': LINE_DEFAULT_OPACITY,
                'target-arrow-shape': 'none',
                'overlay-opacity': 0,
                'transition-property': 'line-opacity, opacity',
                'transition-duration': '0.2s',
            }
        },
        // Dimmed
        {
            selector: '.dimmed',
            style: {
                'opacity': DIM_OPACITY,
            }
        },
        // Highlighted node
        {
            selector: '.highlighted',
            style: {
                'border-width': 3,
                'border-color': '#4a9eff',
                'z-index': 999,
            }
        },
        // Highlighted edge
        {
            selector: 'edge.highlighted',
            style: {
                'line-opacity': LINE_HIGHLIGHT_OPACITY,
                'width': 1.5,
                'z-index': 998,
            }
        },
        // Hidden
        {
            selector: '.hidden',
            style: {
                'display': 'none',
            }
        },
        // Edge hidden (separate from node hidden for filter logic)
        {
            selector: '.edge-hidden',
            style: {
                'display': 'none',
            }
        },
    ];
}


// ---- Radial Layout ----

function computeRadialPositions() {
    if (!graphData || !branchAssignments) return {};

    const branchKeys = Object.keys(BRANCHES);

    // Equal angles: each branch gets 360/N degrees
    const sliceWidth = 360 / branchKeys.length;
    const branchAngles = {};
    branchKeys.forEach((k, i) => {
        const start = -90 + i * sliceWidth;
        branchAngles[k] = {
            start: start,
            width: sliceWidth,
            center: start + sliceWidth / 2,
        };
    });

    // Group entities by branch and ring
    const branchRings = {};
    branchKeys.forEach(k => {
        branchRings[k] = { 1: [], 2: [], 3: [] };
    });
    for (const [id, info] of Object.entries(branchAssignments)) {
        const node = graphData.nodes.find(n => n.id === parseInt(id));
        if (!node) continue;
        if (branchRings[info.branch]) {
            branchRings[info.branch][info.ring].push(parseInt(id));
        }
    }

    const positions = {};

    // Title badge at center
    positions['title'] = { x: 0, y: 0 };

    // Branch anchors
    branchKeys.forEach(k => {
        const angle = branchAngles[k].center;
        const rad = angle * Math.PI / 180;
        positions['anchor_' + k] = {
            x: Math.cos(rad) * RING_DISTANCES[1] * 0.52,
            y: Math.sin(rad) * RING_DISTANCES[1] * 0.52,
        };
    });

    // Entity positions
    branchKeys.forEach(k => {
        const ba = branchAngles[k];
        const sectorRad = ba.width * Math.PI / 180;

        [1, 2, 3].forEach(ring => {
            const entities = branchRings[k][ring];
            if (entities.length === 0) return;

            const dist = RING_DISTANCES[ring];
            const centerRad = ba.center * Math.PI / 180;
            const count = entities.length;

            // Fan spread: distribute within sector
            const maxSpread = sectorRad * 0.85;
            const spacing = count > 1 ? Math.min(0.18, maxSpread / (count - 1)) : 0;
            const totalSpread = spacing * (count - 1);
            const startAngle = centerRad - totalSpread / 2;

            entities.forEach((eid, i) => {
                const angle = count > 1 ? startAngle + i * spacing : centerRad;
                positions[String(eid)] = {
                    x: Math.cos(angle) * dist,
                    y: Math.sin(angle) * dist,
                };
            });
        });
    });

    return positions;
}


function buildRadialMap() {
    if (!cy || !graphData || !branchAssignments) return;

    egoMode = false;
    hubMode = true;
    currentCenterId = null;
    currentView = 'radial';

    const positions = computeRadialPositions();
    const elements = buildElements(positions);

    cy.batch(() => {
        cy.elements().remove();
        cy.add(elements);
    });

    cy.layout({
        name: 'preset',
        positions: (node) => {
            return positions[node.id()] || { x: 0, y: 0 };
        },
        fit: true,
        padding: 60,
    }).run();

    applyAllFilters();

    // Update view toggle button
    updateViewToggle();
}


function buildElements(positions) {
    const elements = [];
    const nodeIds = new Set();

    // Title badge
    elements.push({
        group: 'nodes',
        data: { id: 'title', label: '', size: 80, color: '#0a0a0f', borderColor: 'rgba(255,255,255,0.12)' },
        classes: 'title-badge',
        position: positions['title'] || { x: 0, y: 0 },
    });

    // Branch anchors
    Object.keys(BRANCHES).forEach(k => {
        const b = BRANCHES[k];
        elements.push({
            group: 'nodes',
            data: {
                id: 'anchor_' + k,
                label: '',
                branchLabel: b.label,
                size: 50,
                color: b.color,
                borderColor: b.color,
            },
            classes: 'branch-anchor',
            position: positions['anchor_' + k] || { x: 0, y: 0 },
        });
    });

    // Entity nodes
    graphData.nodes.forEach(n => {
        const info = branchAssignments[String(n.id)];
        if (!info) return;

        const branch = BRANCHES[info.branch];
        if (!branch) return;

        const size = NODE_SIZES[info.ring] || 20;
        const typeColor = TYPE_COLORS[n.entity_type] || '#888';
        const branchColor = branch.color;

        const nodeData = {
            id: String(n.id),
            label: n.name,
            entityId: n.id,
            entityType: n.entity_type,
            branchKey: info.branch,
            ring: info.ring,
            size: size,
            color: branchColor,
            borderColor: typeColor,
            connectionCount: n.connection_count || 0,
        };

        if (n.photo_url) {
            nodeData.photo_url = n.photo_url;
        }

        elements.push({
            group: 'nodes',
            data: nodeData,
            position: positions[String(n.id)] || { x: 0, y: 0 },
        });
        nodeIds.add(String(n.id));
    });

    // Edges
    graphData.edges.forEach(e => {
        const srcId = String(e.source);
        const tgtId = String(e.target);
        if (!nodeIds.has(srcId) || !nodeIds.has(tgtId)) return;

        elements.push({
            group: 'edges',
            data: {
                id: 'e' + e.id,
                source: srcId,
                target: tgtId,
                edgeId: e.id,
                relationshipType: e.relationship_type,
                evidenceTier: e.evidence_tier,
                tierColor: TIER_COLORS[e.evidence_tier] || '#888',
                yearStart: e.year_start,
                yearEnd: e.year_end,
                description: e.description || '',
            },
        });
    });

    return elements;
}


// ---- Force Layout ----

function switchToForce() {
    if (!cy || currentView === 'force') return;
    currentView = 'force';

    // Use fcose if available, fall back to built-in cose
    const hasFcose = typeof cytoscapeFcose !== 'undefined' || cy.layout({ name: 'fcose', stop: () => {} }).options;
    let layoutOpts;

    try {
        layoutOpts = {
            name: 'fcose',
            animate: true,
            animationDuration: 800,
            animationEasing: 'ease-out',
            quality: 'default',
            randomize: false,
            nodeDimensionsIncludeLabels: false,
            uniformNodeDimensions: false,
            packComponents: true,
            nodeRepulsion: () => 6000,
            idealEdgeLength: () => 120,
            edgeElasticity: () => 0.2,
            nestingFactor: 0.1,
            gravity: 0.3,
            gravityRange: 1.5,
            gravityCompound: 1.0,
            numIter: 2500,
            initialEnergyOnIncremental: 0.3,
            fit: true,
            padding: 40,
        };
        cy.layout(layoutOpts).run();
    } catch (e) {
        // Fallback to built-in cose
        console.warn('fcose unavailable, using cose:', e.message);
        layoutOpts = {
            name: 'cose',
            animate: true,
            animationDuration: 800,
            nodeRepulsion: () => 6000,
            idealEdgeLength: () => 120,
            edgeElasticity: () => 0.2,
            gravity: 0.3,
            numIter: 1000,
            fit: true,
            padding: 40,
        };
        cy.layout(layoutOpts).run();
    }

    updateViewToggle();
}


function switchToRadial() {
    if (!cy || currentView === 'radial') return;

    if (egoMode) {
        // Can't switch to radial from ego — go back to hub first
        navStack = [];
        Dossier.close();
        buildRadialMap();
        updateBreadcrumb();
        return;
    }

    currentView = 'radial';
    const positions = computeRadialPositions();

    cy.layout({
        name: 'preset',
        positions: (node) => {
            return positions[node.id()] || { x: 0, y: 0 };
        },
        animate: true,
        animationDuration: 600,
        animationEasing: 'ease-in-out',
        fit: true,
        padding: 60,
    }).run();

    updateViewToggle();
}


function toggleView() {
    if (egoMode) return; // No toggling in ego mode
    if (currentView === 'radial') {
        switchToForce();
    } else {
        switchToRadial();
    }
}


function updateViewToggle() {
    const btn = document.getElementById('btn-view-toggle');
    if (!btn) return;
    if (egoMode) {
        btn.querySelector('.btn-label').textContent = 'Ego';
        btn.classList.remove('active');
    } else if (currentView === 'force') {
        btn.querySelector('.btn-label').textContent = 'Force';
        btn.classList.add('active');
    } else {
        btn.querySelector('.btn-label').textContent = 'Radial';
        btn.classList.remove('active');
    }
}


// ---- Ego Mode ----

async function recenterOn(nodeId) {
    if (!cy || !graphData || isRecentering) return;
    isRecentering = true;

    try {
        const neighborhood = await API.getNeighborhood(nodeId, 2);
        if (!neighborhood || !neighborhood.nodes.length) {
            isRecentering = false;
            return;
        }

        egoMode = true;
        hubMode = false;
        currentCenterId = nodeId;
        currentView = 'ego';

        // Build ego elements
        const egoNodeIds = new Set(neighborhood.nodes.map(n => n.id));
        const egoPositions = computeEgoPositions(nodeId, neighborhood);
        const elements = buildEgoElements(nodeId, neighborhood, egoPositions);

        cy.batch(() => {
            cy.elements().remove();
            cy.add(elements);
        });

        cy.layout({
            name: 'preset',
            positions: (node) => {
                return egoPositions[node.id()] || { x: 0, y: 0 };
            },
            fit: true,
            padding: 80,
        }).run();

        applyAllFilters();
        updateViewToggle();
    } finally {
        isRecentering = false;
    }
}


function computeEgoPositions(centerId, neighborhood) {
    const positions = {};
    positions[String(centerId)] = { x: 0, y: 0 };

    // BFS to find ring assignment
    const edgeList = neighborhood.edges;
    const adj = {};
    edgeList.forEach(e => {
        if (!adj[e.source]) adj[e.source] = [];
        if (!adj[e.target]) adj[e.target] = [];
        adj[e.source].push(e.target);
        adj[e.target].push(e.source);
    });

    const ringMap = { [centerId]: 0 };
    let frontier = [centerId];
    for (let depth = 1; depth <= 2; depth++) {
        const next = [];
        for (const nid of frontier) {
            for (const neighbor of (adj[nid] || [])) {
                if (ringMap[neighbor] === undefined) {
                    ringMap[neighbor] = depth;
                    next.push(neighbor);
                }
            }
        }
        frontier = next;
    }

    // Position ring 1 and ring 2 nodes
    [1, 2].forEach(ring => {
        const nodesInRing = neighborhood.nodes.filter(n =>
            ringMap[n.id] === ring
        );
        const count = nodesInRing.length;
        if (count === 0) return;

        const dist = EGO_RING_DISTANCES[ring];
        const angleStep = (2 * Math.PI) / count;

        nodesInRing.forEach((n, i) => {
            const angle = -Math.PI / 2 + i * angleStep;
            positions[String(n.id)] = {
                x: Math.cos(angle) * dist,
                y: Math.sin(angle) * dist,
            };
        });
    });

    return positions;
}


function buildEgoElements(centerId, neighborhood, positions) {
    const elements = [];
    const nodeIds = new Set();
    const centerIdStr = String(centerId);

    // BFS ring map
    const adj = {};
    neighborhood.edges.forEach(e => {
        if (!adj[e.source]) adj[e.source] = [];
        if (!adj[e.target]) adj[e.target] = [];
        adj[e.source].push(e.target);
        adj[e.target].push(e.source);
    });

    const ringMap = { [centerId]: 0 };
    let frontier = [centerId];
    for (let depth = 1; depth <= 2; depth++) {
        const next = [];
        for (const nid of frontier) {
            for (const neighbor of (adj[nid] || [])) {
                if (ringMap[neighbor] === undefined) {
                    ringMap[neighbor] = depth;
                    next.push(neighbor);
                }
            }
        }
        frontier = next;
    }

    neighborhood.nodes.forEach(n => {
        const info = branchAssignments[String(n.id)];
        const branch = info ? BRANCHES[info.branch] : null;
        const ring = ringMap[n.id] !== undefined ? ringMap[n.id] : 2;
        const size = EGO_NODE_SIZES[ring] || 18;
        const typeColor = TYPE_COLORS[n.entity_type] || '#888';
        const branchColor = branch ? branch.color : '#888';

        const nodeData = {
            id: String(n.id),
            label: n.name,
            entityId: n.id,
            entityType: n.entity_type,
            branchKey: info ? info.branch : 'unknown',
            ring: ring,
            size: size,
            color: n.id === centerId ? '#4a9eff' : branchColor,
            borderColor: typeColor,
            connectionCount: n.connection_count || 0,
        };

        if (n.photo_url) {
            nodeData.photo_url = n.photo_url;
        }

        elements.push({
            group: 'nodes',
            data: nodeData,
            position: positions[String(n.id)] || { x: 0, y: 0 },
        });
        nodeIds.add(String(n.id));
    });

    neighborhood.edges.forEach(e => {
        const srcId = String(e.source);
        const tgtId = String(e.target);
        if (!nodeIds.has(srcId) || !nodeIds.has(tgtId)) return;

        elements.push({
            group: 'edges',
            data: {
                id: 'e' + e.id,
                source: srcId,
                target: tgtId,
                edgeId: e.id,
                relationshipType: e.relationship_type,
                evidenceTier: e.evidence_tier,
                tierColor: TIER_COLORS[e.evidence_tier] || '#888',
                yearStart: e.year_start,
                yearEnd: e.year_end,
                description: e.description || '',
            },
        });
    });

    return elements;
}


// ---- Filtering ----

function filterByTier(activeTiers) {
    if (!cy) return;
    filterState.activeTiers = activeTiers instanceof Set ? activeTiers : new Set(activeTiers);
    applyEdgeFilters();
}

function filterByType(activeTypes) {
    if (!cy) return;
    filterState.activeTypes = activeTypes instanceof Set ? activeTypes : new Set(activeTypes);
    cy.batch(() => {
        cy.nodes().forEach(node => {
            if (node.hasClass('title-badge') || node.hasClass('branch-anchor')) return;
            const type = node.data('entityType');
            if (type && !filterState.activeTypes.has(type)) {
                node.addClass('hidden');
            } else {
                node.removeClass('hidden');
            }
        });
    });
}

function filterByYear(yearMin, yearMax, showUndated) {
    if (!cy) return;
    filterState.yearMin = yearMin;
    filterState.yearMax = yearMax;
    filterState.showUndated = showUndated;
    applyEdgeFilters();
}

function applyEdgeFilters() {
    if (!cy) return;

    cy.batch(() => {
        cy.edges().forEach(edge => {
            let visible = true;

            // Tier filter
            const tier = edge.data('evidenceTier');
            if (tier && !filterState.activeTiers.has(tier)) {
                visible = false;
            }

            // Year filter
            if (visible && filterState.yearMin !== null) {
                const ys = edge.data('yearStart');
                const ye = edge.data('yearEnd');
                if (ys == null && ye == null) {
                    if (!filterState.showUndated) visible = false;
                } else {
                    const start = ys || ye;
                    const end = ye || ys;
                    if (end < filterState.yearMin || start > filterState.yearMax) {
                        visible = false;
                    }
                }
            }

            // Connection visibility
            if (!filterState.showConnections) {
                visible = false;
            }

            if (visible) {
                edge.removeClass('edge-hidden');
            } else {
                edge.addClass('edge-hidden');
            }
        });
    });
}

function applyAllFilters() {
    if (filterState.activeTypes) {
        filterByType(filterState.activeTypes);
    }
    applyEdgeFilters();
}


// ---- Highlight / Focus ----

function highlightNode(nodeId) {
    if (!cy) return;
    clearHighlight();

    const node = cy.getElementById(String(nodeId));
    if (!node || node.empty()) return;

    const connectedEdges = node.connectedEdges();
    const connectedNodes = connectedEdges.connectedNodes();

    cy.batch(() => {
        // Dim everything
        cy.elements().addClass('dimmed');

        // Undim connected
        node.removeClass('dimmed').addClass('highlighted');
        connectedEdges.removeClass('dimmed').addClass('highlighted');
        connectedNodes.removeClass('dimmed');

        // Keep branch anchors and title visible
        cy.nodes('.title-badge, .branch-anchor').removeClass('dimmed');
    });
}

function clearHighlight() {
    if (!cy) return;
    cy.batch(() => {
        cy.elements().removeClass('dimmed highlighted');
    });
}

function focusNode(nodeId) {
    if (!cy) return;
    const node = cy.getElementById(String(nodeId));
    if (!node || node.empty()) return;

    cy.animate({
        center: { eles: node },
        zoom: 2.5,
        duration: 400,
        easing: 'ease-in-out',
    });

    highlightNode(nodeId);
}


// ---- Hover (lightweight) ----

function hoverHighlight(node) {
    if (!cy) return;
    if (cy.elements('.highlighted').length > 0) return; // Active highlight takes precedence

    const connectedEdges = node.connectedEdges();
    connectedEdges.forEach(e => {
        e.style('line-opacity', LINE_HIGHLIGHT_OPACITY);
        e.style('width', 1.2);
    });
}

function hoverClear() {
    if (!cy) return;
    if (cy.elements('.highlighted').length > 0) return;

    cy.edges().removeStyle('line-opacity width');
}


// ---- Zoom / Pan controls ----

function zoomIn() {
    if (!cy) return;
    const w = cy.width(), h = cy.height();
    cy.animate({
        zoom: { level: cy.zoom() * 1.4, renderedPosition: { x: w / 2, y: h / 2 } },
        duration: 200,
    });
}

function zoomOut() {
    if (!cy) return;
    const w = cy.width(), h = cy.height();
    cy.animate({
        zoom: { level: cy.zoom() / 1.4, renderedPosition: { x: w / 2, y: h / 2 } },
        duration: 200,
    });
}

function resetView() {
    if (!cy) return;
    cy.animate({ fit: { eles: cy.elements(), padding: 60 }, duration: 300 });
}

function toggleConnections() {
    filterState.showConnections = !filterState.showConnections;
    applyEdgeFilters();
    return filterState.showConnections;
}


// ---- Branch assignment loader ----

function setBranchAssignments(assignments) {
    branchAssignments = assignments;
    // Also set global for backwards compat
    ENTITY_BRANCH_MAP = {};
    for (const [id, info] of Object.entries(assignments)) {
        ENTITY_BRANCH_MAP[id] = { branch: info.branch, ring: info.ring };
    }
}
