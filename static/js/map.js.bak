/**
 * Intel Console — SVG Radial Transformation Map Engine
 * Pure vanilla JS + SVG, no dependencies
 *
 * Two layers:
 *   Layer 1: Radial map — Epstein at center, 7 branches, all entities
 *   Layer 2: Ego mode — click a person → concentric rings (BFS depth 2)
 *
 * Replaces graph.js (Cytoscape). Modeled on inner-sanctum/js/main.js.
 */

// ---- Constants ----
const SVG_NS = 'http://www.w3.org/2000/svg';

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

// Radial layout distances
const CENTER_RADIUS = 55;
const BRANCH_RING = 160;
const RING1_DISTANCE = 280;
const RING2_DISTANCE = 440;
const RING3_DISTANCE = 600;

// Node sizes
const NODE_RADII = {
    center: 55,
    ring1: 22,
    ring2: 16,
    ring3: 12,
    anchor: 28,
};

// Ego mode distances
const EGO_RING0_DIST = 0;
const EGO_RING1_DIST = 200;
const EGO_RING2_DIST = 380;
const EGO_NODE_RADII = [45, 22, 14];

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

const state = {
    selectedNode: null,
    showConnections: true,
    zoom: 1,
    panX: 0, panY: 0,
    isPanning: false,
    panStartX: 0, panStartY: 0,
    panStartViewX: 0, panStartViewY: 0,
    viewBox: { x: -800, y: -700, w: 1600, h: 1400 },
    nodePositions: {},
    nodeElements: {},
    edgeElements: [],
    branchAnchors: {},
    activeTiers: new Set(['documented', 'credible', 'inference', 'speculative']),
    activeTypes: null,
    yearMin: null,
    yearMax: null,
    showUndated: true,
};

let svg = null;
let layerEdges = null;
let layerSpokes = null;
let layerNodes = null;
let layerLabels = null;

// ---- Helpers ----
function svgEl(tag, attrs) {
    const el = document.createElementNS(SVG_NS, tag);
    if (attrs) {
        for (const [k, v] of Object.entries(attrs)) {
            el.setAttribute(k, v);
        }
    }
    return el;
}

function deg2rad(deg) {
    return deg * Math.PI / 180;
}

function updateViewBox() {
    const vb = state.viewBox;
    svg.setAttribute('viewBox', `${vb.x} ${vb.y} ${vb.w} ${vb.h}`);
}

function getNodeById(id) {
    if (!graphData) return null;
    return graphData.nodes.find(n => n.id === id) || null;
}


// ---- Store graph data (called from app.js) ----
function storeGraphData(data) {
    graphData = data;
}


// ============================================================
//  Layer 1 — Radial Map
// ============================================================

function computeRadialPositions() {
    state.nodePositions = {};
    if (!graphData) return;

    // Center node
    state.nodePositions[CENTER_ENTITY_ID] = { x: 0, y: 0 };

    const branchKeys = Object.keys(BRANCHES);

    branchKeys.forEach(bKey => {
        const branch = BRANCHES[bKey];
        const baseAngle = branch.angle;
        const baseRad = deg2rad(baseAngle);

        // Branch anchor position
        state.nodePositions['anchor_' + bKey] = {
            x: Math.cos(baseRad) * BRANCH_RING,
            y: Math.sin(baseRad) * BRANCH_RING,
        };

        // Gather entities for this branch by ring
        const ring1 = [], ring2 = [], ring3 = [];
        for (const [idStr, mapping] of Object.entries(ENTITY_BRANCH_MAP)) {
            if (mapping.branch !== bKey) continue;
            const id = parseInt(idStr);
            if (id === CENTER_ENTITY_ID) continue;
            if (mapping.ring === 1) ring1.push(id);
            else if (mapping.ring === 2) ring2.push(id);
            else ring3.push(id);
        }

        // Place ring 1 entities fanned around branch angle
        const spread1 = Math.min(18, 40 / Math.max(ring1.length, 1));
        const start1 = baseAngle - ((ring1.length - 1) * spread1) / 2;
        ring1.forEach((id, i) => {
            const angle = deg2rad(start1 + i * spread1);
            state.nodePositions[id] = {
                x: Math.cos(angle) * RING1_DISTANCE,
                y: Math.sin(angle) * RING1_DISTANCE,
            };
        });

        // Place ring 2
        const spread2 = Math.min(14, 36 / Math.max(ring2.length, 1));
        const start2 = baseAngle - ((ring2.length - 1) * spread2) / 2;
        ring2.forEach((id, i) => {
            const angle = deg2rad(start2 + i * spread2);
            state.nodePositions[id] = {
                x: Math.cos(angle) * RING2_DISTANCE,
                y: Math.sin(angle) * RING2_DISTANCE,
            };
        });

        // Place ring 3
        const spread3 = Math.min(10, 32 / Math.max(ring3.length, 1));
        const start3 = baseAngle - ((ring3.length - 1) * spread3) / 2;
        ring3.forEach((id, i) => {
            const angle = deg2rad(start3 + i * spread3);
            state.nodePositions[id] = {
                x: Math.cos(angle) * RING3_DISTANCE,
                y: Math.sin(angle) * RING3_DISTANCE,
            };
        });
    });
}

