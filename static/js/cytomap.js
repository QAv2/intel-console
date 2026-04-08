/**
 * Intel Console — Cytoscape.js Transformation Map Engine
 *
 * View modes:
 *   1. Hub: 11 branch anchors as entry points
 *   2. Focused: Active branch expanded at center, 10 others in depth-scaled peripheral ring
 *   3. Force: fcose layout for exploring connections
 *   4. Ego: BFS depth-2 neighborhood in concentric layout
 *
 * Exports the same global API surface so that
 * app.js, dossier.js, search.js work unchanged.
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

// SVG fallback icons for entities without photos (white icon on transparent bg)
function _mkIcon(path, vb = '0 0 24 24') {
    return 'data:image/svg+xml,' + encodeURIComponent(
        `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${vb}" fill="none" stroke="rgba(255,255,255,0.55)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">${path}</svg>`
    );
}
const TYPE_ICONS = {
    person:       _mkIcon('<circle cx="12" cy="8" r="4"/><path d="M4 21v-1a6 6 0 0 1 12 0v1"/>', '0 0 20 24'),
    organization: _mkIcon('<rect x="3" y="7" width="18" height="14" rx="1"/><path d="M3 11h18M9 7V3h6v4M9 15h.01M15 15h.01"/>'),
    agency:       _mkIcon('<path d="M12 3L2 9h20L12 3zM4 9v9h16V9"/><path d="M9 18v-5h6v5M4 18h16"/>'),
    program:      _mkIcon('<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M8 10l3 3-3 3M13 16h3"/>'),
    event:        _mkIcon('<path d="M13 2L3 14h9l-1 8 10-12h-9l1-8"/>'),
    legislation:  _mkIcon('<path d="M12 2v4M4 8h16M7 12l5 8 5-8"/><circle cx="12" cy="6" r="1.5" fill="rgba(255,255,255,0.55)" stroke="none"/>'),
    facility:     _mkIcon('<path d="M3 21h18M5 21V7l7-4 7 4v14"/><path d="M9 21v-4h6v4M9 9h.01M15 9h.01M9 13h.01M15 13h.01"/>'),
    foundation:   _mkIcon('<path d="M12 8a4 4 0 0 0-4 4v1h8v-1a4 4 0 0 0-4-4zM6 17h12M8 21h8M4 13h2M18 13h2"/><circle cx="12" cy="4" r="1.5" fill="rgba(255,255,255,0.55)" stroke="none"/>'),
    publication:  _mkIcon('<path d="M4 4h16v16H4z"/><path d="M8 8h8M8 12h5"/>'),
    contract:     _mkIcon('<path d="M14 2H6v20h12V6z"/><path d="M14 2v4h4M9 13h6M9 17h4"/>'),
    shell_company:_mkIcon('<path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2z"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/>'),
};

const TIER_COLORS = {
    documented:  '#34d399',
    credible:    '#fbbf24',
    inference:   '#fb923c',
    speculative: '#f87171',
};

// Radial layout — adaptive: radius scales with entity count for tight packing
// minDist is the ring radius when only 1 entity; nodeSpacing is the target arc gap between nodes
const RING_CONFIG = {
    1: { minDist: 80,  nodeSpacing: 55 },   // Ring 1: key players, biggest nodes
    2: { minDist: 130, nodeSpacing: 38 },    // Ring 2: mid-tier
    3: { minDist: 180, nodeSpacing: 28 },    // Ring 3: outermost, smallest
};
const NODE_SIZES = { 1: 44, 2: 28, 3: 20 };
const BRANCH_NODE_SIZES = { 1: 44, 2: 32, 3: 24 };
const EGO_RING_DISTANCES = [0, 160, 300];
const EGO_NODE_SIZES = [44, 24, 16];

// Focused branch view — peripheral ring geometry
const RING_LAYOUT = {
    peripheralRadius: 700,    // distance from center to peripheral branch anchors
    tilt: 0.45,               // ellipse aspect ratio (simulates viewing angle)
    minScale: 0.3,            // node scale at "back" of ring (theta=PI)
    maxScale: 0.7,            // node scale at "front" of ring (theta=0)
    clusterRadius: 55,        // base radius of peripheral mini-cluster
};

/** Compute adaptive ring distance: tight when sparse, expands with count */
function adaptiveRingDist(ring, count) {
    const cfg = RING_CONFIG[ring];
    if (!cfg || count <= 1) return cfg ? cfg.minDist : 100;
    // circumference needed = count * nodeSpacing; radius = circumference / (2*PI)
    const needed = (count * cfg.nodeSpacing) / (2 * Math.PI);
    return Math.max(cfg.minDist, needed);
}

