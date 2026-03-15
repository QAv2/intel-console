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
let activeBranchFilter = null; // currently focused branch key, or null

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

        // Branch anchor click — toggle branch focus
        if (node.hasClass('branch-anchor')) {
            const branchKey = node.id().replace('anchor_', '');
            toggleBranchFocus(branchKey);
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
    activeBranchFilter = null;

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

    // Edges — compute center-pull bezier distance for each
    graphData.edges.forEach(e => {
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


/**
 * Compute signed perpendicular distance to pull an edge's bezier
 * control point toward center (0,0) — spiderweb aesthetic.
 *
 * pullFactor controls how aggressively curves bow inward:
 *   0.0 = straight line, 0.5 = halfway to center, 1.0 = through center
 */
const CENTER_PULL_FACTOR = 0.45;

function computeCenterPull(positions, srcId, tgtId) {
    const p1 = positions[srcId];
    const p2 = positions[tgtId];
    if (!p1 || !p2) return 0;

    // Midpoint of the edge
    const mx = (p1.x + p2.x) / 2;
    const my = (p1.y + p2.y) / 2;

    // Vector from midpoint toward center (0,0)
    const toCenterX = -mx;
    const toCenterY = -my;

    // Edge direction vector (source → target)
    const dx = p2.x - p1.x;
    const dy = p2.y - p1.y;
    const edgeLen = Math.sqrt(dx * dx + dy * dy);
    if (edgeLen < 1) return 0;

    // Unit perpendicular to edge (rotate 90° left: (-dy, dx))
    const perpX = -dy / edgeLen;
    const perpY = dx / edgeLen;

    // Project the center-pull vector onto the perpendicular
    // This gives the signed distance: positive = left of src→tgt
    const projection = (toCenterX * perpX + toCenterY * perpY) * CENTER_PULL_FACTOR;

    // Clamp to avoid extreme curves on very short edges
    const maxPull = edgeLen * 0.6;
    return Math.max(-maxPull, Math.min(maxPull, projection));
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


// ---- Branch Focus ----

function toggleBranchFocus(branchKey) {
    if (!cy || !hubMode) return;

    if (activeBranchFilter === branchKey) {
        clearBranchFocus();
        return;
    }

    activeBranchFilter = branchKey;

    cy.batch(() => {
        cy.elements().removeClass('dimmed highlighted');

        // Dim all entity nodes and edges
        cy.nodes().forEach(node => {
            if (node.hasClass('title-badge')) return;

            if (node.hasClass('branch-anchor')) {
                // Dim other branch anchors
                const key = node.id().replace('anchor_', '');
                if (key !== branchKey) {
                    node.addClass('dimmed');
                }
                return;
            }

            const nodeBranch = node.data('branchKey');
            if (nodeBranch !== branchKey) {
                node.addClass('dimmed');
            }
        });

        // Dim edges not connecting two nodes in this branch
        cy.edges().forEach(edge => {
            const srcBranch = edge.source().data('branchKey');
            const tgtBranch = edge.target().data('branchKey');
            if (srcBranch !== branchKey && tgtBranch !== branchKey) {
                edge.addClass('dimmed');
            } else {
                edge.style('line-opacity', LINE_HIGHLIGHT_OPACITY);
                edge.style('width', 1.2);
            }
        });
    });

    // Zoom to the branch
    const branchNodes = cy.nodes().filter(n =>
        n.data('branchKey') === branchKey || n.id() === 'anchor_' + branchKey
    );
    if (branchNodes.length > 0) {
        cy.animate({
            fit: { eles: branchNodes, padding: 80 },
            duration: 400,
            easing: 'ease-in-out',
        });
    }
}

function clearBranchFocus() {
    if (!cy) return;
    activeBranchFilter = null;

    cy.batch(() => {
        cy.elements().removeClass('dimmed highlighted');
        cy.edges().removeStyle('line-opacity width');
    });

    cy.animate({
        fit: { eles: cy.elements(), padding: 60 },
        duration: 300,
    });
}


// ---- Hover (lightweight) ----

function hoverHighlight(node) {
    if (!cy) return;
    if (activeBranchFilter) return; // Branch focus takes precedence
    if (cy.elements('.highlighted').length > 0) return; // Active highlight takes precedence

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
    // Also set global for backwards compat
    ENTITY_BRANCH_MAP = {};
    for (const [id, info] of Object.entries(assignments)) {
        ENTITY_BRANCH_MAP[id] = { branch: info.branch, ring: info.ring };
    }
}