function buildRadialMap() {
    if (!graphData) return;
    hubMode = true;
    egoMode = false;
    currentCenterId = null;
    state.selectedNode = null;

    clearSVG();
    computeRadialPositions();

    // Create SVG layers
    layerEdges = svgEl('g', { class: 'layer-edges' });
    layerSpokes = svgEl('g', { class: 'layer-spokes' });
    layerNodes = svgEl('g', { class: 'layer-nodes' });
    layerLabels = svgEl('g', { class: 'layer-labels' });
    svg.appendChild(layerEdges);
    svg.appendChild(layerSpokes);
    svg.appendChild(layerNodes);
    svg.appendChild(layerLabels);

    // Draw defs (filters, gradients)
    const defs = svgEl('defs');
    // Glow filter for center node
    const filter = svgEl('filter', { id: 'glow', x: '-50%', y: '-50%', width: '200%', height: '200%' });
    const feGaussian = svgEl('feGaussianBlur', { stdDeviation: '6', result: 'coloredBlur' });
    filter.appendChild(feGaussian);
    const feMerge = svgEl('feMerge');
    const feMergeNode1 = svgEl('feMergeNode', { in: 'coloredBlur' });
    const feMergeNode2 = svgEl('feMergeNode', { in: 'SourceGraphic' });
    feMerge.appendChild(feMergeNode1);
    feMerge.appendChild(feMergeNode2);
    filter.appendChild(feMerge);
    defs.appendChild(filter);
    svg.insertBefore(defs, layerEdges);

    // Draw cross-connections (edges from graphData between entities in different branches)
    drawRadialEdges();

    // Draw spokes from center through each branch
    const branchKeys = Object.keys(BRANCHES);
    branchKeys.forEach(bKey => {
        const branch = BRANCHES[bKey];
        const rad = deg2rad(branch.angle);
        const endX = Math.cos(rad) * (RING3_DISTANCE + 60);
        const endY = Math.sin(rad) * (RING3_DISTANCE + 60);
        const spoke = svgEl('line', {
            x1: 0, y1: 0, x2: endX, y2: endY,
            stroke: branch.color,
            'stroke-width': '1',
            'stroke-opacity': '0.12',
            'stroke-dasharray': '4,4',
        });
        layerSpokes.appendChild(spoke);
    });

    // Draw branch anchor circles with labels
    branchKeys.forEach(bKey => {
        const branch = BRANCHES[bKey];
        const pos = state.nodePositions['anchor_' + bKey];
        if (!pos) return;

        // Count entities in this branch
        let count = 0;
        for (const mapping of Object.values(ENTITY_BRANCH_MAP)) {
            if (mapping.branch === bKey) count++;
        }

        const g = svgEl('g', { transform: `translate(${pos.x},${pos.y})`, class: 'branch-anchor', 'data-branch': bKey, cursor: 'pointer' });

        // Anchor circle
        const circle = svgEl('circle', {
            cx: 0, cy: 0, r: NODE_RADII.anchor,
            fill: branch.color + '22',
            stroke: branch.color,
            'stroke-width': '2',
        });
        g.appendChild(circle);

        // Count badge
        const countText = svgEl('text', {
            x: 0, y: 1,
            'text-anchor': 'middle',
            'dominant-baseline': 'central',
            fill: branch.color,
            'font-family': "'SF Mono', monospace",
            'font-size': '11',
            'font-weight': '700',
            'pointer-events': 'none',
        });
        countText.textContent = String(count);
        g.appendChild(countText);

        // Label below
        const label = svgEl('text', {
            x: 0, y: NODE_RADII.anchor + 14,
            'text-anchor': 'middle',
            fill: branch.color,
            'font-family': "'SF Mono', monospace",
            'font-size': '8',
            'font-weight': '600',
            'letter-spacing': '0.5',
            opacity: '0.7',
            'pointer-events': 'none',
        });
        label.textContent = branch.label;
        g.appendChild(label);

        // Hover: highlight all entities in this branch
        g.addEventListener('mouseenter', () => {
            if (state.selectedNode) return;
            hoverHighlightBranch(bKey);
        });
        g.addEventListener('mouseleave', () => {
            if (state.selectedNode) return;
            hoverClear();
        });

        // Click: zoom/pan to focus on this branch sector
        g.addEventListener('click', (evt) => {
            evt.stopPropagation();
            focusBranch(bKey);
        });

        layerNodes.appendChild(g);
    });

    // Draw entity nodes
    graphData.nodes.forEach(n => {
        if (n.id === CENTER_ENTITY_ID) return; // draw center last
        const mapping = ENTITY_BRANCH_MAP[n.id];
        if (!mapping) return;
        const pos = state.nodePositions[n.id];
        if (!pos) return;

        const radius = NODE_RADII['ring' + mapping.ring] || NODE_RADII.ring3;
        const branch = BRANCHES[mapping.branch];
        drawEntityNode(n, pos, radius, branch.color, mapping.ring);
    });

    // Draw center node (Epstein)
    const centerNode = getNodeById(CENTER_ENTITY_ID);
    if (centerNode) {
        drawCenterNode(centerNode);
    }

    // Set viewBox
    state.viewBox = { x: -800, y: -700, w: 1600, h: 1400 };
    updateViewBox();

    // Reapply active filters to new edges
    applyEdgeFilters();
}