// Opacity
const DIM_OPACITY = 0.08;
const LINE_DEFAULT_OPACITY = 0.35;
const LINE_HIGHLIGHT_OPACITY = 0.8;

// ---- State ----
let graphData = null;
let currentCenterId = null;
let navStack = [];
let egoMode = false;
let hubMode = true;
let isRecentering = false;
let activeBranchFilter = null; // currently focused branch key, or null
let activeBranchView = null;   // current branch-level view key, or null for hub overview

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

// Ring rotation state (for drag-to-rotate interaction)
const ringState = {
    rotation: 0,            // current rotation offset in radians
    dragStartRotation: 0,   // rotation when drag began
    activeBranch: null,     // current active branch key
    otherBranches: [],      // ordered peripheral branch keys
    branchRing1: {},        // { branchKey: [entityId, ...] } for each peripheral branch
    entityNames: {},        // { entityId: name } for label toggling during rotation
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
        wheelSensitivity: 0.8,
        boxSelectionEnabled: false,
        selectionType: 'single',
        pixelRatio: 'auto',
    });

    // Node click
    cy.on('tap', 'node', (evt) => {
        const node = evt.target;
        if (node.hasClass('title-badge') || node.hasClass('branch-center')) return;

        // Branch anchor click — switch to that branch
        if (node.hasClass('branch-anchor')) {
            const branchKey = node.id().replace('anchor_', '');
            toggleBranchFocus(branchKey);
            return;
        }

        // Peripheral entity click — switch to that branch
        if (node.data('isPeripheral') === 1) {
            const branchKey = node.data('branchKey');
            if (branchKey) {
                toggleBranchFocus(branchKey);
            }
            return;
        }

        const nodeId = parseInt(node.id());
        if (window._onMapNodeClick) {
            window._onMapNodeClick(nodeId);
        }
    });

    // Background click
    cy.on('tap', (evt) => {
        if (evt.target === cy) {
            if (activeBranchFilter) {
                clearBranchFocus();
            }
            if (window._onMapBgClick) {
                window._onMapBgClick();
            }
        }
    });

    // Hover highlights
    cy.on('mouseover', 'node', (evt) => {
        const node = evt.target;
        if (node.hasClass('title-badge') || node.hasClass('branch-center')) return;
        hoverHighlight(node);
    });

    cy.on('mouseout', 'node', (evt) => {
        hoverClear();
    });

    // ---- Ring rotation drag (on branch-center node) ----
    let ringDragging = false;
    let ringDragStartX = 0;

    cy.on('tapstart', 'node.branch-center', (evt) => {
        if (!activeBranchView) return;
        ringDragging = true;
        ringDragStartX = evt.renderedPosition.x;
        ringState.dragStartRotation = ringState.rotation;
        cy.panningEnabled(false);
        cy.container().style.cursor = 'grabbing';
    });

    cy.on('vmousemove', (evt) => {
        if (!ringDragging) return;
        const dx = evt.renderedPosition.x - ringDragStartX;
        ringState.rotation = ringState.dragStartRotation + dx * 0.004;
        updatePeripheralPositions();
    });

    cy.on('vmouseup', () => {
        if (!ringDragging) return;
        ringDragging = false;
        cy.panningEnabled(true);
        cy.container().style.cursor = '';
        snapToNearestBranch();
    });

    // Safety: release if mouse leaves window
    document.addEventListener('mouseup', () => {
        if (ringDragging) {
            ringDragging = false;
            cy.panningEnabled(true);
            cy.container().style.cursor = '';
            snapToNearestBranch();
        }
    });

    // Cursor hint on branch-center hover
    cy.on('mouseover', 'node.branch-center', () => {
        if (activeBranchView && !ringDragging) {
            cy.container().style.cursor = 'grab';
        }
    });
    cy.on('mouseout', 'node.branch-center', () => {
        if (!ringDragging) {
            cy.container().style.cursor = '';
        }
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
                'min-zoomed-font-size': 0,
            }
        },
        // Photo nodes (real photos)
        {
            selector: 'node[photo_url][!isIcon]',
            style: {
                'background-image': 'data(photo_url)',
                'background-fit': 'cover',
                'background-clip': 'node',
            }
        },
        // Fallback type icons
        {
            selector: 'node[isIcon]',
            style: {
                'background-image': 'data(photo_url)',
                'background-fit': 'contain',
                'background-clip': 'none',
                'background-width': '55%',
                'background-height': '55%',
                'background-opacity': 0.7,
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
                'width': 'data(size)',
                'height': 'data(size)',
                'background-color': '#0a0a0f',
                'border-width': 2,
                'border-color': 'data(color)',
                'shape': 'ellipse',
                'text-margin-y': 0,
                'z-index': 5,
            }
        },
        // Branch center node (focused view title — drag to rotate ring)
        {
            selector: 'node.branch-center',
            style: {
                'label': 'data(branchLabel)',
                'font-size': 7,
                'font-weight': 'bold',
                'color': 'data(color)',
                'text-valign': 'center',
                'text-halign': 'center',
                'text-wrap': 'wrap',
                'text-max-width': '100px',
                'width': 60,
                'height': 60,
                'background-color': '#0a0a0f',
                'border-width': 1.5,
                'border-color': 'data(color)',
                'border-style': 'dashed',
                'shape': 'ellipse',
                'text-margin-y': 0,
                'z-index': 5,
                'min-zoomed-font-size': 0,
            }
        },
        // Peripheral nodes (depth-scaled opacity)
        {
            selector: 'node[isPeripheral = 1]',
            style: {
                'opacity': 'mapData(depth, 0, 1, 0.2, 0.75)',
            }
        },
        // Edge base — unbundled bezier with center-pull (spiderweb aesthetic)
        {
            selector: 'edge',
            style: {
                'curve-style': 'unbundled-bezier',
                'control-point-distances': 'data(cpDist)',
                'control-point-weights': 0.5,
                'width': 0.8,
                'line-color': 'data(tierColor)',
                'line-opacity': LINE_DEFAULT_OPACITY,
                'target-arrow-shape': 'none',
                'overlay-opacity': 0,
                'transition-property': 'line-opacity, opacity',
                'transition-duration': '0.2s',
            }
        },
        // Cross-branch edges (dashed, subtle)
        {
            selector: 'edge[isCrossBranch = 1]',
            style: {
                'curve-style': 'straight',
                'line-opacity': 0.18,
                'line-style': 'dashed',
                'line-dash-pattern': [6, 3],
                'width': 0.5,
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


// ---- Hub View (11 branch anchors) ----

function buildRadialMap() {
    if (!cy || !graphData || !branchAssignments) return;

    egoMode = false;
    hubMode = true;
    activeBranchView = null;
    currentCenterId = null;
    currentView = 'radial';
    activeBranchFilter = null;

    const branchKeys = Object.keys(BRANCHES);
    const N = branchKeys.length;
    const elements = [];
    const positions = {};

    // Title badge at center
    positions['title'] = { x: 0, y: 0 };
    elements.push({
        group: 'nodes',
        data: { id: 'title', label: '', size: 80, color: '#0a0a0f', borderColor: 'rgba(255,255,255,0.12)' },
        classes: 'title-badge',
        position: { x: 0, y: 0 },
    });

    // Branch anchors in a circle — sized by entity count
    const branchStats = {};
    branchKeys.forEach(k => { branchStats[k] = 0; });
    for (const info of Object.values(branchAssignments)) {
        if (branchStats[info.branch] !== undefined) branchStats[info.branch]++;
    }
    const maxCount = Math.max(...Object.values(branchStats));

    branchKeys.forEach((k, i) => {
        const angle = -Math.PI / 2 + (2 * Math.PI * i / N);
        const dist = 200;
        const pos = {
            x: Math.cos(angle) * dist,
            y: Math.sin(angle) * dist,
        };
        positions['anchor_' + k] = pos;

        const sizeFactor = 0.6 + 0.4 * (branchStats[k] / maxCount);
        const size = Math.round(70 * sizeFactor);

        elements.push({
            group: 'nodes',
            data: {
                id: 'anchor_' + k,
                label: '',
                branchLabel: `${BRANCHES[k].label}\n${branchStats[k]}`,
                size: size,
                color: BRANCHES[k].color,
                borderColor: BRANCHES[k].color,
            },
            classes: 'branch-anchor',
            position: pos,
        });
    });

    cy.batch(() => {
        cy.elements().remove();
        cy.add(elements);
    });

    cy.layout({
        name: 'preset',
        positions: (node) => positions[node.id()] || { x: 0, y: 0 },
        fit: true,
        padding: 60,
    }).run();

    // Reset ring state for hub
    ringState.rotation = 0;
    ringState.activeBranch = null;
    ringState.otherBranches = [];
    ringState.branchRing1 = {};
    ringState.entityNames = {};

    applyAllFilters();
    updateViewToggle();
}


// ---- Center-Pull Bezier ----

/**
 * Compute signed perpendicular distance to pull an edge's bezier
 * control point toward center (0,0) — spiderweb aesthetic.
 */
const CENTER_PULL_FACTOR = 0.45;

function computeCenterPull(positions, srcId, tgtId) {
    const p1 = positions[srcId];
    const p2 = positions[tgtId];
    if (!p1 || !p2) return 0;

    const mx = (p1.x + p2.x) / 2;
    const my = (p1.y + p2.y) / 2;

    const toCenterX = -mx;
    const toCenterY = -my;

    const dx = p2.x - p1.x;
    const dy = p2.y - p1.y;
    const edgeLen = Math.sqrt(dx * dx + dy * dy);
    if (edgeLen < 1) return 0;

    const perpX = -dy / edgeLen;
    const perpY = dx / edgeLen;

    const projection = (toCenterX * perpX + toCenterY * perpY) * CENTER_PULL_FACTOR;

    const maxPull = edgeLen * 0.6;
    return Math.max(-maxPull, Math.min(maxPull, projection));
}


// ---- Focused Branch View (with peripheral ring) ----

function computeFocusedLayout(branchKey) {
    if (!graphData || !branchAssignments) return { positions: {}, scales: {}, depths: {} };

    const positions = {};
    const scales = {};
    const depths = {};

    // ---- Active branch at center ----
    positions['branch_center'] = { x: 0, y: 0 };
    scales['branch_center'] = 1.0;
    depths['branch_center'] = 1.0;

    // Gather active branch entities by ring
    const activeRings = { 1: [], 2: [], 3: [] };
    for (const [id, info] of Object.entries(branchAssignments)) {
        if (info.branch !== branchKey) continue;
        activeRings[info.ring].push(parseInt(id));
    }

    [1, 2, 3].forEach(ring => {
        const entities = activeRings[ring];
        if (entities.length === 0) return;
        const dist = adaptiveRingDist(ring, entities.length);
        const angleStep = (2 * Math.PI) / entities.length;

        entities.forEach((eid, i) => {
            const angle = -Math.PI / 2 + i * angleStep;
            const key = String(eid);
            positions[key] = {
                x: Math.cos(angle) * dist,
                y: Math.sin(angle) * dist,
            };
            scales[key] = 1.0;
            depths[key] = 1.0;
        });
    });

    // ---- Peripheral branches in elliptical ring ----
    const otherBranches = Object.keys(BRANCHES).filter(k => k !== branchKey);
    const N = otherBranches.length;

    otherBranches.forEach((key, i) => {
        const theta = 2 * Math.PI * i / N;
        const R = RING_LAYOUT.peripheralRadius;

        // Ellipse: x varies with sin, y with cos*tilt
        // theta=0 → bottom (front/close), theta=PI → top (back/far)
        const cx = R * Math.sin(theta);
        const cy_pos = R * Math.cos(theta) * RING_LAYOUT.tilt;

        // Depth: 1 at front (theta=0), 0 at back (theta=PI)
        const depth = (1 + Math.cos(theta)) / 2;
        const scale = RING_LAYOUT.minScale + (RING_LAYOUT.maxScale - RING_LAYOUT.minScale) * depth;

        // Branch anchor
        const anchorId = 'anchor_' + key;
        positions[anchorId] = { x: cx, y: cy_pos };
        scales[anchorId] = scale;
        depths[anchorId] = depth;

        // Ring 1 entities in mini-cluster around anchor
        const ring1 = [];
        for (const [id, info] of Object.entries(branchAssignments)) {
            if (info.branch !== key || info.ring !== 1) continue;
            ring1.push(parseInt(id));
        }

        const miniR = RING_LAYOUT.clusterRadius * scale;
        ring1.forEach((eid, j) => {
            const miniAngle = -Math.PI / 2 + (2 * Math.PI * j / ring1.length);
            const eidKey = String(eid);
            positions[eidKey] = {
                x: cx + Math.cos(miniAngle) * miniR,
                y: cy_pos + Math.sin(miniAngle) * miniR,
            };
            scales[eidKey] = scale;
            depths[eidKey] = depth;
        });
    });

    return { positions, scales, depths };
}


function buildBranchMap(branchKey) {
    if (!cy || !graphData || !branchAssignments) return;

    egoMode = false;
    hubMode = true;
    activeBranchView = branchKey;
    currentCenterId = null;
    currentView = 'radial';
    activeBranchFilter = null;

    // Populate ring state for rotation
    ringState.rotation = 0;
    ringState.activeBranch = branchKey;
    ringState.otherBranches = Object.keys(BRANCHES).filter(k => k !== branchKey);
    ringState.branchRing1 = {};
    ringState.entityNames = {};
    ringState.otherBranches.forEach(key => {
        ringState.branchRing1[key] = [];
        for (const [id, info] of Object.entries(branchAssignments)) {
            if (info.branch !== key || info.ring !== 1) continue;
            const eid = parseInt(id);
            ringState.branchRing1[key].push(eid);
            const node = graphData.nodes.find(n => n.id === eid);
            if (node) ringState.entityNames[eid] = node.name;
        }
    });

    const layout = computeFocusedLayout(branchKey);
    const elements = buildFocusedElements(branchKey, layout);

    cy.batch(() => {
        cy.elements().remove();
        cy.add(elements);
    });

    cy.layout({
        name: 'preset',
        positions: (node) => layout.positions[node.id()] || { x: 0, y: 0 },
        fit: true,
        padding: 40,
    }).run();

    applyAllFilters();
    updateViewToggle();
}


function buildFocusedElements(branchKey, layout) {
    const elements = [];
    const nodeIds = new Set();
    const activeBranch = BRANCHES[branchKey];
    const { positions, scales, depths } = layout;

    // Branch center title node (grabbable: false so drag is handled by ring rotation)
    elements.push({
        group: 'nodes',
        data: {
            id: 'branch_center',
            label: '',
            branchLabel: activeBranch.label + '\n\u25C0 drag to cycle \u25B6',
            size: 60,
            color: activeBranch.color,
            borderColor: activeBranch.color,
            depth: 1.0,
        },
        grabbable: false,
        classes: 'branch-center',
        position: positions['branch_center'],
    });

    // ---- Active branch entities (all rings) ----
    graphData.nodes.forEach(n => {
        const info = branchAssignments[String(n.id)];
        if (!info || info.branch !== branchKey) return;

        const size = BRANCH_NODE_SIZES[info.ring] || 26;
        const typeColor = TYPE_COLORS[n.entity_type] || '#888';

        const nodeData = {
            id: String(n.id),
            label: n.name,
            entityId: n.id,
            entityType: n.entity_type,
            branchKey: info.branch,
            ring: info.ring,
            size: size,
            color: activeBranch.color,
            borderColor: typeColor,
            connectionCount: n.connection_count || 0,
            depth: 1.0,
            isPeripheral: 0,
        };

        if (n.photo_url) {
            nodeData.photo_url = n.photo_url;
        } else if (TYPE_ICONS[n.entity_type]) {
            nodeData.photo_url = TYPE_ICONS[n.entity_type];
            nodeData.isIcon = 1;
        }

        elements.push({
            group: 'nodes',
            data: nodeData,
            position: positions[String(n.id)] || { x: 0, y: 0 },
        });
        nodeIds.add(String(n.id));
    });

    // ---- Peripheral branch anchors + Ring 1 entities ----
    const otherBranches = Object.keys(BRANCHES).filter(k => k !== branchKey);
    otherBranches.forEach(key => {
        const branch = BRANCHES[key];
        const anchorId = 'anchor_' + key;
        const scale = scales[anchorId] || 0.5;
        const depth = depths[anchorId] || 0.5;

        // Branch anchor node
        elements.push({
            group: 'nodes',
            data: {
                id: anchorId,
                label: '',
                branchLabel: branch.label,
                size: Math.round(50 * scale),
                color: branch.color,
                borderColor: branch.color,
                depth: depth,
                isPeripheral: 1,
            },
            classes: 'branch-anchor',
            position: positions[anchorId],
        });
        nodeIds.add(anchorId);

        // Ring 1 entities of this peripheral branch
        graphData.nodes.forEach(n => {
            const info = branchAssignments[String(n.id)];
            if (!info || info.branch !== key || info.ring !== 1) return;

            const nodeSize = Math.round(BRANCH_NODE_SIZES[1] * scale * 0.7);
            const typeColor = TYPE_COLORS[n.entity_type] || '#888';

            const nodeData = {
                id: String(n.id),
                label: depth > 0.45 ? n.name : '',
                entityId: n.id,
                entityType: n.entity_type,
                branchKey: info.branch,
                ring: info.ring,
                size: nodeSize,
                color: branch.color,
                borderColor: typeColor,
                connectionCount: n.connection_count || 0,
                depth: depth,
                isPeripheral: 1,
            };

            if (n.photo_url) {
                nodeData.photo_url = n.photo_url;
            } else if (TYPE_ICONS[n.entity_type]) {
                nodeData.photo_url = TYPE_ICONS[n.entity_type];
                nodeData.isIcon = 1;
            }

            elements.push({
                group: 'nodes',
                data: nodeData,
                position: positions[String(n.id)] || { x: 0, y: 0 },
            });
            nodeIds.add(String(n.id));
        });
    });

    // ---- Edges: intra-branch + cross-branch to peripheral Ring 1 ----
    graphData.edges.forEach(e => {
        const srcId = String(e.source);
        const tgtId = String(e.target);
        if (!nodeIds.has(srcId) || !nodeIds.has(tgtId)) return;

        const srcInfo = branchAssignments[srcId];
        const tgtInfo = branchAssignments[tgtId];
        if (!srcInfo || !tgtInfo) return;

        const srcIsActive = srcInfo.branch === branchKey;
        const tgtIsActive = tgtInfo.branch === branchKey;

        // Only: intra-branch OR cross-branch with one end in active branch
        if (!srcIsActive && !tgtIsActive) return;

        const isCrossBranch = srcIsActive !== tgtIsActive;
        const cpDist = isCrossBranch ? 0 : computeCenterPull(positions, srcId, tgtId);

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
                cpDist: cpDist,
                isCrossBranch: isCrossBranch ? 1 : 0,
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
        navStack = [];
        Dossier.close();
        if (activeBranchView) {
            buildBranchMap(activeBranchView);
        } else {
            buildRadialMap();
        }
        updateBreadcrumb();
        return;
    }

    // Rebuild the radial/focused view
    if (activeBranchView) {
        buildBranchMap(activeBranchView);
    } else {
        buildRadialMap();
    }
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


function computeBfsRingMap(centerId, neighborhood) {
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
    return ringMap;
}


function computeEgoPositions(centerId, neighborhood) {
    const positions = {};
    positions[String(centerId)] = { x: 0, y: 0 };

    const ringMap = computeBfsRingMap(centerId, neighborhood);

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

    const ringMap = computeBfsRingMap(centerId, neighborhood);

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
        } else if (TYPE_ICONS[n.entity_type]) {
            nodeData.photo_url = TYPE_ICONS[n.entity_type];
            nodeData.isIcon = 1;
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

        const cpDist = computeCenterPull(positions, srcId, tgtId);

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
                cpDist: cpDist,
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
            if (node.hasClass('title-badge') || node.hasClass('branch-anchor') || node.hasClass('branch-center')) return;
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
        cy.elements().addClass('dimmed');

        node.removeClass('dimmed').addClass('highlighted');
        connectedEdges.removeClass('dimmed').addClass('highlighted');
        connectedNodes.removeClass('dimmed');

        cy.nodes('.title-badge, .branch-anchor, .branch-center').removeClass('dimmed');
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


// ---- Branch Focus ----

function toggleBranchFocus(branchKey) {
    if (!cy || egoMode) return;

    if (activeBranchView === branchKey) {
        // Already viewing this branch — go back to hub
        buildRadialMap();
        if (typeof updateBreadcrumb === 'function') updateBreadcrumb();
        return;
    }

    buildBranchMap(branchKey);
    if (typeof updateBreadcrumb === 'function') updateBreadcrumb();
}

function clearBranchFocus() {
    if (!cy || !activeBranchView) return;
    buildRadialMap();
    if (typeof updateBreadcrumb === 'function') updateBreadcrumb();
}


// ---- Ring Rotation ----

function updatePeripheralPositions() {
    if (!cy || !ringState.otherBranches.length) return;

    const N = ringState.otherBranches.length;
    const R = RING_LAYOUT.peripheralRadius;

    cy.batch(() => {
        ringState.otherBranches.forEach((key, i) => {
            const theta = 2 * Math.PI * i / N + ringState.rotation;
            const cx = R * Math.sin(theta);
            const cy_pos = R * Math.cos(theta) * RING_LAYOUT.tilt;
            const depth = (1 + Math.cos(theta)) / 2;
            const scale = RING_LAYOUT.minScale + (RING_LAYOUT.maxScale - RING_LAYOUT.minScale) * depth;

            // Update branch anchor
            const anchorNode = cy.getElementById('anchor_' + key);
            if (anchorNode && !anchorNode.empty()) {
                anchorNode.position({ x: cx, y: cy_pos });
                anchorNode.data('size', Math.round(50 * scale));
                anchorNode.data('depth', depth);
            }

            // Update Ring 1 entities in this cluster
            const ring1 = ringState.branchRing1[key] || [];
            const miniR = RING_LAYOUT.clusterRadius * scale;
            ring1.forEach((eid, j) => {
                const miniAngle = -Math.PI / 2 + (2 * Math.PI * j / ring1.length);
                const node = cy.getElementById(String(eid));
                if (node && !node.empty()) {
                    node.position({
                        x: cx + Math.cos(miniAngle) * miniR,
                        y: cy_pos + Math.sin(miniAngle) * miniR,
                    });
                    node.data('size', Math.round(BRANCH_NODE_SIZES[1] * scale * 0.7));
                    node.data('depth', depth);
                    node.data('label', depth > 0.45 ? (ringState.entityNames[eid] || '') : '');
                }
            });
        });
    });
}


function animateRingRotation(targetRotation, onComplete) {
    const startRotation = ringState.rotation;
    const duration = 300;
    const startTime = performance.now();

    function step(now) {
        const elapsed = now - startTime;
        const t = Math.min(elapsed / duration, 1);
        const eased = 1 - (1 - t) * (1 - t); // ease-out quadratic

        ringState.rotation = startRotation + (targetRotation - startRotation) * eased;
        updatePeripheralPositions();

        if (t < 1) {
            requestAnimationFrame(step);
        } else if (onComplete) {
            onComplete();
        }
    }

    requestAnimationFrame(step);
}


function snapToNearestBranch() {
    if (!ringState.otherBranches.length) return;

    const N = ringState.otherBranches.length;
    const snapThreshold = Math.PI / N; // half the angle between branches

    // Small drag — snap back without switching
    if (Math.abs(ringState.rotation - ringState.dragStartRotation) < snapThreshold * 0.5) {
        animateRingRotation(ringState.dragStartRotation, null);
        return;
    }

    // Find which branch is closest to the front (theta ≈ 0)
    let bestIdx = 0;
    let bestDist = Infinity;

    for (let i = 0; i < N; i++) {
        let theta = (2 * Math.PI * i / N + ringState.rotation) % (2 * Math.PI);
        if (theta > Math.PI) theta -= 2 * Math.PI;
        if (theta < -Math.PI) theta += 2 * Math.PI;

        if (Math.abs(theta) < bestDist) {
            bestDist = Math.abs(theta);
            bestIdx = i;
        }
    }

    const frontBranch = ringState.otherBranches[bestIdx];

    // Animate to align this branch to front, then switch
    const targetRotation = -(2 * Math.PI * bestIdx / N);
    let diff = targetRotation - ringState.rotation;
    while (diff > Math.PI) diff -= 2 * Math.PI;
    while (diff < -Math.PI) diff += 2 * Math.PI;

    animateRingRotation(ringState.rotation + diff, () => {
        ringState.rotation = 0;
        buildBranchMap(frontBranch);
        if (typeof updateBreadcrumb === 'function') updateBreadcrumb();
    });
}


// ---- Hover (lightweight) ----

function hoverHighlight(node) {
    if (!cy) return;
    if (activeBranchFilter) return;
    if (cy.elements('.highlighted').length > 0) return;

    const connectedEdges = node.connectedEdges();
    connectedEdges.forEach(e => {
        e.style('line-opacity', LINE_HIGHLIGHT_OPACITY);
        e.style('width', 1.2);
    });
}

function hoverClear() {
    if (!cy) return;
    if (activeBranchFilter) return;
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
    ENTITY_BRANCH_MAP = {};
    for (const [id, info] of Object.entries(assignments)) {
        ENTITY_BRANCH_MAP[id] = { branch: info.branch, ring: info.ring };
    }
}
