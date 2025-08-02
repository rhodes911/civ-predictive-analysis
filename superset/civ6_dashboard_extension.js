/**
 * Civ VI Data Refresh Button - Custom Dashboard Extension
 * 
 * This module adds a custom refresh button to Superset dashboards
 * that triggers Civ VI data loading via Docker.
 */

(function() {
    'use strict';
    
    // Configuration
    const CIV6_CONFIG = {
        refreshEndpoint: '/civ6/refresh-data',
        statusEndpoint: '/civ6/status',
        buttonId: 'civ6-refresh-btn',
        statusId: 'civ6-status-display'
    };
    
    // Create the refresh button HTML
    function createRefreshButton() {
        return `
            <div id="${CIV6_CONFIG.buttonId}-container" style="display: inline-flex; align-items: center; margin-left: 12px;">
                <button 
                    id="${CIV6_CONFIG.buttonId}" 
                    class="btn btn-primary btn-sm"
                    style="
                        background: linear-gradient(135deg, #ff6b6b, #ee5a52);
                        border: none;
                        border-radius: 6px;
                        padding: 8px 16px;
                        color: white;
                        font-weight: 500;
                        font-size: 13px;
                        cursor: pointer;
                        transition: all 0.3s ease;
                        display: flex;
                        align-items: center;
                        gap: 6px;
                    "
                    title="Load new Civ VI turn data"
                >
                    <span style="font-size: 14px;">🏆</span>
                    <span>Load New Turns</span>
                </button>
                <div id="${CIV6_CONFIG.statusId}" style="margin-left: 8px; font-size: 12px; color: #666;"></div>
            </div>
        `;
    }
    
    // Add hover effects via CSS
    function addButtonStyles() {
        const style = document.createElement('style');
        style.textContent = `
            #${CIV6_CONFIG.buttonId}:hover {
                transform: translateY(-1px);
                box-shadow: 0 4px 12px rgba(255, 107, 107, 0.3);
                background: linear-gradient(135deg, #ee5a52, #dc3545) !important;
            }
            
            #${CIV6_CONFIG.buttonId}:active {
                transform: translateY(0);
            }
            
            #${CIV6_CONFIG.buttonId}.loading {
                background: linear-gradient(135deg, #6c757d, #5a6268) !important;
                cursor: not-allowed;
            }
            
            #${CIV6_CONFIG.buttonId}.loading span:first-child {
                animation: spin 1s linear infinite;
            }
            
            @keyframes spin {
                from { transform: rotate(0deg); }
                to { transform: rotate(360deg); }
            }
            
            .civ6-toast {
                position: fixed;
                top: 80px;
                right: 20px;
                background: white;
                border-radius: 8px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.15);
                padding: 16px 20px;
                z-index: 9999;
                max-width: 400px;
                border-left: 4px solid #28a745;
                animation: slideIn 0.3s ease-out;
            }
            
            .civ6-toast.error {
                border-left-color: #dc3545;
            }
            
            @keyframes slideIn {
                from {
                    transform: translateX(100%);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
        `;
        document.head.appendChild(style);
    }
    
    // Show toast notification
    function showToast(message, type = 'success') {
        const toast = document.createElement('div');
        toast.className = `civ6-toast ${type}`;
        toast.innerHTML = `
            <div style="font-weight: 600; margin-bottom: 4px;">
                ${type === 'success' ? '✅ Success!' : '❌ Error'}
            </div>
            <div style="color: #666; font-size: 14px;">${message}</div>
        `;
        
        document.body.appendChild(toast);
        
        // Auto-remove after 5 seconds
        setTimeout(() => {
            if (toast.parentNode) {
                toast.style.animation = 'slideIn 0.3s ease-out reverse';
                setTimeout(() => {
                    toast.remove();
                }, 300);
            }
        }, 5000);
    }
    
    // Update status display
    function updateStatus(data) {
        const statusEl = document.getElementById(CIV6_CONFIG.statusId);
        if (statusEl && data) {
            statusEl.innerHTML = `
                <span style="color: #28a745; font-weight: 500;">
                    Turn ${data.latest_turn || 0} • ${data.total_records || 0} records
                </span>
            `;
        }
    }
    
    // Fetch current status
    async function fetchStatus() {
        try {
            const response = await fetch(CIV6_CONFIG.statusEndpoint);
            const data = await response.json();
            
            if (data.success) {
                updateStatus(data.status);
            }
        } catch (error) {
            console.warn('Could not fetch Civ VI status:', error);
        }
    }
    
    // Handle refresh button click
    async function handleRefresh() {
        const button = document.getElementById(CIV6_CONFIG.buttonId);
        if (!button || button.classList.contains('loading')) return;
        
        // Set loading state
        button.classList.add('loading');
        button.querySelector('span:last-child').textContent = 'Loading...';
        button.disabled = true;
        
        try {
            const response = await fetch(CIV6_CONFIG.refreshEndpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
            });
            
            const data = await response.json();
            
            if (data.success) {
                showToast(`Data refresh completed! Latest turn: ${data.data?.latest_turn || 'Unknown'}`, 'success');
                updateStatus(data.data);
                
                // Trigger dashboard refresh after a short delay
                setTimeout(() => {
                    if (window.location.reload) {
                        window.location.reload();
                    }
                }, 2000);
            } else {
                showToast(data.error || 'Refresh failed', 'error');
            }
        } catch (error) {
            showToast(`Network error: ${error.message}`, 'error');
        } finally {
            // Reset button state
            button.classList.remove('loading');
            button.querySelector('span:last-child').textContent = 'Load New Turns';
            button.disabled = false;
        }
    }
    
    // Insert the button into the dashboard header
    function insertRefreshButton() {
        // Look for various possible header locations in Superset
        const headerSelectors = [
            '.dashboard-header .header-right',
            '.dashboard-header .right-side',
            '.dashboard-content .header-controls',
            '.dashboard-title-panel .right',
            '[data-test="dashboard-header"] .right-side',
            '.header-container .action-buttons'
        ];
        
        let headerElement = null;
        for (const selector of headerSelectors) {
            headerElement = document.querySelector(selector);
            if (headerElement) break;
        }
        
        // Fallback: look for any header-like element
        if (!headerElement) {
            headerElement = document.querySelector('.dashboard-header, .header-container, [class*="header"]');
        }
        
        if (headerElement && !document.getElementById(CIV6_CONFIG.buttonId)) {
            headerElement.insertAdjacentHTML('beforeend', createRefreshButton());
            
            // Add event listener
            const button = document.getElementById(CIV6_CONFIG.buttonId);
            if (button) {
                button.addEventListener('click', handleRefresh);
                console.log('✅ Civ VI refresh button added successfully!');
                
                // Fetch initial status
                fetchStatus();
                return true;
            }
        }
        
        return false;
    }
    
    // Initialize the extension
    function initCiv6Extension() {
        // Add styles
        addButtonStyles();
        
        // Try to insert button immediately
        if (insertRefreshButton()) {
            return;
        }
        
        // If immediate insertion failed, use MutationObserver to wait for dashboard to load
        const observer = new MutationObserver((mutations) => {
            for (const mutation of mutations) {
                if (mutation.type === 'childList') {
                    if (insertRefreshButton()) {
                        observer.disconnect();
                        return;
                    }
                }
            }
        });
        
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
        
        // Timeout after 10 seconds
        setTimeout(() => {
            observer.disconnect();
            console.warn('⚠️ Could not find suitable location for Civ VI refresh button');
        }, 10000);
    }
    
    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initCiv6Extension);
    } else {
        initCiv6Extension();
    }
    
    // Also try after a short delay to catch dynamically loaded content
    setTimeout(initCiv6Extension, 2000);
    
})();