function drawRadialEdges() {
    if (!graphData) return;
    state.edgeElements = [];

    graphData.edges.forEach(e => {
        const p1 = state.nodePositions[e.source];
        const p2 = state.nodePositions[e.target];
        if (!p1 || !p2) return;

        const tier = e.evidence_tier || 'speculative';
        const color = TIER_COLORS[tier] || TIER_COLORS.speculative;

        // Quadratic bezier curved toward center
        const mx = (p1.x + p2.x) / 2;
        const my = (p1.y + p2.y) / 2;
        const cx = mx * 0.55;
        const cy = my * 0.55;
        const d = `M ${p1.x} ${p1.y} Q ${cx} ${cy} ${p2.x} ${p2.y}`;

        const attrs = {
            d,
            fill: 'none',
            stroke: color,
            'stroke-width': '0.8',
            'stroke-opacity': String(LINE_DEFAULT_OPACITY),
            'data-tier': tier,
            'data-source': String(e.source),
            'data-target': String(e.target),
            class: 'edge-path',
        };
        if (e.year_start != null) attrs['data-year-start'] = String(e.year_start);
        if (e.year_end != null) attrs['data-year-end'] = String(e.year_end);

        const path = svgEl('path', attrs);
        layerEdges.appendChild(path);
        state.edgeElements.push(path);
    });
}

function drawEntityNode(entity, pos, radius, branchColor, ring) {
    const g = svgEl('g', {
        transform: `translate(${pos.x},${pos.y})`,
        class: 'entity-node',
        'data-id': String(entity.id),
        'data-type': entity.entity_type,
        'data-ring': String(ring),
        cursor: 'pointer',
    });

    const typeColor = TYPE_COLORS[entity.entity_type] || '#888';
    const opacity = ring === 3 ? '0.6' : ring === 2 ? '0.8' : '1';
    g.setAttribute('opacity', opacity);

    if (entity.photo_url) {
        // Photo clipped in circle
        const clipId = 'clip-e' + entity.id;
        let defs = svg.querySelector('defs');
        const clipPath = svgEl('clipPath', { id: clipId });
        const clipCircle = svgEl('circle', { cx: 0, cy: 0, r: radius });
        clipPath.appendChild(clipCircle);
        defs.appendChild(clipPath);

        const image = svgEl('image', {
            href: entity.photo_url,
            x: -radius, y: -radius,
            width: radius * 2, height: radius * 2,
            'clip-path': `url(#${clipId})`,
            preserveAspectRatio: 'xMidYMid slice',
        });
        g.appendChild(image);

        // Border circle
        const border = svgEl('circle', {
            cx: 0, cy: 0, r: radius,
            fill: 'none',
            stroke: typeColor,
            'stroke-width': ring === 1 ? '2' : '1.5',
        });
        g.appendChild(border);
    } else {
        // Colored circle with initial
        const circle = svgEl('circle', {
            cx: 0, cy: 0, r: radius,
            fill: typeColor + '22',
            stroke: typeColor,
            'stroke-width': '1.5',
        });
        g.appendChild(circle);

        const initial = entity.name.charAt(0).toUpperCase();
        const text = svgEl('text', {
            x: 0, y: 1,
            'text-anchor': 'middle',
            'dominant-baseline': 'central',
            fill: typeColor,
            'font-family': "'SF Mono', monospace",
            'font-size': String(Math.max(8, radius * 0.7)),
            'font-weight': '600',
        });
        text.textContent = initial;
        g.appendChild(text);
    }

    // Name label below node
    const fontSize = ring === 1 ? 9 : ring === 2 ? 7 : 6;
    const label = svgEl('text', {
        x: 0, y: radius + 10,
        'text-anchor': 'middle',
        fill: 'rgba(255,255,255,0.65)',
        'font-family': "'SF Mono', monospace",
        'font-size': String(fontSize),
        'pointer-events': 'none',
        class: 'node-label',
    });
    // Truncate long names
    const maxLen = ring === 3 ? 14 : ring === 2 ? 18 : 22;
    const displayName = entity.name.length > maxLen
        ? entity.name.substring(0, maxLen - 1) + '\u2026'
        : entity.name;
    label.textContent = displayName;

    layerNodes.appendChild(g);
    layerLabels.appendChild(label);

    // Store label position for later update
    label.setAttribute('x', pos.x);
    label.setAttribute('y', pos.y + radius + 10);

    // Click handler
    g.addEventListener('click', (evt) => {
        evt.stopPropagation();
        if (window._onMapNodeClick) {
            window._onMapNodeClick(entity.id);
        }
    });

    // Hover handler — light up connected edges
    g.addEventListener('mouseenter', () => {
        if (state.selectedNode) return; // don't override click-selection
        hoverHighlight(entity.id);
    });
    g.addEventListener('mouseleave', () => {
        if (state.selectedNode) return;
        hoverClear();
    });

    state.nodeElements[entity.id] = g;
}

