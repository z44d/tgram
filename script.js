// tgram Documentation JavaScript - Optimized

// Theme toggle
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;
const themeIcon = document.querySelector('.theme-icon');

// Load saved theme
const savedTheme = localStorage.getItem('theme') || 'dark';
body.className = savedTheme;
updateThemeIcon();

themeToggle?.addEventListener('click', () => {
    const currentTheme = body.className;
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    body.className = newTheme;
    localStorage.setItem('theme', newTheme);
    updateThemeIcon();
});

function updateThemeIcon() {
    if (themeIcon) {
        const isDark = body.className === 'dark';
        themeIcon.innerHTML = isDark ? 
            `<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,18.5A6.5,6.5,0,1,1,18.5,12,6.51,6.51,0,0,1,12,18.5ZM12,7A5,5,0,1,0,17,12,5,5,0,0,0,12,7Z"/>
                <path d="M12,1a1,1,0,0,0-1,1V4a1,1,0,0,0,2,0V2A1,1,0,0,0,12,1Z"/>
                <path d="M12,20a1,1,0,0,0-1,1v2a1,1,0,0,0,2,0V21A1,1,0,0,0,12,20Z"/>
                <path d="M4.22,4.22a1,1,0,0,0-1.41,1.41L4.22,7.05A1,1,0,1,0,5.64,5.64Z"/>
                <path d="M18.36,18.36a1,1,0,0,0-1.41,1.41l1.42,1.42a1,1,0,0,0,1.41-1.41Z"/>
                <path d="M1,13H4a1,1,0,0,0,0-2H1a1,1,0,0,0,0,2Z"/>
                <path d="M20,13h3a1,1,0,0,0,0-2H20a1,1,0,0,0,0,2Z"/>
                <path d="M4.22,19.78a1,1,0,0,0,1.41,0l1.42-1.42a1,1,0,0,0-1.41-1.41L4.22,18.36A1,1,0,0,0,4.22,19.78Z"/>
                <path d="M18.36,5.64a1,1,0,0,0,1.41,0l1.42-1.42a1,1,0,0,0-1.41-1.41L18.36,4.22A1,1,0,0,0,18.36,5.64Z"/>
            </svg>` :
            `<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M21.64,13a1,1,0,0,0-1.05-.14,8.05,8.05,0,0,1-3.37.73A8.15,8.15,0,0,1,9.08,5.49a8.59,8.59,0,0,1,.25-2A1,1,0,0,0,8,2.36,10.14,10.14,0,1,0,22,14.05,1,1,0,0,0,21.64,13Zm-9.5,6.69A8.14,8.14,0,0,1,7.08,5.22v.27A10.15,10.15,0,0,0,17.22,15.63a9.79,9.79,0,0,0,2.1-.22A8.11,8.11,0,0,1,12.14,19.73Z"/>
            </svg>`;
    }
}

// Optimized search functionality
const searchInput = document.getElementById('search');
const searchResults = document.getElementById('search-results');

// Debounce search for better performance
let searchTimeout;
const SEARCH_DELAY = 300;

if (searchInput && searchResults) {
    searchInput.addEventListener('input', (e) => {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            const query = e.target.value.toLowerCase().trim();
            
            if (query.length < 1) {
                searchResults.style.display = 'none';
                return;
            }
            
            performSearch(query);
        }, SEARCH_DELAY);
    });

    searchInput.addEventListener('blur', () => {
        setTimeout(() => {
            searchResults.style.display = 'none';
        }, 200);
    });
}

function performSearch(query) {
    const results = [];
    const maxResults = 8; // Limit for performance
    
    // Get current page path to determine correct URLs
    const currentPath = window.location.pathname;
    const isInSubdir = currentPath.includes('/methods/') || currentPath.includes('/types/');
    const prefix = isInSubdir ? '../' : '';
    
    // First, check for exact type matches (highest priority)
    const exactTypeMatches = [];
    if (window.tgramTypes) {
        Object.entries(window.tgramTypes).forEach(([name, data]) => {
            if (name.toLowerCase() === query) {
                exactTypeMatches.push({
                    type: 'type',
                    name: name,
                    description: data.description,
                    url: `${prefix}types/${name}.html`,
                    priority: 100
                });
            }
        });
    }
    
    // Search types (high priority)
    const typeResults = [];
    if (window.tgramTypes) {
        Object.entries(window.tgramTypes).forEach(([name, data]) => {
            if (name.toLowerCase() === query) return; // Skip exact matches (already added)
            
            let priority = 0;
            if (name.toLowerCase().startsWith(query)) priority = 80;
            else if (name.toLowerCase().includes(query)) priority = 60;
            else if (data.description.toLowerCase().includes(query)) priority = 40;
            
            if (priority > 0) {
                typeResults.push({
                    type: 'type',
                    name: name,
                    description: data.description,
                    url: `${prefix}types/${name}.html`,
                    priority: priority
                });
            }
        });
    }
    
    // Search methods (lower priority)
    const methodResults = [];
    if (window.tgramMethods) {
        Object.entries(window.tgramMethods).forEach(([name, data]) => {
            let priority = 0;
            if (name.toLowerCase() === query) priority = 70; // Lower than type exact match
            else if (name.toLowerCase().startsWith(query)) priority = 50;
            else if (name.toLowerCase().includes(query)) priority = 30;
            else if (data.description.toLowerCase().includes(query)) priority = 10;
            
            if (priority > 0) {
                methodResults.push({
                    type: 'method',
                    name: name,
                    description: data.description,
                    url: `${prefix}methods/${name}.html`,
                    priority: priority
                });
            }
        });
    }
    
    // Combine and sort all results by priority
    const allResults = [...exactTypeMatches, ...typeResults, ...methodResults]
        .sort((a, b) => b.priority - a.priority)
        .slice(0, maxResults);
    
    displaySearchResults(allResults);
}

