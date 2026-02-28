/**
 * Intel Console — Timeline Slider
 *
 * Dual-handle range slider with density histogram.
 * Filters edges by year_start / year_end.
 * Undated edges (no year) shown by default, toggleable.
 */

const Timeline = (() => {
    const YEAR_MIN = 1940;
    const YEAR_MAX = 2026;
    const DECADE_SNAP = false;

    let container = null;
    let trackEl = null;
    let histogramEl = null;
    let fillEl = null;
    let handleMin = null;
    let handleMax = null;
    let labelMin = null;
    let labelMax = null;
    let undatedToggle = null;
    let activeCountEl = null;
    let dragging = null; // 'min' | 'max' | null
    let currentMin = YEAR_MIN;
    let currentMax = YEAR_MAX;
    let showUndated = true;
    let yearCounts = {};
    let totalDated = 0;
    let totalUndated = 0;

    function init() {
        container = document.getElementById('timeline-container');
        if (!container) return;

        buildHistogramData();
        render();
        attachEvents();
    }

    function buildHistogramData() {
        if (!graphData) return;
        yearCounts = {};
        totalDated = 0;
        totalUndated = 0;

        graphData.edges.forEach(e => {
            const ys = e.year_start;
            const ye = e.year_end;
            if (ys == null && ye == null) {
                totalUndated++;
                return;
            }
            totalDated++;
            // Count each year in the span
            const start = ys || ye;
            const end = ye || ys;
            // For histogram, just count start year (or end if no start)
            const yr = start;
            yearCounts[yr] = (yearCounts[yr] || 0) + 1;
        });
    }

    function render() {
        if (!container) return;

        // Build histogram bars
        const decades = [];
        for (let y = YEAR_MIN; y <= YEAR_MAX; y += 5) {
            let count = 0;
            for (let i = 0; i < 5 && y + i <= YEAR_MAX; i++) {
                count += (yearCounts[y + i] || 0);
            }
            decades.push({ year: y, count });
        }
        const maxCount = Math.max(...decades.map(d => d.count), 1);

        let histBars = decades.map(d => {
            const pct = (d.count / maxCount) * 100;
            const left = yearToPercent(d.year);
            const width = yearToPercent(d.year + 5) - left;
            return `<div class="tl-hist-bar" style="left:${left}%;width:${width}%;height:${pct}%" title="${d.year}-${d.year + 4}: ${d.count} connections"></div>`;
        }).join('');

        container.innerHTML = `
            <div class="tl-header">
                <span class="tl-title">TIMELINE</span>
                <label class="tl-undated-toggle" title="Show connections without dates">
                    <input type="checkbox" ${showUndated ? 'checked' : ''}>
                    <span class="tl-undated-label">Undated <span class="tl-undated-count">(${totalUndated})</span></span>
                </label>
                <span class="tl-active-count" id="tl-active-count"></span>
            </div>
            <div class="tl-slider-wrap">
                <div class="tl-histogram">${histBars}</div>
                <div class="tl-track">
                    <div class="tl-fill"></div>
                    <div class="tl-handle tl-handle-min" data-handle="min">
                        <span class="tl-handle-label">${currentMin}</span>
                    </div>
                    <div class="tl-handle tl-handle-max" data-handle="max">
                        <span class="tl-handle-label">${currentMax}</span>
                    </div>
                </div>
                <div class="tl-ticks">
                    ${generateTicks()}
                </div>
            </div>
        `;

        // Cache refs
        trackEl = container.querySelector('.tl-track');
        histogramEl = container.querySelector('.tl-histogram');
        fillEl = container.querySelector('.tl-fill');
        handleMin = container.querySelector('.tl-handle-min');
        handleMax = container.querySelector('.tl-handle-max');
        labelMin = handleMin.querySelector('.tl-handle-label');
        labelMax = handleMax.querySelector('.tl-handle-label');
        undatedToggle = container.querySelector('.tl-undated-toggle input');
        activeCountEl = container.querySelector('#tl-active-count');

        positionHandles();
        updateActiveCount();
    }

    function generateTicks() {
        let html = '';
        for (let y = YEAR_MIN; y <= YEAR_MAX; y += 10) {
            const pct = yearToPercent(y);
            html += `<span class="tl-tick" style="left:${pct}%">${y}</span>`;
        }
        return html;
    }

    function yearToPercent(year) {
        return ((year - YEAR_MIN) / (YEAR_MAX - YEAR_MIN)) * 100;
    }

    function percentToYear(pct) {
        return Math.round(YEAR_MIN + (pct / 100) * (YEAR_MAX - YEAR_MIN));
    }

    function positionHandles() {
        if (!handleMin || !handleMax || !fillEl) return;
        const pMin = yearToPercent(currentMin);
        const pMax = yearToPercent(currentMax);
        handleMin.style.left = pMin + '%';
        handleMax.style.left = pMax + '%';
        fillEl.style.left = pMin + '%';
        fillEl.style.width = (pMax - pMin) + '%';
        labelMin.textContent = currentMin;
        labelMax.textContent = currentMax;

        // Dim histogram bars outside range
        container.querySelectorAll('.tl-hist-bar').forEach(bar => {
            const barLeft = parseFloat(bar.style.left);
            const barWidth = parseFloat(bar.style.width);
            const barRight = barLeft + barWidth;
            if (barRight < pMin || barLeft > pMax) {
                bar.classList.add('tl-hist-dim');
            } else {
                bar.classList.remove('tl-hist-dim');
            }
        });
    }

    function updateActiveCount() {
        if (!activeCountEl || !graphData) return;
        let visible = 0;
        graphData.edges.forEach(e => {
            const ys = e.year_start;
            const ye = e.year_end;
            if (ys == null && ye == null) {
                if (showUndated) visible++;
                return;
            }
            const start = ys || ye;
            const end = ye || ys;
            if (end >= currentMin && start <= currentMax) visible++;
        });
        const total = graphData.edges.length;
        activeCountEl.textContent = `${visible}/${total}`;
    }

    function applyFilter() {
        filterByYear(currentMin, currentMax, showUndated);
        updateActiveCount();
    }

    function attachEvents() {
        if (!container) return;

        // Handle drag
        container.addEventListener('mousedown', (e) => {
            const handle = e.target.closest('.tl-handle');
            if (handle) {
                dragging = handle.dataset.handle;
                e.preventDefault();
            }
        });

        window.addEventListener('mousemove', (e) => {
            if (!dragging || !trackEl) return;
            const rect = trackEl.getBoundingClientRect();
            let pct = ((e.clientX - rect.left) / rect.width) * 100;
            pct = Math.max(0, Math.min(100, pct));
            let year = percentToYear(pct);

            if (dragging === 'min') {
                year = Math.min(year, currentMax - 1);
                currentMin = year;
            } else {
                year = Math.max(year, currentMin + 1);
                currentMax = year;
            }
            positionHandles();
            applyFilter();
        });

        window.addEventListener('mouseup', () => {
            dragging = null;
        });

        // Touch support
        container.addEventListener('touchstart', (e) => {
            const handle = e.target.closest('.tl-handle');
            if (handle) {
                dragging = handle.dataset.handle;
            }
        }, { passive: true });

        window.addEventListener('touchmove', (e) => {
            if (!dragging || !trackEl) return;
            const touch = e.touches[0];
            const rect = trackEl.getBoundingClientRect();
            let pct = ((touch.clientX - rect.left) / rect.width) * 100;
            pct = Math.max(0, Math.min(100, pct));
            let year = percentToYear(pct);

            if (dragging === 'min') {
                year = Math.min(year, currentMax - 1);
                currentMin = year;
            } else {
                year = Math.max(year, currentMin + 1);
                currentMax = year;
            }
            positionHandles();
            applyFilter();
        }, { passive: true });

        window.addEventListener('touchend', () => {
            dragging = null;
        });

        // Track click (jump nearest handle)
        trackEl.addEventListener('click', (e) => {
            if (e.target.closest('.tl-handle')) return;
            const rect = trackEl.getBoundingClientRect();
            const pct = ((e.clientX - rect.left) / rect.width) * 100;
            const year = percentToYear(pct);
            const distMin = Math.abs(year - currentMin);
            const distMax = Math.abs(year - currentMax);
            if (distMin <= distMax) {
                currentMin = Math.min(year, currentMax - 1);
            } else {
                currentMax = Math.max(year, currentMin + 1);
            }
            positionHandles();
            applyFilter();
        });

        // Undated toggle
        undatedToggle.addEventListener('change', () => {
            showUndated = undatedToggle.checked;
            applyFilter();
        });
    }

    function reset() {
        currentMin = YEAR_MIN;
        currentMax = YEAR_MAX;
        showUndated = true;
        if (undatedToggle) undatedToggle.checked = true;
        positionHandles();
        applyFilter();
    }

    return { init, reset, buildHistogramData };
})();