function drawCenterNode(entity) {
    const pos = state.nodePositions[CENTER_ENTITY_ID];
    if (!pos) return;
    const r = NODE_RADII.center;

    const g = svgEl('g', {
        transform: `translate(${pos.x},${pos.y})`,
        class: 'entity-node center-node',
        'data-id': String(entity.id),
        cursor: 'pointer',
        filter: 'url(#glow)',
    });

    if (entity.photo_url) {
        const clipId = 'clip-center';
        let defs = svg.querySelector('defs');
        const clipPath = svgEl('clipPath', { id: clipId });
        const clipCircle = svgEl('circle', { cx: 0, cy: 0, r: r });
        clipPath.appendChild(clipCircle);
        defs.appendChild(clipPath);

        const image = svgEl('image', {
            href: entity.photo_url,
            x: -r, y: -r,
            width: r * 2, height: r * 2,
            'clip-path': `url(#${clipId})`,
            preserveAspectRatio: 'xMidYMid slice',
        });
        g.appendChild(image);

        const border = svgEl('circle', {
            cx: 0, cy: 0, r: r,
            fill: 'none',
            stroke: '#ffffff',
            'stroke-width': '3',
        });
        g.appendChild(border);
    } else {
        const circle = svgEl('circle', {
            cx: 0, cy: 0, r: r,
            fill: '#4a9eff22',
            stroke: '#ffffff',
            'stroke-width': '3',
        });
        g.appendChild(circle);
    }

    // Center label
    const label = svgEl('text', {
        x: 0, y: r + 16,
        'text-anchor': 'middle',
        fill: 'rgba(255,255,255,0.9)',
        'font-family': "'SF Mono', monospace",
        'font-size': '12',
        'font-weight': '700',
        'pointer-events': 'none',
    });
    label.textContent = entity.name;

    layerNodes.appendChild(g);
    layerLabels.appendChild(label);

    g.addEventListener('click', (evt) => {
        evt.stopPropagation();
        if (window._onMapNodeClick) {
            window._onMapNodeClick(entity.id);
        }
    });

    // Hover handler — light up connected edges
    g.addEventListener('mouseenter', () => {
        if (state.selectedNode) return;
        hoverHighlight(entity.id);
    });
    g.addEventListener('mouseleave', () => {
        if (state.selectedNode) return;
        hoverClear();
    });

    state.nodeElements[entity.id] = g;
}


// ============================================================
//  Layer 2 — Ego Mode (Concentric Rings)
// ============================================================

function computeRings(centerId, data) {
    const adj = {};
    data.nodes.forEach(n => { adj[n.id] = []; });
    data.edges.forEach(e => {
        if (!adj[e.source]) adj[e.source] = [];
        if (!adj[e.target]) adj[e.target] = [];
        adj[e.source].push(e.target);
        adj[e.target].push(e.source);
    });

    const rings = {};
    const queue = [centerId];
    rings[centerId] = 0;
    while (queue.length > 0) {
        const current = queue.shift();
        for (const n of (adj[current] || [])) {
            if (rings[n] === undefined) {
                rings[n] = rings[current] + 1;
                queue.push(n);
            }
        }
    }
    return rings;
}

function computeEgoPositions(centerId, data) {
    const rings = computeRings(centerId, data);
    const positions = {};

    // Center
    positions[centerId] = { x: 0, y: 0, ring: 0 };

    // Group by ring
    const ring1nodes = [], ring2nodes = [];
    data.nodes.forEach(n => {
        if (n.id === centerId) return;
        const r = rings[n.id] !== undefined ? Math.min(rings[n.id], 2) : 2;
        if (r === 1) ring1nodes.push(n);
        else ring2nodes.push(n);
    });

    // Place ring 1 evenly around center
    const angleStep1 = (2 * Math.PI) / Math.max(ring1nodes.length, 1);
    ring1nodes.forEach((n, i) => {
        const angle = -Math.PI / 2 + i * angleStep1;
        positions[n.id] = {
            x: Math.cos(angle) * EGO_RING1_DIST,
            y: Math.sin(angle) * EGO_RING1_DIST,
            ring: 1,
        };
    });

    // Place ring 2 evenly
    const angleStep2 = (2 * Math.PI) / Math.max(ring2nodes.length, 1);
    ring2nodes.forEach((n, i) => {
        const angle = -Math.PI / 2 + i * angleStep2;
        positions[n.id] = {
            x: Math.cos(angle) * EGO_RING2_DIST,
            y: Math.sin(angle) * EGO_RING2_DIST,
            ring: 2,
        };
    });

    return { positions, rings };
}

