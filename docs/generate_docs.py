#!/usr/bin/env python3
"""
Generate static HTML documentation for tgram library
Optimized for GitHub Pages hosting
"""

import json
import shutil
from pathlib import Path
from datetime import datetime
import re


def load_json_data(json_path):
    """Load and validate JSON data"""
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if "methods" not in data or "types" not in data:
            print("❌ Error: JSON must contain 'methods' and 'types' keys")
            return None

        print(
            f"✅ Loaded {len(data['methods'])} methods and {len(data['types'])} types"
        )
        return data

    except FileNotFoundError:
        print(f"❌ Error: File not found: {json_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON: {e}")
        return None


def is_class_type(type_str):
    """Check if a type is a class type"""
    if not type_str:
        return False

    basic_types = ["str", "int", "bool", "float", "dict", "list"]
    clean_type = re.sub(
        r"Union\[.*?\]|List\[.*?\]|Optional\[.*?\]", "", type_str
    ).strip()
    type_names = re.findall(r"\b[A-Z][a-zA-Z0-9_]*\b", clean_type)
    return any(type_name.lower() not in basic_types for type_name in type_names)


def extract_class_name(type_str):
    """Extract class name from type string"""
    if not type_str:
        return "Class"

    match = re.search(r"\b[A-Z][a-zA-Z0-9_]*\b", type_str)
    return match.group(0) if match else "Class"


def generate_method_example(method_name, method_data):
    """Generate Python example for a method"""
    parameters = method_data.get("parameters", {})
    required_params = []

    for param_name, param_info in parameters.items():
        if param_info.get("required", False):
            param_type = param_info.get("type", "str")

            if "int" in param_type.lower():
                example_value = "123456789"
            elif "bool" in param_type.lower():
                example_value = "True"
            elif "str" in param_type.lower():
                example_value = f'"example_{param_name}"'
            elif "Union" in param_type:
                example_value = f"your_{param_name}"
            elif is_class_type(param_type):
                class_names = re.findall(r"\b[A-Z][a-zA-Z0-9_]*\b", param_type)
                class_name = class_names[0] if class_names else "Class"
                example_value = f"{class_name}(...)"
            else:
                example_value = f"your_{param_name}"

            required_params.append(f"{param_name}={example_value}")

    params_str = ",\n    ".join(required_params)
    if params_str:
        return f"await bot.{method_name}(\n    {params_str}\n)"
    else:
        return f"await bot.{method_name}()"


def create_base_template():
    """Create base HTML template"""
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - tgram Documentation</title>
    <link rel="stylesheet" href="{css_path}styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-core.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
    <link rel="icon" type="image/x-icon" href="{css_path}favicon.svg">
</head>
<body class="dark">
    <header class="header">
        <div class="header-content">
            <div class="header-left">
                <a href="{root_path}index.html" class="logo">
                    <div class="logo-icon">T</div>
                    <div class="logo-text">
                        <h1>tgram</h1>
                        <p>Telegram Bot API Library</p>
                    </div>
                </a>
            </div>
            <div class="header-right">
                <div class="search-container">
                    <input type="text" id="search" placeholder="Search methods and types..." class="search-input">
                    <div id="search-results" class="search-results"></div>
                </div>
                <button id="theme-toggle" class="theme-toggle" title="Toggle theme">
                    <span class="theme-icon">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M21.64,13a1,1,0,0,0-1.05-.14,8.05,8.05,0,0,1-3.37.73A8.15,8.15,0,0,1,9.08,5.49a8.59,8.59,0,0,1,.25-2A1,1,0,0,0,8,2.36,10.14,10.14,0,1,0,22,14.05,1,1,0,0,0,21.64,13Zm-9.5,6.69A8.14,8.14,0,0,1,7.08,5.22v.27A10.15,10.15,0,0,0,17.22,15.63a9.79,9.79,0,0,0,2.1-.22A8.11,8.11,0,0,1,12.14,19.73Z"/>
                        </svg>
                    </span>
                </button>
                <a href="https://github.com/z44d/tgram" target="_blank" class="github-link" title="GitHub">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                    </svg>
                </a>
            </div>
        </div>
    </header>

    <div class="layout">
        <aside class="sidebar">
            <nav class="sidebar-nav">
                {sidebar_content}
            </nav>
        </aside>

        <main class="main-content">
            {main_content}
        </main>
    </div>

    <script src="{css_path}search-data.js"></script>
    <script src="{css_path}script.js"></script>
</body>
</html>"""


def create_css():
    """Create optimized CSS styles"""
    return """/* tgram Documentation Styles - Optimized */
:root {
  --bg-primary: #0f172a;
  --bg-secondary: #1e293b;
  --bg-tertiary: #334155;
  --text-primary: #ffffff;
  --text-secondary: #cbd5e1;
  --text-muted: #64748b;
  --border-color: #475569;
  --accent-blue: #3b82f6;
  --accent-purple: #8b5cf6;
  --accent-red: #ef4444;
  --accent-green: #10b981;
}

.light {
  --bg-primary: #ffffff;
  --bg-secondary: #f8fafc;
  --bg-tertiary: #e2e8f0;
  --text-primary: #1e293b;
  --text-secondary: #475569;
  --text-muted: #64748b;
  --border-color: #cbd5e1;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background-color: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.6;
}

