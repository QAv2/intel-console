/**
 * Intel Console — Branch Definitions (11 thematic branches)
 *
 * Entity-to-branch assignments are loaded from branch_assignments.json by api.js.
 * This file defines branch metadata only.
 */

const BRANCHES = {
    power:         { label: 'Power Architecture',       color: '#a63d40' },
    intelligence:  { label: 'Intelligence & Covert',    color: '#4a7c9b' },
    financial:     { label: 'Financial Control',        color: '#b8763a' },
    hidden_history:{ label: 'Hidden History',           color: '#c9842a' },
    consciousness: { label: 'Consciousness & Anomalous',color: '#7a5aa0' },
    exploitation:  { label: 'Exploitation Networks',    color: '#f87171' },
    narrative:     { label: 'Narrative Control',        color: '#4a8a8a' },
    health:        { label: 'Health & Bio',             color: '#5a8a6a' },
    resource:      { label: 'Resource Control',         color: '#34d399' },
    cosmology:     { label: 'Cosmology & Origins',      color: '#c9a84c' },
    elite_social:  { label: 'Elite Social Architecture',color: '#f472b6' },
};

// Entity-to-branch mapping loaded dynamically — see API.getBranchAssignments()
let ENTITY_BRANCH_MAP = {};