async function recenterOn(nodeId) {
    if (isRecentering) return;
    isRecentering = true;
    egoMode = true;
    hubMode = false;

    try {
        const data = await API.getNeighborhood(nodeId, 2);
        const { positions, rings } = computeEgoPositions(nodeId, data);

        clearSVG();
        state.nodePositions = {};
        state.nodeElements = {};
        state.edgeElements = [];

        // Create layers
        layerEdges = svgEl('g', { class: 'layer-edges' });
        layerSpokes = svgEl('g', { class: 'layer-spokes' });
        layerNodes = svgEl('g', { class: 'layer-nodes' });
        layerLabels = svgEl('g', { class: 'layer-labels' });

        // Defs
        const defs = svgEl('defs');
        const filter = svgEl('filter', { id: 'glow', x: '-50%', y: '-50%', width: '200%', height: '200%' });
        const feGaussian = svgEl('feGaussianBlur', { stdDeviation: '6', result: 'coloredBlur' });
        filter.appendChild(feGaussian);
        const feMerge = svgEl('feMerge');
        feMerge.appendChild(svgEl('feMergeNode', { in: 'coloredBlur' }));
        feMerge.appendChild(svgEl('feMergeNode', { in: 'SourceGraphic' }));
        filter.appendChild(feMerge);
        defs.appendChild(filter);

        svg.appendChild(defs);
        svg.appendChild(layerEdges);
        svg.appendChild(layerSpokes);
        svg.appendChild(layerNodes);
        svg.appendChild(layerLabels);

        // Draw concentric ring guides
        [EGO_RING1_DIST, EGO_RING2_DIST].forEach(dist => {
            const guide = svgEl('circle', {
                cx: 0, cy: 0, r: dist,
                fill: 'none',
                stroke: 'rgba(255,255,255,0.04)',
                'stroke-width': '1',
                'stroke-dasharray': '6,6',
            });
            layerSpokes.appendChild(guide);
        });

        // Store positions
        for (const [idStr, pos] of Object.entries(positions)) {
            state.nodePositions[parseInt(idStr)] = pos;
        }

        // Draw edges
        data.edges.forEach(e => {
            const p1 = positions[e.source];
            const p2 = positions[e.target];
            if (!p1 || !p2) return;

            const tier = e.evidence_tier || 'speculative';
            const color = TIER_COLORS[tier] || TIER_COLORS.speculative;

            const srcRing = rings[e.source] !== undefined ? Math.min(rings[e.source], 2) : 2;
            const tgtRing = rings[e.target] !== undefined ? Math.min(rings[e.target], 2) : 2;
            const isCenter = srcRing === 0 || tgtRing === 0;
            const opacity = isCenter ? 0.4 : 0.15;
            const width = isCenter ? 1.2 : 0.7;

            // Bezier curved toward center
            const mx = (p1.x + p2.x) / 2;
            const my = (p1.y + p2.y) / 2;
            const cx = mx * 0.6;
            const cy = my * 0.6;
            const d = `M ${p1.x} ${p1.y} Q ${cx} ${cy} ${p2.x} ${p2.y}`;

            const eAttrs = {
                d,
                fill: 'none',
                stroke: color,
                'stroke-width': String(width),
                'stroke-opacity': String(opacity),
                'data-tier': tier,
                'data-source': String(e.source),
                'data-target': String(e.target),
                class: 'edge-path',
            };
            if (e.year_start != null) eAttrs['data-year-start'] = String(e.year_start);
            if (e.year_end != null) eAttrs['data-year-end'] = String(e.year_end);

            const path = svgEl('path', eAttrs);
            layerEdges.appendChild(path);
            state.edgeElements.push(path);
        });

        // Draw nodes
        data.nodes.forEach(n => {
            const pos = positions[n.id];
            if (!pos) return;
            const ring = pos.ring;
            const radius = EGO_NODE_RADII[ring] || EGO_NODE_RADII[2];

            if (n.id === nodeId) {
                // Center node in ego
                drawEgoCenterNode(n, pos, radius);
            } else {
                const typeColor = TYPE_COLORS[n.entity_type] || '#888';
                drawEntityNode(n, pos, radius, typeColor, ring === 0 ? 1 : ring);
            }
        });

        currentCenterId = nodeId;

        // ViewBox for ego mode
        state.viewBox = { x: -500, y: -500, w: 1000, h: 1000 };
        updateViewBox();

        // Reapply active filters to new edges
        applyEdgeFilters();

    } finally {
        setTimeout(() => { isRecentering = false; }, 200);
    }
}

function drawEgoCenterNode(entity, pos, radius) {
    const r = radius;
    const g = svgEl('g', {
        transform: `translate(${pos.x},${pos.y})`,
        class: 'entity-node center-node',
        'data-id': String(entity.id),
        cursor: 'pointer',
        filter: 'url(#glow)',
    });

    if (entity.photo_url) {
        const clipId = 'clip-ego-center';
        let defs = svg.querySelector('defs');
        const clipPath = svgEl('clipPath', { id: clipId });
        const clipCircle = svgEl('circle', { cx: 0, cy: 0, r: r });
        clipPath.appendChild(clipCircle);
        defs.appendChild(clipPath);

        const image = svgEl('image', {
            href: entity.photo_url,
            x: -r, y: -r,
            width: r * 2, height: r * 2,
            'clip-path': `url(#${clipId})`,
            preserveAspectRatio: 'xMidYMid slice',
        });
        g.appendChild(image);

        const border = svgEl('circle', {
            cx: 0, cy: 0, r: r,
            fill: 'none',
            stroke: '#ffffff',
            'stroke-width': '3',
        });
        g.appendChild(border);
    } else {
        const typeColor = TYPE_COLORS[entity.entity_type] || '#4a9eff';
        const circle = svgEl('circle', {
            cx: 0, cy: 0, r: r,
            fill: typeColor + '22',
            stroke: '#ffffff',
            'stroke-width': '3',
        });
        g.appendChild(circle);

        const initial = entity.name.charAt(0).toUpperCase();
        const text = svgEl('text', {
            x: 0, y: 1,
            'text-anchor': 'middle',
            'dominant-baseline': 'central',
            fill: '#ffffff',
            'font-family': "'SF Mono', monospace",
            'font-size': String(r * 0.5),
            'font-weight': '700',
        });
        text.textContent = initial;
        g.appendChild(text);
    }

    // Label
    const label = svgEl('text', {
        x: pos.x, y: pos.y + r + 16,
        'text-anchor': 'middle',
        fill: 'rgba(255,255,255,0.9)',
        'font-family': "'SF Mono', monospace",
        'font-size': '12',
        'font-weight': '700',
        'pointer-events': 'none',
    });
    label.textContent = entity.name;

    layerNodes.appendChild(g);
    layerLabels.appendChild(label);

    g.addEventListener('click', (evt) => {
        evt.stopPropagation();
        if (window._onMapNodeClick) {
            window._onMapNodeClick(entity.id);
        }
    });

    g.addEventListener('mouseenter', () => {
        if (state.selectedNode) return;
        hoverHighlight(entity.id);
    });
    g.addEventListener('mouseleave', () => {
        if (state.selectedNode) return;
        hoverClear();
    });

    state.nodeElements[entity.id] = g;
}