/* Header - Optimized */
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 64px;
  background-color: var(--bg-secondary);
  border-bottom: 1px solid var(--border-color);
  z-index: 1000;
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  padding: 0 24px;
}

.logo {
  display: flex;
  align-items: center;
  gap: 16px;
  text-decoration: none;
  color: var(--text-primary);
}

.logo-icon {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
  font-size: 18px;
}

.logo-text h1 {
  font-size: 20px;
  font-weight: bold;
  margin: 0;
}

.logo-text p {
  font-size: 14px;
  color: var(--text-muted);
  margin: 0;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 16px;
}

/* Search - Optimized */
.search-container {
  position: relative;
}

.search-input {
  width: 300px;
  padding: 8px 12px;
  background-color: var(--bg-tertiary);
  border: 1px solid var(--border-color);
  border-radius: 6px;
  color: var(--text-primary);
  font-size: 14px;
}

.search-results {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background-color: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 6px;
  max-height: 300px;
  overflow-y: auto;
  display: none;
  z-index: 1001;
}

.search-result {
  padding: 8px 12px;
  cursor: pointer;
  border-bottom: 1px solid var(--border-color);
}

.search-result:hover {
  background-color: var(--bg-tertiary);
}

.theme-toggle, .github-link {
  padding: 8px;
  background: none;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  border-radius: 4px;
  text-decoration: none;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Layout - Optimized */
.layout {
  display: flex;
  margin-top: 64px;
  min-height: calc(100vh - 64px);
}

.sidebar {
  width: 256px;
  background-color: var(--bg-secondary);
  border-right: 1px solid var(--border-color);
  position: fixed;
  height: calc(100vh - 64px);
  overflow-y: auto;
  padding: 16px;
}

.main-content {
  flex: 1;
  margin-left: 256px;
  padding: 32px;
  max-width: calc(100vw - 256px);
}

/* Sidebar - Optimized */
.sidebar-section {
  margin-bottom: 24px;
}

.sidebar-title {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px;
  background: none;
  border: none;
  color: var(--text-primary);
  font-weight: 600;
  cursor: pointer;
  width: 100%;
  text-align: left;
  border-radius: 4px;
}

.category-title {
  font-size: 12px;
  font-weight: 600;
  color: var(--accent-blue);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 8px;
  padding: 0 8px;
}

.sidebar-link {
  display: block;
  padding: 6px 8px;
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 14px;
  border-radius: 4px;
  margin-bottom: 2px;
}

.sidebar-link:hover {
  color: var(--text-primary);
  background-color: var(--bg-tertiary);
}

.sidebar-link.active {
  color: var(--text-primary);
  background-color: var(--accent-blue);
}

/* Content - Optimized */
.page-title {
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 16px;
}

.page-description {
  font-size: 18px;
  color: var(--text-secondary);
  margin-bottom: 24px;
}

.card {
  background-color: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 24px;
  margin-bottom: 24px;
}

.card-title {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 8px;
}

/* Badges - Optimized */
.badge {
  display: inline-flex;
  align-items: center;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
  text-decoration: none;
}

.badge-blue {
  background-color: rgba(59, 130, 246, 0.2);
  color: #93c5fd;
  border: 1px solid rgba(59, 130, 246, 0.3);
}

.badge-purple {
  background-color: rgba(139, 92, 246, 0.2);
  color: #c4b5fd;
  border: 1px solid rgba(139, 92, 246, 0.3);
}

.badge-red {
  background-color: rgba(239, 68, 68, 0.2);
  color: #fca5a5;
  border: 1px solid rgba(239, 68, 68, 0.3);
}

.badge-green {
  background-color: rgba(16, 185, 129, 0.2);
  color: #86efac;
  border: 1px solid rgba(16, 185, 129, 0.3);
}

/* Collapsible Sidebar Styles */
.collapsible {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 8px;
  background: none;
  border: none;
  color: var(--text-primary);
  font-weight: 600;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.2s;
}

.collapsible:hover {
  background-color: var(--bg-tertiary);
}

.sidebar-icon, .category-icon, .search-icon {
  display: flex;
  align-items: center;
  justify-content: center;
}

.collapse-icon {
  transition: transform 0.2s ease;
}

.collapsible-content {
  overflow: hidden;
  transition: max-height 0.3s ease;
}

.category-methods {
  margin-left: 16px;
}

.category-title {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding: 6px 8px;
  background: none;
  border: none;
  color: var(--accent-blue);
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  cursor: pointer;
  width: 100%;
  text-align: left;
  border-radius: 4px;
  margin-bottom: 4px;
}

.category-title:hover {
  background-color: rgba(59, 130, 246, 0.1);
}

.search-link {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px;
  color: var(--text-secondary);
  text-decoration: none;
  border-radius: 6px;
  margin-bottom: 8px;
  transition: all 0.2s;
}

.search-link:hover {
  color: var(--text-primary);
  background-color: var(--bg-tertiary);
}

.search-link.active {
  color: var(--text-primary);
  background-color: var(--accent-blue);
}

/* Search Page Styles */
.search-page {
  max-width: 800px;
  margin: 0 auto;
}

.search-header {
  text-align: center;
  margin-bottom: 32px;
}

.search-header h1 {
  font-size: 32px;
  font-weight: bold;
  margin-bottom: 8px;
}

.search-header p {
  font-size: 16px;
  color: var(--text-secondary);
}

.search-form {
  margin-bottom: 32px;
}

.search-input-container {
  display: flex;
  gap: 8px;
  max-width: 600px;
  margin: 0 auto;
}

.search-page-input {
  flex: 1;
  padding: 12px 16px;
  background-color: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  color: var(--text-primary);
  font-size: 16px;
}

.search-page-input:focus {
  outline: none;
  border-color: var(--accent-blue);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.search-btn {
  padding: 12px 16px;
  background-color: var(--accent-blue);
  border: none;
  border-radius: 8px;
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 0.2s;
}

.search-btn:hover {
  background-color: #2563eb;
}

.search-page-results {
  min-height: 200px;
}

.search-placeholder, .no-results {
  text-align: center;
  padding: 48px 24px;
  color: var(--text-muted);
}

.search-placeholder h3, .no-results h3 {
  margin: 16px 0 8px;
  color: var(--text-secondary);
}

.search-results-header {
  margin-bottom: 16px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--border-color);
}

.search-results-header h3 {
  color: var(--text-primary);
  font-size: 18px;
}

.search-results-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.search-result-card {
  background-color: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 20px;
  cursor: pointer;
  transition: all 0.2s;
}

.search-result-card:hover {
  border-color: var(--accent-blue);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.result-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
}

.result-header h4 {
  font-size: 18px;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0;
}

.result-description {
  color: var(--text-secondary);
  margin-bottom: 8px;
  line-height: 1.5;
}

.result-params, .result-fields {
  font-size: 14px;
  color: var(--text-muted);
}

.result-params strong, .result-fields strong {
  color: var(--text-secondary);
}

/* Code Styles */
pre {
  background-color: var(--bg-tertiary);
  border: 1px solid var(--border-color);
  border-radius: 6px;
  padding: 16px;
  overflow-x: auto;
  margin: 16px 0;
}

code {
  background-color: var(--bg-tertiary);
  padding: 2px 4px;
  border-radius: 3px;
  font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
  font-size: 14px;
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .sidebar {
    width: 100%;
    transform: translateX(-100%);
    transition: transform 0.3s;
  }
  
  .main-content {
    margin-left: 0;
    max-width: 100vw;
    padding: 16px;
  }
  
  .search-input {
    width: 200px;
  }
  
  .search-input-container {
    flex-direction: column;
  }
  
  .search-page-input {
    font-size: 16px; /* Prevent zoom on iOS */
  }
}

/* Print Styles */
@media print {
  .header, .sidebar {
    display: none;
  }
  
  .main-content {
    margin-left: 0;
    max-width: 100%;
  }
}: #fca5a5;
  border: 1px solid rgba(239, 68, 68, 0.3);
}

