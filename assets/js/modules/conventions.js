/**
 * @fileoverview Conventions module for handling multilingual badges and anchors in MkDocs
 * This module uses Material for MkDocs' document$ observable for content updates
 * and handles language changes in the documentation.
 * @requires document$ from Material for MkDocs
 * @requires dcatapesConfig global configuration object
 */

// Constants for styling and configuration
const RETRY_DELAY = 100;
const BADGE_COLORS = {
    must: '#eba58f',
    should: '#ebbb8f',
    may: '#8ecf7b'
};
const BADGE_OPACITY = 'aa'; // Hex for 0.66 opacity

// State management
let conventionIndex = 1;

/**
 * Creates an anchor element with the specified properties
 * @param {string} id - The ID to link to
 * @returns {HTMLElement} The created anchor element
 */
function createAnchor(id) {
    const anchor = document.createElement('a');
    anchor.className = 'headerlink';
    anchor.href = `#${id}`;
    anchor.title = 'Enlace permanente';
    anchor.textContent = '#';
    return anchor;
}

/**
 * Generates an ID for a note based on class and property data
 * @param {HTMLElement} table - The table element to extract data from
 * @returns {string|null} The generated ID or null if unable to generate
 */
function generateNoteId(table) {
    if (!table) return null;

    // Get the first row from thead instead of tbody
    const firstHeaderRow = table.querySelector('thead tr');
    if (!firstHeaderRow) return null;

    // Get class and property values from the first two cells
    const [classCell, propertyCell] = firstHeaderRow.querySelectorAll('th');
    if (!classCell || !propertyCell) return null;

    const classContent = classCell.textContent.trim();
    const propertyContent = propertyCell.textContent.trim();

    // Normalize the values for the ID
    const classId = normalizeForId(classContent);
    const propertyId = normalizeForId(propertyContent);

    return `nota-${classId}-${propertyId}`;
}

/**
 * Normalizes a string to be used as part of an ID
 * @param {string} value - The string to normalize
 * @returns {string} The normalized string
 */
function normalizeForId(value) {
    return value
        .toLowerCase()
        // Replace any non-alphanumeric character with a dash
        .replace(/[^a-z0-9]+/g, '_')
        // Remove dashes from start and end
        .replace(/^-+|-+$/g, '')
        // Handle empty strings
        || 'empty';
}

/**
 * Extracts property text from table
 * @param {HTMLElement} table - The table element
 * @returns {string} The extracted property text
 */
function extractPropertyText(table) {
    const propertyRow = Array.from(table.querySelectorAll('tr')).find(row => {
        const firstCell = row.querySelector('td');
        return firstCell?.textContent.trim() === 'Propiedad';
    });

    const strongElement = propertyRow?.querySelector('td:nth-child(2) strong');
    return strongElement?.textContent.trim().toLowerCase().replace(/[^a-z:]/g, '') || '';
}

/**
 * Creates title container with content and anchor
 * @param {HTMLElement} title - The title element
 * @param {string} id - The ID for the anchor
 * @returns {HTMLElement} The created title container
 */
function createTitleContainer(title, id) {
    const titleContainer = document.createElement('div');
    titleContainer.className = 'title-container';

    while (title.firstChild) {
        titleContainer.appendChild(title.firstChild);
    }

    titleContainer.appendChild(createAnchor(id));
    return titleContainer;
}

/**
 * Creates a secondary badge if applicable
 * @param {HTMLElement} admonition - The admonition element
 * @param {Object} badges - The badges configuration
 * @returns {HTMLElement|null} The created badge or null
 */
function createSecondaryBadge(admonition, badges) {
    const type = ['technical', 'semantic', 'organisational'].find(t => 
        admonition.classList.contains(t) && badges[t]
    );
    
    if (!type) return null;

    const badge = document.createElement('span');
    badge.className = 'secondary-badge';
    badge.textContent = badges[type].name;  // Access the name property
    badge.title = badges[type].title;       // Add tooltip from title property

    const primaryType = ['must', 'should', 'may'].find(t => admonition.classList.contains(t));
    if (primaryType) {
        badge.style.backgroundColor = `${BADGE_COLORS[primaryType]}${BADGE_OPACITY}`;
    }

    return badge;
}

function generateNoteIdFromTitle(titleText) {
    if (!titleText) return null;
    return 'nota-' + titleText
        .toLowerCase()
        .replace(/[áéíóúüñ]/g, c => ({ 
            'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u', 'ñ': 'n'
        })[c])
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/^-+|-+$/g, '')
        .substring(0, 50); // Limit length
}