// ============================================================
//  Full Graph (stub — radial map replaces this use case)
// ============================================================

function loadFullGraph() {
    buildRadialMap();
}

function loadHubSplash() {
    buildRadialMap();
}


// ============================================================
//  Hover Highlight (lightweight — edges only, no node dimming)
// ============================================================

function hoverHighlight(nodeId) {
    // Dim all nodes slightly, brighten hovered + neighbors
    const connected = new Set([nodeId]);
    state.edgeElements.forEach(path => {
        const src = parseInt(path.getAttribute('data-source'));
        const tgt = parseInt(path.getAttribute('data-target'));
        if (src === nodeId) connected.add(tgt);
        if (tgt === nodeId) connected.add(src);
    });

    // Dim non-connected nodes
    svg.querySelectorAll('.entity-node').forEach(el => {
        const id = parseInt(el.getAttribute('data-id'));
        el.style.opacity = connected.has(id) ? '1' : String(DIM_OPACITY);
    });
    svg.querySelectorAll('.branch-anchor').forEach(el => {
        el.style.opacity = String(DIM_OPACITY);
    });

    // Brighten connected edges, dim the rest
    state.edgeElements.forEach(path => {
        const src = parseInt(path.getAttribute('data-source'));
        const tgt = parseInt(path.getAttribute('data-target'));
        if (src === nodeId || tgt === nodeId) {
            path.setAttribute('stroke-opacity', String(LINE_HIGHLIGHT_OPACITY));
            path.setAttribute('stroke-width', '2');
        } else {
            path.setAttribute('stroke-opacity', '0.02');
        }
    });
}

function hoverClear() {
    // Restore default opacities
    svg.querySelectorAll('.entity-node').forEach(el => {
        const ring = el.getAttribute('data-ring');
        if (ring === '3') el.style.opacity = '0.6';
        else if (ring === '2') el.style.opacity = '0.8';
        else el.style.opacity = '1';
    });
    svg.querySelectorAll('.branch-anchor').forEach(el => {
        el.style.opacity = '1';
    });
    state.edgeElements.forEach(path => {
        path.setAttribute('stroke-opacity', String(LINE_DEFAULT_OPACITY));
        path.setAttribute('stroke-width', '0.8');
    });
}


// ============================================================
//  Branch Hover / Focus
// ============================================================

function hoverHighlightBranch(branchKey) {
    // Collect all entity IDs in this branch
    const branchIds = new Set();
    for (const [idStr, mapping] of Object.entries(ENTITY_BRANCH_MAP)) {
        if (mapping.branch === branchKey) branchIds.add(parseInt(idStr));
    }
    // Include center node as connected
    branchIds.add(CENTER_ENTITY_ID);

    // Dim non-branch nodes
    svg.querySelectorAll('.entity-node').forEach(el => {
        const id = parseInt(el.getAttribute('data-id'));
        el.style.opacity = branchIds.has(id) ? '1' : String(DIM_OPACITY);
    });
    svg.querySelectorAll('.branch-anchor').forEach(el => {
        el.style.opacity = el.getAttribute('data-branch') === branchKey ? '1' : String(DIM_OPACITY);
    });

    // Brighten edges where both endpoints are in this branch (or center)
    state.edgeElements.forEach(path => {
        const src = parseInt(path.getAttribute('data-source'));
        const tgt = parseInt(path.getAttribute('data-target'));
        if (branchIds.has(src) && branchIds.has(tgt)) {
            path.setAttribute('stroke-opacity', String(LINE_HIGHLIGHT_OPACITY));
            path.setAttribute('stroke-width', '1.5');
        } else if (branchIds.has(src) || branchIds.has(tgt)) {
            // Cross-branch edge touching this branch — show dimmer
            path.setAttribute('stroke-opacity', '0.25');
            path.setAttribute('stroke-width', '1');
        } else {
            path.setAttribute('stroke-opacity', '0.02');
        }
    });
}

function focusBranch(branchKey) {
    const branch = BRANCHES[branchKey];
    if (!branch) return;

    // Find bounding box of all entities in this branch
    let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
    for (const [idStr, mapping] of Object.entries(ENTITY_BRANCH_MAP)) {
        if (mapping.branch !== branchKey) continue;
        const pos = state.nodePositions[parseInt(idStr)];
        if (!pos) continue;
        minX = Math.min(minX, pos.x);
        minY = Math.min(minY, pos.y);
        maxX = Math.max(maxX, pos.x);
        maxY = Math.max(maxY, pos.y);
    }
    // Include center node
    minX = Math.min(minX, 0);
    minY = Math.min(minY, 0);
    maxX = Math.max(maxX, 0);
    maxY = Math.max(maxY, 0);

    // Add padding
    const pad = 80;
    minX -= pad; minY -= pad;
    maxX += pad; maxY += pad;

    const w = maxX - minX;
    const h = maxY - minY;
    // Maintain aspect ratio
    const aspect = 1600 / 1400;
    let vw = w, vh = h;
    if (vw / vh > aspect) {
        vh = vw / aspect;
    } else {
        vw = vh * aspect;
    }

    state.viewBox = {
        x: minX - (vw - w) / 2,
        y: minY - (vh - h) / 2,
        w: vw,
        h: vh,
    };
    updateViewBox();

    // Also highlight the branch
    hoverHighlightBranch(branchKey);
}