function displaySearchResults(results) {
    if (!searchResults) return;
    
    if (results.length === 0) {
        searchResults.style.display = 'none';
        return;
    }
    
    const html = results.map(result => `
        <div class="search-result" onclick="window.location.href='${result.url}'">
            <div style="font-weight: 600; color: var(--text-primary);">
                ${result.name}
                <span class="badge badge-${result.type === 'method' ? 'blue' : 'purple'}" style="margin-left: 8px; font-size: 10px;">
                    ${result.type}
                </span>
            </div>
            <div style="font-size: 12px; color: var(--text-secondary); margin-top: 2px;">
                ${result.description.substring(0, 60)}${result.description.length > 60 ? '...' : ''}
            </div>
        </div>
    `).join('');
    
    searchResults.innerHTML = html;
    searchResults.style.display = 'block';
}

// Initialize Prism.js when available
document.addEventListener('DOMContentLoaded', () => {
    if (typeof Prism !== 'undefined') {
        Prism.highlightAll();
    }
});

// Collapsible sidebar functionality
document.addEventListener('DOMContentLoaded', () => {
    // Initialize collapsible sections
    const collapsibleButtons = document.querySelectorAll('.collapsible');
    
    collapsibleButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = button.getAttribute('data-target');
            const targetContent = document.getElementById(targetId);
            const collapseIcon = button.querySelector('.collapse-icon');
            
            if (targetContent) {
                const isExpanded = targetContent.style.display !== 'none';
                targetContent.style.display = isExpanded ? 'none' : 'block';
                
                // Rotate collapse icon
                if (collapseIcon) {
                    collapseIcon.style.transform = isExpanded ? 'rotate(-90deg)' : 'rotate(0deg)';
                }
                
                // Save state to localStorage
                localStorage.setItem(`sidebar-${targetId}`, isExpanded ? 'collapsed' : 'expanded');
            }
        });
        
        // Restore saved state
        const targetId = button.getAttribute('data-target');
        const savedState = localStorage.getItem(`sidebar-${targetId}`);
        const targetContent = document.getElementById(targetId);
        const collapseIcon = button.querySelector('.collapse-icon');
        
        if (savedState === 'collapsed' && targetContent) {
            targetContent.style.display = 'none';
            if (collapseIcon) {
                collapseIcon.style.transform = 'rotate(-90deg)';
            }
        }
    });
    
    // Search page functionality
    const searchPageInput = document.getElementById('search-page-input');
    const searchPageBtn = document.getElementById('search-page-btn');
    const searchPageResults = document.getElementById('search-page-results');
    
    // Handle URL query parameter for search page
    if (searchPageInput && window.location.pathname.includes('search.html')) {
        const urlParams = new URLSearchParams(window.location.search);
        const queryParam = urlParams.get('q');
        if (queryParam) {
            searchPageInput.value = queryParam;
            // Trigger search after ensuring data is loaded
            const triggerSearch = () => {
                if (window.tgramMethods && window.tgramTypes) {
                    performAdvancedSearch();
                } else {
                    // Retry after a short delay if data not loaded yet
                    setTimeout(triggerSearch, 50);
                }
            };
            setTimeout(triggerSearch, 100);
        }
    }
    
    if (searchPageInput && searchPageResults) {
        const performAdvancedSearch = () => {
            const query = searchPageInput.value.toLowerCase().trim();
            
            if (query.length < 1) {
                searchPageResults.innerHTML = `
                    <div class="search-placeholder">
                        <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor" opacity="0.3">
                            <path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
                        </svg>
                        <h3>Start typing to search</h3>
                        <p>Search through methods, types, and descriptions</p>
                    </div>
                `;
                return;
            }
            
            const results = [];
            
            // Search methods
            if (window.tgramMethods) {
                Object.entries(window.tgramMethods).forEach(([name, data]) => {
                    const score = calculateSearchScore(query, name, data.description, data.parameters || {});
                    if (score > 0) {
                        results.push({
                            type: 'method',
                            name: name,
                            description: data.description,
                            parameters: data.parameters || {},
                            url: `methods/${name}.html`,
                            score: score
                        });
                    }
                });
            }
            
            // Search types
            if (window.tgramTypes) {
                Object.entries(window.tgramTypes).forEach(([name, data]) => {
                    const score = calculateSearchScore(query, name, data.description, data.fields || {});
                    if (score > 0) {
                        results.push({
                            type: 'type',
                            name: name,
                            description: data.description,
                            fields: data.fields || {},
                            url: `types/${name}.html`,
                            score: score
                        });
                    }
                });
            }
            
            // Sort by score (highest first)
            results.sort((a, b) => b.score - a.score);
            
            displayAdvancedSearchResults(results);
        };
        
        searchPageInput.addEventListener('input', performAdvancedSearch);
        searchPageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                performAdvancedSearch();
            }
        });
        
        if (searchPageBtn) {
            searchPageBtn.addEventListener('click', performAdvancedSearch);
        }
    }
    
    // Enhanced header search with Enter key support
    if (searchInput) {
        searchInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                const query = searchInput.value.trim();
                if (query) {
                    // Navigate to search page with query
                    const currentPath = window.location.pathname;
                    const isInSubdir = currentPath.includes('/methods/') || currentPath.includes('/types/');
                    const searchUrl = isInSubdir ? '../search.html' : 'search.html';
                    window.location.href = `${searchUrl}?q=${encodeURIComponent(query)}`;
                }
            }
        });
    }
});