/**
 * Main function to process admonitions
 */
function addAnchors() {
    if (!window.dcatapesConfig) {
        console.warn('dcatapesConfig not found, retrying in 100ms...');
        setTimeout(addAnchors, RETRY_DELAY);
        return;
    }

    const selectedLang = document.documentElement.lang || Object.keys(dcatapesConfig)[0];
    const badges = dcatapesConfig[selectedLang]?.buttons?.badges;
    
    if (!badges) {
        console.error('No badges configuration found');
        return;
    }
    
    document.querySelectorAll('div.admonition.must, div.admonition.should, div.admonition.may, div.admonition.note')
        .forEach(admonition => {
            if (admonition.id) return;

            const isNote = admonition.classList.contains('note');
            let id;

            if (isNote) {
                // First try to generate ID from previous sibling table
                id = generateNoteId(admonition.previousElementSibling);

                if (!id) {
                    // If no table ID, then check if it's a usage note
                    const titleElement = admonition.querySelector('.admonition-title');
                    const titleText = titleElement?.textContent?.trim();
                    const isUsageNote = titleText?.toLowerCase() === 'nota de uso' || 
                                      titleText?.toLowerCase() === 'usage note';

                    if (isUsageNote) {
                        id = `nota-${conventionIndex++}`;
                    } else {
                        // Try to generate ID from title
                        id = titleText ? generateNoteIdFromTitle(titleText) : null;
                        
                        // Last resort: use incremental ID
                        if (!id) {
                            id = `nota-${conventionIndex++}`;
                        }
                    }
                }
            } else {
                id = generateConventionId(admonition);
            }

            admonition.id = id;
            processTitle(admonition, id, badges);
        });
}
/**
 * Generates convention ID from admonition
 * @param {HTMLElement} admonition - The admonition element
 * @returns {string} The generated ID
 */
function generateConventionId(admonition) {
    const titleContainer = admonition.querySelector('.admonition-title .title-container');
    const titleText = titleContainer?.textContent || '';
    // Match any variation of Convention/Convencion/Convención
    const match = titleText.match(/(?:Conven(?:c|t)i[oó]n)\s+(\d+)/i);
    return match 
        ? `convencion-${match[1].padStart(2, '0')}`
        : `convencion-${conventionIndex++}`;
}

/**
 * Generates convention ID from admonition
 * @param {HTMLElement} admonition - The admonition element
 * @returns {string} The generated ID
 */
function generateConventionId(admonition) {
    const titleText = admonition.querySelector('.admonition-title')?.textContent || '';
    // Match any variation of Convention/Convencion/Convención
    const match = titleText.match(/(?:Conven(?:c|t)i[oó]n)\s+(\d+)/i);
    return match 
        ? `convencion-${match[1].padStart(2, '0')}`
        : `convencion-${conventionIndex++}`;
}

/**
 * Process title element of admonition
 * @param {HTMLElement} admonition - The admonition element
 * @param {string} id - The ID for the anchor
 * @param {Object} badges - The badges configuration
 */
function processTitle(admonition, id, badges) {
    const title = admonition.querySelector('.admonition-title');
    if (!title) return;

    title.appendChild(createTitleContainer(title, id));

    const primaryType = ['must', 'should', 'may'].find(t => admonition.classList.contains(t));
    if (primaryType) {
        title.setAttribute('data-badge', badges[primaryType].name);  // Access the name property
        title.setAttribute('data-badge-title', badges[primaryType].title); // Add tooltip from title property
        
        const secondaryBadge = createSecondaryBadge(admonition, badges);
        if (secondaryBadge) {
            title.appendChild(secondaryBadge);
        }
    }
}

/**
 * Updates badges and anchors when language changes
 */
function updateForLanguageChange() {
    // Reset convention index
    conventionIndex = 1;
    
    // Remove existing badges and anchors
    document.querySelectorAll('.secondary-badge, .headerlink').forEach(el => el.remove());
    
    // Remove existing data-badge attributes
    document.querySelectorAll('[data-badge]').forEach(el => {
        el.removeAttribute('data-badge');
        el.removeAttribute('data-badge-title');
    });
    
    // Re-add anchors and badges with new language
    addAnchors();
}


/**
 * Inicia la función al cargar el contenido de la página y observa cambios en el DOM.
 */
document.addEventListener("DOMContentLoaded", function() {
    addAnchors();

    // Configura un observador para detectar cambios en el DOM
    const observer = new MutationObserver(function() {
        addAnchors();
    });

    // Opciones de observación
    observer.observe(document.body, {
        childList: true,
        subtree: true,
    });
});