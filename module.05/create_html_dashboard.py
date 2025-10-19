"""
Module 05: HTML Dashboard Creator
==================================

Creates an interactive single-page HTML dashboard combining all three dashboards.
This creates a professional web-based dashboard for portfolio showcase.

Author: Diaa
Date: October 2025
"""

import os

OUTPUT_DIR = './outputs/'
HTML_OUTPUT = f'{OUTPUT_DIR}Interactive_Dashboard.html'

def create_html_dashboard():
    """Create a single-page HTML dashboard with tabs."""
    print("\n" + "="*60)
    print("CREATING INTERACTIVE HTML DASHBOARD")
    print("="*60)
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Analyst Capstone - Dashboard</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        
        .container {
            max-width: 1800px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            margin-bottom: 30px;
            text-align: center;
        }
        
        header h1 {
            color: #2c3e50;
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        header p {
            color: #7f8c8d;
            font-size: 1.2em;
        }
        
        .author-info {
            margin-top: 15px;
            padding-top: 15px;
            border-top: 2px solid #ecf0f1;
        }
        
        .author-info p {
            color: #95a5a6;
            font-size: 0.9em;
        }
        
        .tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }
        
        .tab {
            background: white;
            padding: 15px 30px;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 600;
            color: #34495e;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .tab:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
        
        .tab.active {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        
        .dashboard-container {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        
        .dashboard {
            display: none;
        }
        
        .dashboard.active {
            display: block;
        }
        
        .dashboard-title {
            color: #2c3e50;
            font-size: 2em;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 3px solid #3498db;
        }
        
        .dashboard-description {
            color: #7f8c8d;
            font-size: 1.1em;
            margin-bottom: 30px;
            line-height: 1.6;
        }
        
        iframe {
            width: 100%;
            height: 900px;
            border: none;
            border-radius: 10px;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .stat-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .stat-card h3 {
            font-size: 1.2em;
            margin-bottom: 10px;
            opacity: 0.9;
        }
        
        .stat-card p {
            font-size: 2em;
            font-weight: bold;
        }
        
        footer {
            text-align: center;
            padding: 30px;
            color: white;
            margin-top: 30px;
        }
        
        footer a {
            color: white;
            text-decoration: none;
            font-weight: bold;
        }
        
        footer a:hover {
            text-decoration: underline;
        }
        
        @media (max-width: 768px) {
            header h1 {
                font-size: 1.8em;
            }
            
            .tabs {
                flex-direction: column;
            }
            
            .tab {
                width: 100%;
            }
            
            iframe {
                height: 600px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📊 Data Analyst Capstone Dashboard</h1>
            <p>Stack Overflow Developer Survey Analysis - Module 05</p>
            <div class="author-info">
                <p><strong>Author:</strong> Diaa | <strong>Date:</strong> October 2025</p>
                <p><strong>Technologies:</strong> Python • Plotly • Pandas • HTML/CSS</p>
            </div>
        </header>
        
        <div class="stats-grid">
            <div class="stat-card">
                <h3>Dashboards</h3>
                <p>3</p>
            </div>
            <div class="stat-card">
                <h3>Visualizations</h3>
                <p>12+</p>
            </div>
            <div class="stat-card">
                <h3>Data Points</h3>
                <p>10,000+</p>
            </div>
            <div class="stat-card">
                <h3>Technologies Analyzed</h3>
                <p>50+</p>
            </div>
        </div>
        
        <div class="tabs">
            <div class="tab active" onclick="showDashboard('current')">
                Current Technology Usage
            </div>
            <div class="tab" onclick="showDashboard('future')">
                Future Technology Trends
            </div>
            <div class="tab" onclick="showDashboard('demographics')">
                Demographics
            </div>
        </div>
        
        <div class="dashboard-container">
            <div id="current" class="dashboard active">
                <h2 class="dashboard-title">Current Technology Usage</h2>
                <p class="dashboard-description">
                    Explore the current technology stack of developers, including the most popular 
                    programming languages, databases, platforms, and web frameworks actively being used.
                </p>
                <iframe src="dashboard_1_current_tech.html"></iframe>
            </div>
            
            <div id="future" class="dashboard">
                <h2 class="dashboard-title">Future Technology Trends</h2>
                <p class="dashboard-description">
                    Discover what technologies developers want to learn and work with in the coming year, 
                    revealing emerging trends and future directions in software development.
                </p>
                <iframe src="dashboard_2_future_tech.html"></iframe>
            </div>
            
            <div id="demographics" class="dashboard">
                <h2 class="dashboard-title">Demographics Analysis</h2>
                <p class="dashboard-description">
                    Understand the demographics of the developer community, including age distribution, 
                    geographic spread, education levels, and how these factors intersect.
                </p>
                <iframe src="dashboard_3_demographics.html"></iframe>
            </div>
        </div>
        
        <footer>
            <p>Created with ❤️ using Python | 
            <a href="https://github.com/engomaressam/data.analyst.capstone" target="_blank">View on GitHub</a></p>
            <p style="margin-top: 10px; opacity: 0.8;">Module 05: Dashboard Creation - Data Analyst Professional Certificate</p>
        </footer>
    </div>
    
    <script>
        function showDashboard(dashboardId) {
            // Hide all dashboards
            const dashboards = document.querySelectorAll('.dashboard');
            dashboards.forEach(d => d.classList.remove('active'));
            
            // Remove active class from all tabs
            const tabs = document.querySelectorAll('.tab');
            tabs.forEach(t => t.classList.remove('active'));
            
            // Show selected dashboard
            document.getElementById(dashboardId).classList.add('active');
            
            // Add active class to clicked tab
            event.target.classList.add('active');
        }
    </script>
</body>
</html>"""
    
    # Write HTML file
    with open(HTML_OUTPUT, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("="*60)
    print(f"✅ INTERACTIVE HTML DASHBOARD CREATED")
    print("="*60)
    print(f"Output: {os.path.abspath(HTML_OUTPUT)}")
    print("\nTo view: Open the file in your web browser")
    print("Note: Individual dashboard HTML files must be in the same directory")

if __name__ == "__main__":
    create_html_dashboard()