.badge-gray {
  background-color: rgba(100, 116, 139, 0.2);
  color: #cbd5e1;
  border: 1px solid rgba(100, 116, 139, 0.3);
}

/* Hero - Optimized */
.hero {
  text-align: center;
  padding: 64px 0;
  max-width: 800px;
  margin: 0 auto;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background-color: rgba(59, 130, 246, 0.2);
  border: 1px solid rgba(59, 130, 246, 0.3);
  border-radius: 20px;
  color: #93c5fd;
  font-size: 14px;
  margin-bottom: 32px;
}

.hero-title {
  font-size: 48px;
  font-weight: bold;
  margin-bottom: 24px;
  line-height: 1.2;
}

.hero-gradient {
  background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-description {
  font-size: 20px;
  color: var(--text-secondary);
  margin-bottom: 32px;
}

.hero-buttons {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  margin-bottom: 48px;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 24px;
  border-radius: 6px;
  text-decoration: none;
  font-weight: 500;
  border: none;
  cursor: pointer;
  font-size: 16px;
}

.btn-primary {
  background-color: var(--accent-blue);
  color: white;
}

.btn-secondary {
  background-color: var(--bg-secondary);
  color: var(--text-primary);
  border: 1px solid var(--border-color);
}

/* Stats grid - Optimized */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 24px;
  margin-top: 48px;
}

.stat-card {
  text-align: center;
  padding: 24px;
  background-color: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  text-decoration: none;
  color: inherit;
}

.stat-number {
  font-size: 32px;
  font-weight: bold;
  color: var(--accent-blue);
  margin-bottom: 8px;
}

.stat-label {
  color: var(--text-secondary);
  font-size: 14px;
}

/* Code blocks - Optimized */
.code-container {
  background-color: var(--bg-primary);
  border: 1px solid var(--border-color);
  border-radius: 6px;
  overflow: hidden;
}

.code-header {
  display: flex;
  align-items: center;
  justify-content: between;
  padding: 12px 16px;
  background-color: var(--bg-tertiary);
  border-bottom: 1px solid var(--border-color);
  font-size: 12px;
  color: var(--text-muted);
  text-transform: uppercase;
}

.code-block {
  padding: 16px;
  overflow-x: auto;
}

.code-block pre {
  margin: 0;
  font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
  font-size: 14px;
  line-height: 1.5;
}

/* Parameters - Optimized */
.parameters-title {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 16px;
}

