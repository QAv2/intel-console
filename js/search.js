/**
 * Intel Console — Search + filter UI
 */

const Search = {
    input: null,
    results: null,
    debounceTimer: null,

    init() {
        this.input = document.getElementById('search-input');
        this.results = document.getElementById('search-results');

        this.input.addEventListener('input', () => {
            clearTimeout(this.debounceTimer);
            this.debounceTimer = setTimeout(() => this.doSearch(), 200);
        });

        this.input.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.input.value = '';
                this.results.classList.remove('visible');
                this.input.blur();
            }
        });

        // Close search results on outside click
        document.addEventListener('click', (e) => {
            if (!this.input.contains(e.target) && !this.results.contains(e.target)) {
                this.results.classList.remove('visible');
            }
        });
    },

    async doSearch() {
        const q = this.input.value.trim();
        if (q.length < 1) {
            this.results.classList.remove('visible');
            return;
        }

        try {
            const entities = await API.searchEntities(q);
            if (entities.length === 0) {
                this.results.innerHTML = '<div class="search-result-item" style="color:rgba(255,255,255,0.35)">No results</div>';
                this.results.classList.add('visible');
                return;
            }

            this.results.innerHTML = entities.map(e => {
                const color = TYPE_COLORS[e.entity_type] || '#888';
                return `<div class="search-result-item" data-id="${e.id}">
                    <span class="search-result-dot" style="background:${color}"></span>
                    <span>${esc(e.name)}</span>
                    <span class="search-result-type">${e.entity_type.replace('_', ' ')}</span>
                </div>`;
            }).join('');

            this.results.classList.add('visible');

            this.results.querySelectorAll('.search-result-item[data-id]').forEach(el => {
                el.addEventListener('click', () => {
                    const id = parseInt(el.getAttribute('data-id'));
                    if (egoMode) {
                        navStack.push(id);
                        recenterOn(id);
                        updateBreadcrumb();
                    } else {
                        focusNode(id);
                    }
                    Dossier.show(id);
                    this.results.classList.remove('visible');
                    this.input.value = '';
                });
            });
        } catch (err) {
            console.error('Search error:', err);
        }
    },
};


const Filters = {
    activeTiers: new Set(['documented', 'credible', 'inference', 'speculative']),
    activeTypes: new Set(),

    init(entityTypes) {
        this.activeTypes = new Set(entityTypes);

        // Tier toggles
        document.querySelectorAll('.tier-toggle').forEach(label => {
            const tier = label.getAttribute('data-tier');
            const checkbox = label.querySelector('input');
            label.addEventListener('click', (e) => {
                e.preventDefault();
                if (this.activeTiers.has(tier)) {
                    this.activeTiers.delete(tier);
                    label.classList.add('unchecked');
                    checkbox.checked = false;
                } else {
                    this.activeTiers.add(tier);
                    label.classList.remove('unchecked');
                    checkbox.checked = true;
                }
                filterByTier(this.activeTiers);
            });
        });

        // Type pills
        const container = document.getElementById('type-filters');
        container.innerHTML = '<span class="filter-label">TYPE</span>';
        entityTypes.forEach(type => {
            const color = TYPE_COLORS[type] || '#888';
            const pill = document.createElement('span');
            pill.className = 'type-pill active';
            pill.innerHTML = `<span class="pill-dot" style="background:${color}"></span>${type.replace('_', ' ')}`;
            pill.addEventListener('click', () => {
                if (this.activeTypes.has(type)) {
                    this.activeTypes.delete(type);
                    pill.classList.remove('active');
                } else {
                    this.activeTypes.add(type);
                    pill.classList.add('active');
                }
                filterByType(this.activeTypes);
            });
            container.appendChild(pill);
        });
    },
};
