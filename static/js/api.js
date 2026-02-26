/**
 * Intel Console — Static data client (replaces fetch-based API)
 * Loads pre-exported JSON files and serves them from memory.
 */
const API = {
    _graph: null,
    _entities: null,
    _relationships: null,
    _sources: null,
    _stats: null,
    _centrality: null,
    _loaded: false,

    async _load() {
        if (this._loaded) return;
        const base = 'data/';
        const [graph, entities, relationships, sources, stats, centrality] = await Promise.all([
            fetch(base + 'graph.json').then(r => r.json()),
            fetch(base + 'entities.json').then(r => r.json()),
            fetch(base + 'relationships.json').then(r => r.json()),
            fetch(base + 'sources.json').then(r => r.json()),
            fetch(base + 'stats.json').then(r => r.json()),
            fetch(base + 'centrality.json').then(r => r.json()),
        ]);
        this._graph = graph;
        this._entities = entities;
        this._relationships = relationships;
        this._sources = sources;
        this._stats = stats;
        this._centrality = centrality;
        this._loaded = true;
    },

    _tierOrder: { documented: 0, credible: 1, inference: 2, speculative: 3 },

    async getGraphFull(minTier) {
        await this._load();
        const threshold = this._tierOrder[minTier] ?? 3;
        const edges = this._graph.edges.filter(e =>
            (this._tierOrder[e.evidence_tier] ?? 3) <= threshold
        );
        // Recount connections for filtered edges
        const counts = {};
        edges.forEach(e => {
            counts[e.source] = (counts[e.source] || 0) + 1;
            counts[e.target] = (counts[e.target] || 0) + 1;
        });
        const nodes = this._graph.nodes.map(n => ({
            ...n,
            connection_count: counts[n.id] || 0,
        }));
        return { nodes, edges };
    },

    async getEntity(id) {
        await this._load();
        const e = this._entities[id];
        if (!e) throw new Error(`Entity ${id} not found`);
        return e;
    },

    async getRelationships(entityId) {
        await this._load();
        return this._relationships[entityId] || [];
    },

    async getEntitySources(id) {
        await this._load();
        return this._sources[id] || [];
    },

    async searchEntities(q) {
        await this._load();
        const lower = q.toLowerCase();
        const results = [];
        for (const e of Object.values(this._entities)) {
            const haystack = (e.name + ' ' + e.aliases + ' ' + e.description).toLowerCase();
            if (haystack.includes(lower)) {
                results.push(e);
                if (results.length >= 20) break;
            }
        }
        return results;
    },

    async getStats() {
        await this._load();
        return this._stats;
    },

    async getNeighborhood(id, depth = 1) {
        await this._load();
        // BFS on graph edges
        const visited = new Set([id]);
        let frontier = [id];
        for (let d = 0; d < depth; d++) {
            const next = [];
            for (const nid of frontier) {
                for (const e of this._graph.edges) {
                    if (e.source === nid && !visited.has(e.target)) {
                        visited.add(e.target);
                        next.push(e.target);
                    }
                    if (e.target === nid && !visited.has(e.source)) {
                        visited.add(e.source);
                        next.push(e.source);
                    }
                }
            }
            frontier = next;
        }
        const nodeSet = visited;
        const nodes = this._graph.nodes.filter(n => nodeSet.has(n.id));
        const edges = this._graph.edges.filter(e =>
            nodeSet.has(e.source) && nodeSet.has(e.target)
        );
        return { nodes, edges };
    },

    async getCentrality(limit = 20) {
        await this._load();
        return this._centrality.slice(0, limit);
    },
};