function calculateSearchScore(query, name, description, fields) {
    let score = 0;
    const queryLower = query.toLowerCase();
    const nameLower = name.toLowerCase();
    const descLower = description.toLowerCase();
    
    // Exact name match gets highest score
    if (nameLower === queryLower) score += 100;
    // Name starts with query
    else if (nameLower.startsWith(queryLower)) score += 50;
    // Name contains query
    else if (nameLower.includes(queryLower)) score += 25;
    
    // Description contains query
    if (descLower.includes(queryLower)) score += 10;
    
    // Search in fields/parameters
    Object.entries(fields).forEach(([fieldName, fieldData]) => {
        if (fieldName.toLowerCase().includes(queryLower)) score += 5;
        if (typeof fieldData === 'object' && fieldData.description && 
            fieldData.description.toLowerCase().includes(queryLower)) score += 3;
    });
    
    return score;
}

function displayAdvancedSearchResults(results) {
    const searchPageResults = document.getElementById('search-page-results');
    if (!searchPageResults) return;
    
    if (results.length === 0) {
        searchPageResults.innerHTML = `
            <div class="no-results">
                <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor" opacity="0.3">
                    <path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
                </svg>
                <h3>No results found</h3>
                <p>Try different keywords or check your spelling</p>
            </div>
        `;
        return;
    }
    
    const html = `
        <div class="search-results-header">
            <h3>Found ${results.length} result${results.length !== 1 ? 's' : ''}</h3>
        </div>
        <div class="search-results-list">
            ${results.map(result => `
                <div class="search-result-card" onclick="window.location.href='${result.url}'">
                    <div class="result-header">
                        <h4>${result.name}</h4>
                        <span class="badge badge-${result.type === 'method' ? 'blue' : 'purple'}">
                            ${result.type}
                        </span>
                    </div>
                    <p class="result-description">${result.description}</p>
                    ${result.type === 'method' && Object.keys(result.parameters).length > 0 ? 
                        `<div class="result-params">
                            <strong>Parameters:</strong> ${Object.keys(result.parameters).slice(0, 3).join(', ')}
                            ${Object.keys(result.parameters).length > 3 ? '...' : ''}
                        </div>` : ''}
                    ${result.type === 'type' && Object.keys(result.fields).length > 0 ? 
                        `<div class="result-fields">
                            <strong>Fields:</strong> ${Object.keys(result.fields).slice(0, 3).join(', ')}
                            ${Object.keys(result.fields).length > 3 ? '...' : ''}
                        </div>` : ''}
                </div>
            `).join('')}
        </div>
    `;
    
    searchPageResults.innerHTML = html;
}

// Optimize sidebar for mobile
const sidebar = document.querySelector('.sidebar');
if (sidebar && window.innerWidth <= 768) {
    sidebar.style.transform = 'translateX(-100%)';
}