// ============================================================
//  SVG Clear / Selection / Highlight
// ============================================================

function clearSVG() {
    while (svg && svg.firstChild) {
        svg.removeChild(svg.firstChild);
    }
    state.nodeElements = {};
    state.edgeElements = [];
    state.selectedNode = null;
    layerEdges = null;
    layerSpokes = null;
    layerNodes = null;
    layerLabels = null;
}

function highlightNode(nodeId) {
    // Dim everything, brighten selected + connected edges
    const allNodes = svg.querySelectorAll('.entity-node, .branch-anchor');
    const allLabels = svg.querySelectorAll('.node-label');
    const allEdges = svg.querySelectorAll('.edge-path');

    // Find connected node IDs via edges
    const connected = new Set([nodeId]);
    allEdges.forEach(path => {
        const src = parseInt(path.getAttribute('data-source'));
        const tgt = parseInt(path.getAttribute('data-target'));
        if (src === nodeId) connected.add(tgt);
        if (tgt === nodeId) connected.add(src);
    });

    allNodes.forEach(el => {
        const id = parseInt(el.getAttribute('data-id'));
        if (connected.has(id)) {
            el.style.opacity = '1';
        } else {
            el.style.opacity = String(DIM_OPACITY);
        }
    });

    // Dim branch anchors
    svg.querySelectorAll('.branch-anchor').forEach(el => {
        el.style.opacity = String(DIM_OPACITY);
    });

    allEdges.forEach(path => {
        const src = parseInt(path.getAttribute('data-source'));
        const tgt = parseInt(path.getAttribute('data-target'));
        if (src === nodeId || tgt === nodeId) {
            path.setAttribute('stroke-opacity', String(LINE_HIGHLIGHT_OPACITY));
            path.setAttribute('stroke-width', '2');
        } else {
            path.setAttribute('stroke-opacity', '0.03');
        }
    });

    state.selectedNode = nodeId;
}

function clearHighlight() {
    const allNodes = svg.querySelectorAll('.entity-node');
    allNodes.forEach(el => {
        const ring = el.getAttribute('data-ring');
        if (ring === '3') el.style.opacity = '0.6';
        else if (ring === '2') el.style.opacity = '0.8';
        else el.style.opacity = '1';
    });

    svg.querySelectorAll('.branch-anchor').forEach(el => {
        el.style.opacity = '1';
    });

    state.edgeElements.forEach(path => {
        path.setAttribute('stroke-opacity', String(LINE_DEFAULT_OPACITY));
        path.setAttribute('stroke-width', path.getAttribute('data-tier') ? '0.8' : '0.7');
    });

    state.selectedNode = null;
}

function selectNode(nodeId) {
    highlightNode(nodeId);
}

function deselectAll() {
    clearHighlight();
}

function focusNode(nodeId) {
    const pos = state.nodePositions[nodeId];
    if (!pos) return;

    // Pan viewBox to center on this node
    const vb = state.viewBox;
    state.viewBox.x = pos.x - vb.w / 2;
    state.viewBox.y = pos.y - vb.h / 2;
    updateViewBox();
}


// ============================================================
//  Filters
// ============================================================

function filterByTier(activeTiers) {
    state.activeTiers = activeTiers;
    applyEdgeFilters();
}

function filterByType(activeTypes) {
    state.activeTypes = activeTypes;
    svg.querySelectorAll('.entity-node[data-type]').forEach(el => {
        const type = el.getAttribute('data-type');
        if (activeTypes.has(type)) {
            el.style.display = '';
        } else {
            el.style.display = 'none';
        }
    });
}

function filterByYear(yearMin, yearMax, showUndated) {
    state.yearMin = yearMin;
    state.yearMax = yearMax;
    state.showUndated = showUndated;
    applyEdgeFilters();
}

/**
 * Combined edge filter — checks both tier and year constraints.
 * An edge is visible only if it passes ALL active filters.
 */
function applyEdgeFilters() {
    const { activeTiers, yearMin, yearMax, showUndated } = state;
    const hasYearFilter = yearMin != null && yearMax != null;

    state.edgeElements.forEach(path => {
        // Tier check
        const tier = path.getAttribute('data-tier');
        if (!activeTiers.has(tier)) {
            path.style.display = 'none';
            return;
        }

        // Year check (skip if timeline not initialized)
        if (hasYearFilter) {
            const ys = path.getAttribute('data-year-start');
            const ye = path.getAttribute('data-year-end');

            if (!ys && !ye) {
                path.style.display = showUndated ? '' : 'none';
                return;
            }

            const start = ys ? parseInt(ys) : parseInt(ye);
            const end = ye ? parseInt(ye) : parseInt(ys);
            const visible = end >= yearMin && start <= yearMax;
            path.style.display = visible ? '' : 'none';
            return;
        }

        path.style.display = '';
    });
}


// ============================================================
//  Pan & Zoom
// ============================================================