.parameter-indicator {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.parameter-indicator.required {
  background-color: var(--accent-red);
}

.parameter-indicator.optional {
  background-color: var(--text-muted);
}

.parameter-item {
  background-color: var(--bg-primary);
  border: 1px solid var(--border-color);
  border-radius: 6px;
  padding: 16px;
  margin-bottom: 12px;
}

.parameter-header {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  margin-bottom: 8px;
}

.parameter-name {
  font-size: 16px;
  font-weight: 600;
}

.parameter-description {
  color: var(--text-secondary);
  margin-top: 4px;
}

.back-button {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background: none;
  border: none;
  color: var(--text-muted);
  text-decoration: none;
  border-radius: 4px;
  margin-bottom: 24px;
}

/* Responsive - Optimized */
@media (max-width: 768px) {
  .sidebar {
    transform: translateX(-100%);
  }
  
  .main-content {
    margin-left: 0;
    max-width: 100vw;
    padding: 16px;
  }
  
  .search-input {
    width: 200px;
  }
  
  .hero-title {
    font-size: 36px;
  }
}

/* Prism overrides - Minimal */
pre[class*="language-"] {
  background: transparent !important;
  margin: 0 !important;
  padding: 0 !important;
}

code[class*="language-"] {
  color: var(--text-primary) !important;
}
"""


def create_javascript():
    """Create optimized JavaScript functionality"""
    return """// tgram Documentation JavaScript - Optimized

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
"""


def generate_sidebar_content(methods, types, current_page=""):
    """Generate sidebar HTML content"""
    # Group methods by category
    method_categories = {}
    for method_name in methods.keys():
        category = method_name.split("_")[0] or "general"
        if category not in method_categories:
            method_categories[category] = []
        method_categories[category].append(method_name)

    # Determine the correct path prefix based on current page
    if current_page == "":
        # We're on the homepage
        method_prefix = "methods/"
        type_prefix = "types/"
    elif current_page.startswith("methods/"):
        # We're on a method page
        method_prefix = ""
        type_prefix = "../types/"
    elif current_page.startswith("types/"):
        # We're on a type page
        method_prefix = "../methods/"
        type_prefix = ""
    else:
        # Default case
        method_prefix = "methods/"
        type_prefix = "types/"

    sidebar_html = f"""
    <div class="sidebar-section">
        <a href="{"" if current_page == "" else "../" if current_page.startswith(("methods/", "types/")) else ""}search.html" class="search-link {"active" if current_page == "search" else ""}">
            <span class="search-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
                </svg>
            </span>
            <span>Advanced Search</span>
        </a>
    </div>
    
    <div class="sidebar-section">
        <button class="sidebar-title collapsible" data-target="methods-section">
            <span class="sidebar-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M19,3H5C3.9,3,3,3.9,3,5v14c0,1.1,0.9,2,2,2h14c1.1,0,2-0.9,2-2V5C21,3.9,20.1,3,19,3z M19,19H5V5h14V19z"/>
                    <path d="M7,7h10v2H7V7z M7,11h10v2H7V11z M7,15h7v2H7V15z"/>
                </svg>
            </span>
            <span>Methods ({len(methods)})</span>
            <span class="collapse-icon">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M7.41,8.58L12,13.17L16.59,8.58L18,10L12,16L6,10L7.41,8.58Z"/>
                </svg>
            </span>
        </button>
        <div class="sidebar-content collapsible-content" id="methods-section">
    """

    for category, method_list in sorted(method_categories.items()):
        sidebar_html += f"""
            <div class="sidebar-category">
                <button class="category-title collapsible" data-target="category-{category}">
                    <span class="category-icon">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M10,4H4C2.89,4,2,4.89,2,6V18A2,2 0 0,0 4,20H20A2,2 0 0,0 22,18V8C22,6.89 21.1,6 20,6H12L10,4Z"/>
                        </svg>
                    </span>
                    <span>{category} ({len(method_list)})</span>
                    <span class="collapse-icon">
                        <svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M7.41,8.58L12,13.17L16.59,8.58L18,10L12,16L6,10L7.41,8.58Z"/>
                        </svg>
                    </span>
                </button>
                <div class="category-methods collapsible-content" id="category-{category}">
        """

        for method in sorted(method_list):
            active_class = "active" if current_page == f"methods/{method}" else ""
            sidebar_html += f'''
                <a href="{method_prefix}{method}.html" class="sidebar-link {active_class}">
                    {method}
                </a>
            '''

        sidebar_html += "</div></div>"

    sidebar_html += (
        """
        </div>
    </div>
    
    <div class="sidebar-section">
        <button class="sidebar-title collapsible" data-target="types-section">
            <span class="sidebar-icon">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12,2A3,3 0 0,1 15,5V7H20A2,2 0 0,1 22,9V19A2,2 0 0,1 20,21H4A2,2 0 0,1 2,19V9A2,2 0 0,1 4,7H9V5A3,3 0 0,1 12,2M12,4A1,1 0 0,0 11,5V7H13V5A1,1 0 0,0 12,4Z"/>
                </svg>
            </span>
            <span>Types """
        + f"({len(types)})"
        + """</span>
            <span class="collapse-icon">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M7.41,8.58L12,13.17L16.59,8.58L18,10L12,16L6,10L7.41,8.58Z"/>
                </svg>
            </span>
        </button>
        <div class="sidebar-content collapsible-content" id="types-section">
    """
    )

    for type_name in sorted(types.keys()):
        active_class = "active" if current_page == f"types/{type_name}" else ""
        sidebar_html += f'''
            <a href="{type_prefix}{type_name}.html" class="sidebar-link {active_class}">
                {type_name}
            </a>
        '''

    sidebar_html += """
        </div>
    </div>
    """

    return sidebar_html


def generate_index_page(data, output_dir):
    """Generate the main index page - FIXED to use actual data"""
    methods = data["methods"]
    types = data["types"]

    print(f"🔍 Index page debug - Methods: {len(methods)}, Types: {len(types)}")
    print(f"   First 3 methods: {list(methods.keys())[:3]}")
    print(f"   First 3 types: {list(types.keys())[:3]}")

    # Calculate statistics
    method_categories = {}
    for method_name in methods.keys():
        category = method_name.split("_")[0] or "general"
        method_categories[category] = method_categories.get(category, 0) + 1

    # Generate optimized main content
    main_content = f"""
    <div class="hero">
        <div class="hero-badge">
            <span>⭐</span>
            Modern Telegram Bot API Library
        </div>
        
        <h1 class="hero-title">
            Build Powerful Telegram Bots with 
            <span class="hero-gradient">tgram</span>
        </h1>
        
        <p class="hero-description">
            A modern, type-safe Python library for the Telegram Bot API. 
            Simple, fast, and feature-complete with full async support.
        </p>
        
        <div class="hero-buttons">
            <a href="#stats" class="btn btn-primary">
                <span>🚀</span>
                Explore Documentation
            </a>
            <button class="btn btn-secondary" onclick="navigator.clipboard.writeText('pip install tgram'); this.innerHTML='<span>✅</span> Copied!';">
                <span>📦</span>
                pip install tgram
            </button>
        </div>
        
        <div class="code-container">
            <div class="code-header">Quick Start Example</div>
            <div class="code-block">
                <pre><code class="language-python">from tgram import Bot

bot = Bot("YOUR_BOT_TOKEN")

# Send a message
await bot.send_message(
    chat_id=123456789,
    text="Hello from tgram!"
)

# Get updates  
updates = await bot.get_updates()
print(updates)</code></pre>
            </div>
        </div>
    </div>
    
    <div class="stats-grid" id="stats">
        <a href="methods/index.html" class="stat-card">
            <div class="stat-number">{len(methods)}</div>
            <div class="stat-label">Methods Available</div>
        </a>
        <a href="types/index.html" class="stat-card">
            <div class="stat-number">{len(types)}</div>
            <div class="stat-label">Type Definitions</div>
        </a>
    </div>
    """

    # Generate sidebar with actual data
    sidebar_content = generate_sidebar_content(methods, types, "")

    template = create_base_template()
    html = template.format(
        title="tgram Documentation",
        css_path="",
        root_path="",
        sidebar_content=sidebar_content,
        main_content=main_content,
    )

    with open(output_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Generated index.html with {len(methods)} methods and {len(types)} types")


def generate_method_page(method_name, method_data, data, output_dir):
    """Generate individual method page"""
    methods = data["methods"]
    types = data["types"]
    available_types = list(types.keys())
    # Process parameters
    parameters = method_data.get("parameters", {})
    required_params = [
        (k, v) for k, v in parameters.items() if v.get("required", False)
    ]
    optional_params = [
        (k, v) for k, v in parameters.items() if not v.get("required", False)
    ]

    # Generate example
    example = generate_method_example(method_name, method_data)

    # Create type links
    def create_type_link(type_str):
        if not type_str:
            return "Unknown"

        skip_types = {
            "str",
            "int",
            "float",
            "bool",
            "dict",
            "list",
            "None",
            "Any",
            "Optional",
            "Union",
            "List",
            "Literal",
        }

        # Sort available types by length (longest first) to match longer types first
        sorted_types = sorted(
            [t for t in available_types if t not in skip_types], key=len, reverse=True
        )

        result = type_str

        # Replace each type, starting with the longest ones
        for type_name in sorted_types:
            # Use word boundaries to ensure we match complete type names
            pattern = r"\b" + re.escape(type_name) + r"\b"
            replacement = f'<a href="../types/{type_name}.html" class="badge badge-blue">{type_name}</a>'
            result = re.sub(pattern, replacement, result)

        return result

    main_content = f"""
    <div class="page-header">
        <a href="../index.html" class="back-button">
            <span>←</span>
            Back to Documentation
        </a>
        
        <h1 class="page-title">{method_name}</h1>
        <p class="page-description">{method_data.get("description", "No description available")}</p>
        
        <div style="display: flex; gap: 12px; margin-top: 16px;">
            <span class="badge badge-blue">
                Returns: {create_type_link(method_data.get("returns", "Unknown"))}
            </span>
        </div>
    </div>
    """

    if method_data.get("path"):
        main_content += f"""
        <div class="card">
            <div class="card-title">Module Path</div>
            <code style="color: var(--text-secondary);">{method_data["path"]}</code>
        </div>
        """

    # Parameters section
    if parameters:
        main_content += """
        <div class="card">
            <div class="card-title">Parameters</div>
        """

        if required_params:
            main_content += f"""
            <div class="parameters-section">
                <div class="parameters-title">
                    <span class="parameter-indicator required"></span>
                    Required Parameters ({len(required_params)})
                </div>
            """

            for param_name, param_info in required_params:
                main_content += f"""
                <div class="parameter-item">
                    <div class="parameter-header">
                        <span class="badge badge-red">{create_type_link(param_info.get("type", "Unknown"))}</span>
                        <div>
                            <div class="parameter-name">{param_name}</div>
                            <div class="parameter-description">{param_info.get("description", "No description available")}</div>
                        </div>
                    </div>
                </div>
                """

            main_content += "</div>"

        if optional_params:
            main_content += f"""
            <div class="parameters-section">
                <div class="parameters-title">
                    <span class="parameter-indicator optional"></span>
                    Optional Parameters ({len(optional_params)})
                </div>
            """

            for param_name, param_info in optional_params:
                main_content += f"""
                <div class="parameter-item">
                    <div class="parameter-header">
                        <span class="badge badge-gray">{create_type_link(param_info.get("type", "Unknown"))}</span>
                        <div>
                            <div class="parameter-name">{param_name}</div>
                            <div class="parameter-description">{param_info.get("description", "No description available")}</div>
                        </div>
                    </div>
                </div>
                """

            main_content += "</div>"

        main_content += "</div>"

    # Example section
    main_content += f"""
    <div class="card">
        <div class="card-title">Complete Example</div>
        <div class="code-container">
            <div class="code-header">
                Python
                <button onclick="copyCode(this)" style="margin-left: auto; background: none; border: none; color: var(--text-muted); cursor: pointer;">
                    Copy
                </button>
            </div>
            <div class="code-block">
                <pre><code class="language-python">from tgram import Bot

bot = Bot("YOUR_BOT_TOKEN")

# {method_data.get("description", "Method call")}
result = {example}

print(result)</code></pre>
            </div>
        </div>
    </div>
    """

    # Return type section
    main_content += f"""
    <div class="card">
        <div class="card-title">Return Value</div>
        <div style="display: flex; align-items: center; gap: 12px;">
            <span class="badge badge-blue" style="font-size: 16px; padding: 8px 16px;">
                {create_type_link(method_data.get("returns", "Unknown"))}
            </span>
            <p style="color: var(--text-secondary); margin: 0;">
                This method returns a <code>{method_data.get("returns", "Unknown")}</code> object on success.
            </p>
        </div>
    </div>
    """

    sidebar_content = generate_sidebar_content(methods, types, f"methods/{method_name}")

    template = create_base_template()
    html = template.format(
        title=method_name,
        css_path="../",
        root_path="../",
        sidebar_content=sidebar_content,
        main_content=main_content,
    )

    method_dir = output_dir / "methods"
    method_dir.mkdir(exist_ok=True)

    with open(method_dir / f"{method_name}.html", "w", encoding="utf-8") as f:
        f.write(html)


def generate_type_page(type_name, type_data, data, output_dir):
    """Generate individual type page"""
    methods = data["methods"]
    types = data["types"]
    available_types = list(types.keys())

    # Create type links
    def create_type_link(type_str):
        if not type_str:
            return "Unknown"

        skip_types = {
            "str",
            "int",
            "float",
            "bool",
            "dict",
            "list",
            "None",
            "Any",
            "Optional",
            "Union",
            "List",
            "Literal",
        }

        # Sort available types by length (longest first) to match longer types first
        sorted_types = sorted(
            [t for t in available_types if t not in skip_types], key=len, reverse=True
        )

        result = type_str

        # Replace each type, starting with the longest ones
        for type_name in sorted_types:
            # Use word boundaries to ensure we match complete type names
            pattern = r"\b" + re.escape(type_name) + r"\b"
            replacement = (
                f'<a href="{type_name}.html" class="badge badge-purple">{type_name}</a>'
            )
            result = re.sub(pattern, replacement, result)

        return result

    main_content = f"""
    <div class="page-header">
        <a href="../index.html" class="back-button">
            <span>←</span>
            Back to Documentation
        </a>
        
        <h1 class="page-title">{type_name}</h1>
        <p class="page-description">{type_data.get("description", "No description available")}</p>
        
        <div style="display: flex; gap: 12px; margin-top: 16px;">
            <span class="badge badge-purple">Type</span>
        </div>
    </div>
    """

    # Properties section
    properties = type_data.get("properties", {})
    if properties:
        main_content += f"""
        <div class="card">
            <div class="card-title">Properties ({len(properties)})</div>
        """

        for prop_name, prop_info in properties.items():
            main_content += f"""
            <div class="parameter-item">
                <div class="parameter-header">
                    <span class="badge badge-blue">{create_type_link(prop_info.get("type", "Unknown"))}</span>
                    <div>
                        <div class="parameter-name">{prop_name}</div>
                        <div class="parameter-description">{prop_info.get("description", "No description available")}</div>
                    </div>
                </div>
            </div>
            """

        main_content += "</div>"

    # Usage section
    main_content += """
    <div class="card">
        <div class="card-title">Usage in Methods</div>
        <p style="color: var(--text-secondary); margin-bottom: 16px;">
            This type is commonly used in the following scenarios:
        </p>
        <div style="background-color: var(--bg-primary); border: 1px solid var(--border-color); border-radius: 6px; padding: 16px;">
            <ul style="color: var(--text-secondary); margin: 0; padding-left: 20px;">
                <li>As a return type from API methods</li>
                <li>As a parameter type in method calls</li>
                <li>In webhook updates and responses</li>
            </ul>
        </div>
    </div>
    """

    sidebar_content = generate_sidebar_content(methods, types, f"types/{type_name}")

    template = create_base_template()
    html = template.format(
        title=type_name,
        css_path="../",
        root_path="../",
        sidebar_content=sidebar_content,
        main_content=main_content,
    )

    type_dir = output_dir / "types"
    type_dir.mkdir(exist_ok=True)

    with open(type_dir / f"{type_name}.html", "w", encoding="utf-8") as f:
        f.write(html)


def generate_methods_index(data, output_dir):
    """Generate methods index page"""
    methods = data["methods"]
    types = data["types"]

    # Group methods by category
    method_categories = {}
    for method_name, method_data in methods.items():
        category = method_name.split("_")[0] or "general"
        if category not in method_categories:
            method_categories[category] = []
        method_categories[category].append((method_name, method_data))

    main_content = f"""
    <div class="page-header">
        <a href="../index.html" class="back-button">
            <span>←</span>
            Back to Documentation
        </a>
        
        <h1 class="page-title">All Methods</h1>
        <p class="page-description">
            Complete list of all {len(methods)} available methods in the tgram library.
        </p>
    </div>
    """

    for category, method_list in sorted(method_categories.items()):
        main_content += f"""
        <div class="card">
            <div class="card-title">
                <span style="color: var(--accent-blue);">●</span>
                {category.title()} Methods ({len(method_list)})
            </div>
            <div style="display: grid; gap: 12px;">
        """

        for method_name, method_data in sorted(method_list):
            main_content += f'''
            <a href="{method_name}.html" style="text-decoration: none; color: inherit;">
                <div style="background-color: var(--bg-primary); border: 1px solid var(--border-color); border-radius: 6px; padding: 16px; transition: all 0.2s;">
                    <div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 8px;">
                        <h3 style="margin: 0; font-size: 16px; font-weight: 600;">{method_name}</h3>
                        <span class="badge badge-blue">{method_data.get("returns", "Unknown")}</span>
                    </div>
                    <p style="margin: 0; color: var(--text-secondary); font-size: 14px;">
                        {method_data.get("description", "No description available")[:100]}{"..." if len(method_data.get("description", "")) > 100 else ""}
                    </p>
                </div>
            </a>
            '''

        main_content += """
            </div>
        </div>
        """

    sidebar_content = generate_sidebar_content(methods, types)

    template = create_base_template()
    html = template.format(
        title="All Methods",
        css_path="../",
        root_path="../",
        sidebar_content=sidebar_content,
        main_content=main_content,
    )

    method_dir = output_dir / "methods"
    method_dir.mkdir(exist_ok=True)

    with open(method_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(html)


def generate_types_index(data, output_dir):
    """Generate types index page"""
    methods = data["methods"]
    types = data["types"]

    main_content = f"""
    <div class="page-header">
        <a href="../index.html" class="back-button">
            <span>←</span>
            Back to Documentation
        </a>
        
        <h1 class="page-title">All Types</h1>
        <p class="page-description">
            Complete list of all {len(types)} available types in the tgram library.
        </p>
    </div>
    
    <div style="display: grid; gap: 16px;">
    """

    for type_name, type_data in sorted(types.items()):
        properties_count = len(type_data.get("properties", {}))
        main_content += f'''
        <a href="{type_name}.html" style="text-decoration: none; color: inherit;">
            <div class="card" style="transition: all 0.2s; cursor: pointer;">
                <div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 16px;">
                    <div>
                        <h3 style="margin: 0 0 8px 0; font-size: 20px; font-weight: 600;">{type_name}</h3>
                        <p style="margin: 0; color: var(--text-secondary);">{type_data.get("description", "No description available")}</p>
                    </div>
                    <span class="badge badge-purple">Type</span>
                </div>
                <div style="font-size: 14px; color: var(--text-muted);">
                    {properties_count} properties
                </div>
            </div>
        </a>
        '''

    main_content += "</div>"

    sidebar_content = generate_sidebar_content(methods, types)

    template = create_base_template()
    html = template.format(
        title="All Types",
        css_path="../",
        root_path="../",
        sidebar_content=sidebar_content,
        main_content=main_content,
    )

    type_dir = output_dir / "types"
    type_dir.mkdir(exist_ok=True)

    with open(type_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(html)


def create_search_data_js(data, output_dir):
    """Create JavaScript file with search data"""
    js_content = f"""// Search data for tgram documentation
window.tgramMethods = {json.dumps(data["methods"], indent=2)};
window.tgramTypes = {json.dumps(data["types"], indent=2)};
"""

    with open(output_dir / "search-data.js", "w", encoding="utf-8") as f:
        f.write(js_content)


def generate_search_page(data, output_dir):
    """Generate dedicated search results page"""
    template = create_base_template()
    sidebar_content = generate_sidebar_content(data["methods"], data["types"], "search")

    search_content = """
    <div class="search-page">
        <div class="search-header">
            <h1>Search Documentation</h1>
            <p>Search through all methods and types in the tgram library</p>
        </div>
        
        <div class="search-form">
            <div class="search-input-container">
                <input type="text" id="search-page-input" placeholder="Enter your search query..." class="search-page-input">
                <button id="search-page-btn" class="search-btn">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
                    </svg>
                </button>
            </div>
        </div>
        
        <div id="search-page-results" class="search-page-results">
            <div class="search-placeholder">
                <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor" opacity="0.3">
                    <path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
                </svg>
                <h3>Start typing to search</h3>
                <p>Search through methods, types, and descriptions</p>
            </div>
        </div>
    </div>
    """

    html_content = template.format(
        title="Search",
        css_path="",
        root_path="",
        sidebar_content=sidebar_content,
        main_content=search_content,
    )

    with open(output_dir / "search.html", "w", encoding="utf-8") as f:
        f.write(html_content)


def create_github_pages_config(output_dir):
    """Create GitHub Pages configuration files"""

    # Create .nojekyll to disable Jekyll processing
    with open(output_dir / ".nojekyll", "w") as f:
        f.write("")

    # Create CNAME file (optional - user can modify)
    cname_content = "# Replace with your custom domain\n# your-domain.com"
    with open(output_dir / "CNAME.example", "w") as f:
        f.write(cname_content)

    # Create README for the docs
    readme_content = f"""# tgram Documentation

This is the auto-generated documentation for the tgram Python library.

## 🚀 Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

### 📊 Statistics:
- **Methods**: {len(data["methods"]) if "data" in globals() else "N/A"}
- **Types**: {len(data["types"]) if "data" in globals() else "N/A"}

### 🔧 Auto-Generation:
This documentation is automatically generated from the tgram JSON schema.

To update:
1. Update your `tgram_schema.json` file
2. Run `python generate_html_docs.py`
3. Commit and push to GitHub

### 🌐 GitHub Pages:
This site is hosted on GitHub Pages. Any changes to the `docs/` directory will automatically update the live site.

---
Generated by tgram documentation generator
"""

    with open(output_dir / "README.md", "w") as f:
        f.write(readme_content)


def main():
    """Main function to generate HTML documentation"""
    import sys

    print("🚀 Generating static HTML documentation for GitHub Pages...")

    # Get JSON file path
    json_path = sys.argv[1] if len(sys.argv) > 1 else "tgram_schema.json"

    # Load data
    global data
    data = load_json_data(json_path)
    if not data:
        return 1

    # Debug: Show what was actually loaded
    print("\n🔍 Debug - Loaded data:")
    print(f"   📚 Methods found: {list(data['methods'].keys())}")
    print(f"   🏷️  Types found: {list(data['types'].keys())}")

    # Create output directory
    output_dir = Path("docs")
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir()

    print("📁 Creating directory structure...")
    (output_dir / "methods").mkdir()
    (output_dir / "types").mkdir()

    print("🎨 Generating CSS and JavaScript...")
    # Create CSS file
    with open(output_dir / "styles.css", "w", encoding="utf-8") as f:
        f.write(create_css())

    # Create JavaScript file
    with open(output_dir / "script.js", "w", encoding="utf-8") as f:
        f.write(create_javascript())

    # Create search data
    create_search_data_js(data, output_dir)

    # Create favicon (simple SVG)
    favicon_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <rect width="100" height="100" rx="20" fill="url(#grad)"/>
        <defs>
            <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#3b82f6"/>
                <stop offset="100%" style="stop-color:#8b5cf6"/>
            </linearGradient>
        </defs>
        <text x="50" y="65" font-family="Arial, sans-serif" font-size="60" font-weight="bold" text-anchor="middle" fill="white">T</text>
    </svg>"""

    with open(output_dir / "favicon.svg", "w") as f:
        f.write(favicon_svg)

    print("📄 Generating pages...")

    # Generate main pages
    generate_index_page(data, output_dir)
    generate_methods_index(data, output_dir)
    generate_types_index(data, output_dir)
    generate_search_page(data, output_dir)

    # Generate method pages
    print(f"📝 Generating {len(data['methods'])} method pages...")
    for method_name, method_data in data["methods"].items():
        generate_method_page(method_name, method_data, data, output_dir)

    # Generate type pages
    print(f"🏷️ Generating {len(data['types'])} type pages...")
    for type_name, type_data in data["types"].items():
        generate_type_page(type_name, type_data, data, output_dir)

    # Create GitHub Pages config
    print("⚙️ Creating GitHub Pages configuration...")
    create_github_pages_config(output_dir)

    # Calculate statistics
    method_categories = {}
    for method_name in data["methods"].keys():
        category = method_name.split("_")[0] or "general"
        method_categories[category] = method_categories.get(category, 0) + 1

    print(f"""
🎉 Static HTML documentation generated successfully!

📊 Statistics:
   • Methods: {len(data["methods"])}
   • Types: {len(data["types"])}
   • Categories: {len(method_categories)}
   • Total Pages: {len(data["methods"]) + len(data["types"]) + 3}

📂 Generated Files:
   • docs/index.html (main page)
   • docs/methods/*.html ({len(data["methods"])} method pages)
   • docs/types/*.html ({len(data["types"])} type pages)
   • docs/styles.css (styling)
   • docs/script.js (functionality)
   • docs/.nojekyll (GitHub Pages config)

📁 Method Categories:""")

    for category, count in sorted(method_categories.items()):
        print(f"   • {category}: {count} methods")

    print("""
🌐 Ready for GitHub Pages hosting!
""")

    return 0


if __name__ == "__main__":
    exit(main())
