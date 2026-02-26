/**
 * Intel Console — Entity dossier panel
 *
 * Features:
 *   - Photo + name header (64px photo or initial placeholder)
 *   - Metadata display (birth/death dates, nationality, status badge)
 *   - Full description with pre-wrap paragraph rendering
 *   - Entity-level source citations (from entity_sources table)
 *   - Relationships grouped by type with evidence tier coloring
 *   - Relationship clicks → recenterOn() with navStack integration
 */

const Dossier = {
    panel: null,
    inner: null,
    closeBtn: null,
    currentEntityId: null,

    init() {
        this.panel = document.getElementById('dossier-panel');
        this.inner = document.getElementById('panel-inner');
        this.closeBtn = document.getElementById('panel-close');
        this.closeBtn.addEventListener('click', () => this.close());
    },

    close() {
        this.panel.classList.remove('open');
        this.currentEntityId = null;
        clearHighlight();
    },

    async show(entityId) {
        this.currentEntityId = entityId;
        highlightNode(entityId);

        const [entity, relationships, entitySources] = await Promise.all([
            API.getEntity(entityId),
            API.getRelationships(entityId),
            API.getEntitySources(entityId),
        ]);

        const meta = entity.metadata || {};
        const color = TYPE_COLORS[entity.entity_type] || '#888';

        // Group relationships by type
        const grouped = {};
        relationships.forEach(r => {
            const key = r.relationship_type;
            if (!grouped[key]) grouped[key] = [];
            grouped[key].push(r);
        });

        let html = '';

        // ---- Photo header ----
        if (meta.photo_url) {
            html += `<div class="panel-photo-header">`;
            html += `<img class="panel-photo" src="${esc(meta.photo_url)}" alt="${esc(entity.name)}" style="border-color:${color}">`;
            html += `<div>`;
            html += `<div class="panel-type-tag" style="background:${color}22;color:${color}">${entity.entity_type.replace('_', ' ')}</div>`;
            html += `<h2 class="panel-title">${esc(entity.name)}</h2>`;
            if (entity.aliases) {
                html += `<p class="panel-aliases">aka ${esc(entity.aliases)}</p>`;
            }
            html += `</div></div>`;
        } else {
            // No photo — show initial placeholder
            const initial = entity.name.charAt(0).toUpperCase();
            html += `<div class="panel-photo-header">`;
            html += `<div class="panel-photo-placeholder" style="border-color:${color};color:${color}">${initial}</div>`;
            html += `<div>`;
            html += `<div class="panel-type-tag" style="background:${color}22;color:${color}">${entity.entity_type.replace('_', ' ')}</div>`;
            html += `<h2 class="panel-title">${esc(entity.name)}</h2>`;
            if (entity.aliases) {
                html += `<p class="panel-aliases">aka ${esc(entity.aliases)}</p>`;
            }
            html += `</div></div>`;
        }

        // ---- Metadata badges ----
        const badges = [];
        if (meta.status) {
            const statusColors = {
                alive: '#34d399',
                deceased: '#94a3b8',
                incarcerated: '#f87171',
                unknown: '#fbbf24',
            };
            const sc = statusColors[meta.status] || '#888';
            badges.push(`<span class="meta-badge" style="border-color:${sc};color:${sc}">${meta.status}</span>`);
        }
        if (meta.nationality) {
            badges.push(`<span class="meta-badge">${esc(meta.nationality)}</span>`);
        }
        if (meta.birth_date) {
            let dateStr = meta.birth_date;
            if (meta.death_date) {
                dateStr += ` — ${meta.death_date}`;
            }
            badges.push(`<span class="meta-badge">${esc(dateStr)}</span>`);
        }
        if (badges.length > 0) {
            html += `<div class="meta-badges">${badges.join('')}</div>`;
        }

        // ---- Description ----
        if (entity.description) {
            html += `<div class="panel-description">${esc(entity.description)}</div>`;
        }

        // ---- Entity-level sources ----
        if (entitySources && entitySources.length > 0) {
            html += `<div class="panel-section-label">Sources (${entitySources.length})</div>`;
            html += `<div class="entity-sources">`;
            entitySources.forEach(s => {
                if (s.url) {
                    html += `<a class="entity-source-item" href="${esc(s.url)}" target="_blank">`;
                } else {
                    html += `<span class="entity-source-item">`;
                }
                html += `<span class="entity-source-title">${esc(s.title)}</span>`;
                const details = [];
                if (s.author) details.push(s.author);
                if (s.year) details.push(String(s.year));
                if (details.length) {
                    html += `<span class="entity-source-detail">${esc(details.join(', '))}</span>`;
                }
                html += s.url ? `</a>` : `</span>`;
            });
            html += `</div>`;
        }

        // ---- Relationships grouped ----
        if (relationships.length > 0) {
            html += `<div class="panel-section-label">Relationships (${relationships.length})</div>`;

            for (const [relType, rels] of Object.entries(grouped)) {
                html += `<div class="rel-group">`;
                html += `<div class="rel-group-title">${relType.replace(/_/g, ' ')}</div>`;

                rels.forEach(r => {
                    const otherName = r.source_id === entityId
                        ? this._getNodeName(r.target_id)
                        : this._getNodeName(r.source_id);
                    const otherId = r.source_id === entityId ? r.target_id : r.source_id;
                    const direction = r.source_id === entityId ? '\u2192' : '\u2190';

                    let sourcesHtml = '';
                    if (r.sources && r.sources.length) {
                        sourcesHtml = '<div class="rel-sources">';
                        sourcesHtml += r.sources.map(s =>
                            s.url
                                ? `<a class="rel-source-link" href="${esc(s.url)}" target="_blank">${esc(s.title)}</a>`
                                : esc(s.title)
                        ).join(' | ');
                        sourcesHtml += '</div>';
                    }

                    html += `<div class="rel-item" data-tier="${r.evidence_tier}" data-entity-id="${otherId}">
                        <div>
                            <div class="rel-entity-name">${direction} ${esc(otherName)}</div>
                            ${r.description ? `<div class="rel-desc">${esc(r.description)}</div>` : ''}
                            ${sourcesHtml}
                        </div>
                    </div>`;
                });

                html += `</div>`;
            }
        }

        this.inner.innerHTML = html;
        this.panel.classList.add('open');

        // Scroll to top on new entity
        this.panel.scrollTop = 0;

        // Click handlers on relationship items → recenterOn
        this.inner.querySelectorAll('.rel-item[data-entity-id]').forEach(el => {
            el.addEventListener('click', (evt) => {
                // Don't navigate if clicking a source link
                if (evt.target.closest('.rel-source-link')) return;

                const id = parseInt(el.getAttribute('data-entity-id'));
                if (id && egoMode) {
                    navStack.push(id);
                    recenterOn(id);
                    updateBreadcrumb();
                    this.show(id);
                } else if (id) {
                    focusNode(id);
                    this.show(id);
                }
            });
        });
    },

    _getNodeName(id) {
        if (!graphData) return `#${id}`;
        const node = graphData.nodes.find(n => n.id === id);
        return node ? node.name : `#${id}`;
    },
};

function esc(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}