function initPanZoom() {
    // Mouse drag to pan
    svg.addEventListener('mousedown', (e) => {
        if (e.target === svg || e.target.closest('.layer-edges') || e.target.closest('.layer-spokes')) {
            state.isPanning = true;
            state.panStartX = e.clientX;
            state.panStartY = e.clientY;
            state.panStartViewX = state.viewBox.x;
            state.panStartViewY = state.viewBox.y;
            svg.style.cursor = 'grabbing';
        }
    });

    window.addEventListener('mousemove', (e) => {
        if (!state.isPanning) return;
        const dx = e.clientX - state.panStartX;
        const dy = e.clientY - state.panStartY;
        const scale = state.viewBox.w / svg.clientWidth;
        state.viewBox.x = state.panStartViewX - dx * scale;
        state.viewBox.y = state.panStartViewY - dy * scale;
        updateViewBox();
    });

    window.addEventListener('mouseup', () => {
        if (state.isPanning) {
            state.isPanning = false;
            svg.style.cursor = 'grab';
        }
    });

    // Scroll wheel zoom
    svg.addEventListener('wheel', (e) => {
        e.preventDefault();
        const zoomFactor = e.deltaY > 0 ? 1.1 : 0.9;
        const rect = svg.getBoundingClientRect();
        const mx = (e.clientX - rect.left) / rect.width;
        const my = (e.clientY - rect.top) / rect.height;

        const vb = state.viewBox;
        const newW = Math.max(400, Math.min(10000, vb.w * zoomFactor));
        const newH = Math.max(350, Math.min(8750, vb.h * zoomFactor));

        // Zoom toward cursor
        vb.x += (vb.w - newW) * mx;
        vb.y += (vb.h - newH) * my;
        vb.w = newW;
        vb.h = newH;
        updateViewBox();
    }, { passive: false });

    // Touch pan/pinch
    let touches = [];
    let lastPinchDist = 0;

    svg.addEventListener('touchstart', (e) => {
        touches = [...e.touches];
        if (touches.length === 1) {
            state.isPanning = true;
            state.panStartX = touches[0].clientX;
            state.panStartY = touches[0].clientY;
            state.panStartViewX = state.viewBox.x;
            state.panStartViewY = state.viewBox.y;
        } else if (touches.length === 2) {
            lastPinchDist = Math.hypot(
                touches[1].clientX - touches[0].clientX,
                touches[1].clientY - touches[0].clientY
            );
        }
    }, { passive: true });

    svg.addEventListener('touchmove', (e) => {
        e.preventDefault();
        const ts = [...e.touches];
        if (ts.length === 1 && state.isPanning) {
            const dx = ts[0].clientX - state.panStartX;
            const dy = ts[0].clientY - state.panStartY;
            const scale = state.viewBox.w / svg.clientWidth;
            state.viewBox.x = state.panStartViewX - dx * scale;
            state.viewBox.y = state.panStartViewY - dy * scale;
            updateViewBox();
        } else if (ts.length === 2) {
            const dist = Math.hypot(
                ts[1].clientX - ts[0].clientX,
                ts[1].clientY - ts[0].clientY
            );
            if (lastPinchDist > 0) {
                const factor = lastPinchDist / dist;
                const vb = state.viewBox;
                const newW = Math.max(400, Math.min(10000, vb.w * factor));
                const newH = Math.max(350, Math.min(8750, vb.h * factor));
                vb.x += (vb.w - newW) * 0.5;
                vb.y += (vb.h - newH) * 0.5;
                vb.w = newW;
                vb.h = newH;
                updateViewBox();
            }
            lastPinchDist = dist;
        }
    }, { passive: false });

    svg.addEventListener('touchend', () => {
        state.isPanning = false;
        lastPinchDist = 0;
    }, { passive: true });

    // Background click = deselect
    svg.addEventListener('click', (e) => {
        if (e.target === svg) {
            if (window._onMapBgClick) {
                window._onMapBgClick();
            }
        }
    });
}


// ============================================================
//  Toolbar controls
// ============================================================

function zoomIn() {
    const vb = state.viewBox;
    const newW = Math.max(400, vb.w * 0.8);
    const newH = Math.max(350, vb.h * 0.8);
    vb.x += (vb.w - newW) * 0.5;
    vb.y += (vb.h - newH) * 0.5;
    vb.w = newW;
    vb.h = newH;
    updateViewBox();
}

function zoomOut() {
    const vb = state.viewBox;
    const newW = Math.min(10000, vb.w * 1.25);
    const newH = Math.min(8750, vb.h * 1.25);
    vb.x += (vb.w - newW) * 0.5;
    vb.y += (vb.h - newH) * 0.5;
    vb.w = newW;
    vb.h = newH;
    updateViewBox();
}

function resetView() {
    if (egoMode) {
        state.viewBox = { x: -500, y: -500, w: 1000, h: 1000 };
    } else {
        state.viewBox = { x: -800, y: -700, w: 1600, h: 1400 };
    }
    updateViewBox();
}

function toggleConnections() {
    state.showConnections = !state.showConnections;
    if (layerEdges) {
        layerEdges.style.display = state.showConnections ? '' : 'none';
    }
    return state.showConnections;
}


// ============================================================
//  Init
// ============================================================

function initMap() {
    svg = document.getElementById('map-svg');
    if (!svg) return;
    svg.style.cursor = 'grab';
    initPanZoom();
}

// initMap() is called explicitly from app.js before any rendering
