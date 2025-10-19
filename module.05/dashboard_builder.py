"""
Module 05: Dashboard Creation with Python
==========================================

Creates professional dashboards using Plotly and exports to PDF and HTML.
This demonstrates advanced Python visualization skills for employers.

Author: Diaa
Date: October 2025
"""

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# CONFIGURATION
# ============================================================================

DATA_FILE = '../data/survey_results_updated.csv'
OUTPUT_DIR = './outputs/'

# Create output directory if it doesn't exist
import os
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================================================
# DATA LOADING AND PREPARATION
# ============================================================================

def load_and_prepare_data(file_path):
    """Load and prepare the survey data."""
    print("Loading data...")
    df = pd.read_sql_query("SELECT * FROM main", conn) if 'conn' in globals() else pd.read_csv(file_path)
    print(f"Data loaded: {len(df)} records, {len(df.columns)} columns")
    return df

def get_top_n(series, n=10, split_char=';'):
    """
    Get top N items from a series that may contain multiple values separated by split_char.
    """
    # Split and flatten
    all_items = []
    for item in series.dropna():
        if pd.isna(item):
            continue
        if split_char in str(item):
            all_items.extend([x.strip() for x in str(item).split(split_char)])
        else:
            all_items.append(str(item).strip())
    
    # Count and get top N
    counter = Counter(all_items)
    top_items = counter.most_common(n)
    
    return pd.DataFrame(top_items, columns=['Item', 'Count'])

# ============================================================================
# DASHBOARD 1: CURRENT TECHNOLOGY USAGE
# ============================================================================

def create_current_tech_dashboard(df):
    """Create Current Technology Usage dashboard with 4 panels."""
    print("\n" + "="*60)
    print("Creating CURRENT TECHNOLOGY USAGE Dashboard")
    print("="*60)
    
    # Create subplots: 2 rows x 2 columns
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=(
            'Top 10 Languages Have Worked With',
            'Top 10 Databases Have Worked With',
            'Platforms Have Worked With',
            'Top 10 Web Frameworks Have Worked With'
        ),
        specs=[
            [{"type": "bar"}, {"type": "bar"}],
            [{"type": "scatter"}, {"type": "scatter"}]
        ],
        vertical_spacing=0.15,
        horizontal_spacing=0.12
    )
    
    # Panel 1: Top 10 Languages (Horizontal Bar Chart)
    print("Panel 1: Top 10 Languages...")
    lang_data = get_top_n(df['LanguageHaveWorkedWith'], 10)
    fig.add_trace(
        go.Bar(
            y=lang_data['Item'],
            x=lang_data['Count'],
            orientation='h',
            marker=dict(color='rgb(26, 118, 255)'),
            text=lang_data['Count'],
            textposition='outside',
            name='Languages'
        ),
        row=1, col=1
    )
    
    # Panel 2: Top 10 Databases (Column Chart)
    print("Panel 2: Top 10 Databases...")
    db_data = get_top_n(df['DatabaseHaveWorkedWith'], 10)
    fig.add_trace(
        go.Bar(
            x=db_data['Item'],
            y=db_data['Count'],
            marker=dict(color='rgb(55, 83, 109)'),
            text=db_data['Count'],
            textposition='outside',
            name='Databases'
        ),
        row=1, col=2
    )
    
    # Panel 3: Platforms (Bubble Chart as word cloud alternative)
    print("Panel 3: Platforms...")
    platform_data = get_top_n(df['PlatformHaveWorkedWith'], 15)
    fig.add_trace(
        go.Scatter(
            x=list(range(len(platform_data))),
            y=[1]*len(platform_data),
            mode='markers+text',
            marker=dict(
                size=platform_data['Count']/platform_data['Count'].max()*100,
                color=platform_data['Count'],
                colorscale='Viridis',
                showscale=False
            ),
            text=platform_data['Item'],
            textposition='middle center',
            textfont=dict(size=10),
            name='Platforms'
        ),
        row=2, col=1
    )
    
    # Panel 4: Top 10 Web Frameworks (Hierarchy Bubble / Scatter Bubble)
    print("Panel 4: Top 10 Web Frameworks...")
    webframe_data = get_top_n(df['WebframeHaveWorkedWith'], 10)
    fig.add_trace(
        go.Scatter(
            x=list(range(len(webframe_data))),
            y=webframe_data['Count'],
            mode='markers+text',
            marker=dict(
                size=webframe_data['Count']/webframe_data['Count'].max()*80,
                color=webframe_data['Count'],
                colorscale='RdYlGn',
                showscale=True,
                colorbar=dict(title="Count", x=1.15)
            ),
            text=webframe_data['Item'],
            textposition='top center',
            textfont=dict(size=9),
            name='Web Frameworks'
        ),
        row=2, col=2
    )
    
    # Update layout
    fig.update_xaxes(title_text="Count", row=1, col=1)
    fig.update_xaxes(title_text="Database", tickangle=45, row=1, col=2)
    fig.update_xaxes(showticklabels=False, row=2, col=1)
    fig.update_xaxes(showticklabels=False, row=2, col=2)
    
    fig.update_yaxes(title_text="Language", row=1, col=1)
    fig.update_yaxes(title_text="Count", row=1, col=2)
    fig.update_yaxes(showticklabels=False, row=2, col=1)
    fig.update_yaxes(title_text="Count", row=2, col=2)
    
    fig.update_layout(
        title_text="<b>Current Technology Usage Dashboard</b>",
        title_font_size=24,
        showlegend=False,
        height=900,
        width=1600,
        template='plotly_white'
    )
    
    # Save
    print("Saving Current Technology Usage dashboard...")
    fig.write_html(f"{OUTPUT_DIR}dashboard_1_current_tech.html")
    fig.write_image(f"{OUTPUT_DIR}dashboard_1_current_tech.png", width=1600, height=900)
    print("✅ Current Technology Usage dashboard saved!")
    
    return fig

# ============================================================================
# DASHBOARD 2: FUTURE TECHNOLOGY TRENDS
# ============================================================================

def create_future_tech_dashboard(df):
    """Create Future Technology Trends dashboard with 4 panels."""
    print("\n" + "="*60)
    print("Creating FUTURE TECHNOLOGY TRENDS Dashboard")
    print("="*60)
    
    # Create subplots
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=(
            'Top 10 Languages Want to Work With',
            'Top 10 Databases Want to Work With',
            'Platforms Want to Work With (TreeMap Style)',
            'Top 10 Web Frameworks Want to Work With'
        ),
        specs=[
            [{"type": "bar"}, {"type": "bar"}],
            [{"type": "scatter"}, {"type": "scatter"}]
        ],
        vertical_spacing=0.15,
        horizontal_spacing=0.12
    )
    
    # Panel 1: Top 10 Languages Desired (Bar Chart)
    print("Panel 1: Top 10 Languages Desired...")
    lang_data = get_top_n(df['LanguageWantToWorkWith'], 10)
    fig.add_trace(
        go.Bar(
            y=lang_data['Item'],
            x=lang_data['Count'],
            orientation='h',
            marker=dict(color='rgb(46, 204, 113)'),
            text=lang_data['Count'],
            textposition='outside',
            name='Languages'
        ),
        row=1, col=1
    )
    
    # Panel 2: Top 10 Databases Desired (Column Chart)
    print("Panel 2: Top 10 Databases Desired...")
    db_data = get_top_n(df['DatabaseWantToWorkWith'], 10)
    fig.add_trace(
        go.Bar(
            x=db_data['Item'],
            y=db_data['Count'],
            marker=dict(color='rgb(52, 152, 219)'),
            text=db_data['Count'],
            textposition='outside',
            name='Databases'
        ),
        row=1, col=2
    )
    
    # Panel 3: Platforms Desired (TreeMap style with bubbles)
    print("Panel 3: Platforms Desired...")
    platform_data = get_top_n(df['PlatformWantToWorkWith'], 12)
    # Create treemap-style layout with scatter
    fig.add_trace(
        go.Scatter(
            x=list(range(len(platform_data))),
            y=[i//4 for i in range(len(platform_data))],
            mode='markers+text',
            marker=dict(
                size=platform_data['Count']/platform_data['Count'].max()*120,
                color=platform_data['Count'],
                colorscale='Plasma',
                showscale=False,
                line=dict(width=2, color='white')
            ),
            text=platform_data['Item'],
            textposition='middle center',
            textfont=dict(size=10, color='white'),
            name='Platforms'
        ),
        row=2, col=1
    )
    
    # Panel 4: Top 10 Web Frameworks Desired (Bubble Chart)
    print("Panel 4: Top 10 Web Frameworks Desired...")
    webframe_data = get_top_n(df['WebframeWantToWorkWith'], 10)
    fig.add_trace(
        go.Scatter(
            x=list(range(len(webframe_data))),
            y=webframe_data['Count'],
            mode='markers+text',
            marker=dict(
                size=webframe_data['Count']/webframe_data['Count'].max()*80,
                color=webframe_data['Count'],
                colorscale='Turbo',
                showscale=True,
                colorbar=dict(title="Count", x=1.15)
            ),
            text=webframe_data['Item'],
            textposition='top center',
            textfont=dict(size=9),
            name='Web Frameworks'
        ),
        row=2, col=2
    )
    
    # Update layout
    fig.update_xaxes(title_text="Count", row=1, col=1)
    fig.update_xaxes(title_text="Database", tickangle=45, row=1, col=2)
    fig.update_xaxes(showticklabels=False, row=2, col=1)
    fig.update_xaxes(showticklabels=False, row=2, col=2)
    
    fig.update_yaxes(title_text="Language", row=1, col=1)
    fig.update_yaxes(title_text="Count", row=1, col=2)
    fig.update_yaxes(showticklabels=False, row=2, col=1)
    fig.update_yaxes(title_text="Count", row=2, col=2)
    
    fig.update_layout(
        title_text="<b>Future Technology Trends Dashboard</b>",
        title_font_size=24,
        showlegend=False,
        height=900,
        width=1600,
        template='plotly_white'
    )
    
    # Save
    print("Saving Future Technology Trends dashboard...")
    fig.write_html(f"{OUTPUT_DIR}dashboard_2_future_tech.html")
    fig.write_image(f"{OUTPUT_DIR}dashboard_2_future_tech.png", width=1600, height=900)
    print("✅ Future Technology Trends dashboard saved!")
    
    return fig

# ============================================================================
# DASHBOARD 3: DEMOGRAPHICS
# ============================================================================

def create_demographics_dashboard(df):
    """Create Demographics dashboard with 4-5 panels."""
    print("\n" + "="*60)
    print("Creating DEMOGRAPHICS Dashboard")
    print("="*60)
    
    # Create subplots
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=(
            'Respondents by Age Group',
            'Respondent Count by Country (Top 10)',
            'Respondents by Education Level',
            'Respondent Count by Age & Education'
        ),
        specs=[
            [{"type": "pie"}, {"type": "bar"}],
            [{"type": "bar"}, {"type": "bar"}]
        ],
        vertical_spacing=0.15,
        horizontal_spacing=0.12
    )
    
    # Panel 1: Age Distribution (Pie Chart)
    print("Panel 1: Age Distribution...")
    age_counts = df['Age'].value_counts().head(7)
    fig.add_trace(
        go.Pie(
            labels=age_counts.index,
            values=age_counts.values,
            hole=0.3,
            textinfo='label+percent',
            marker=dict(colors=px.colors.sequential.RdBu),
            name='Age'
        ),
        row=1, col=1
    )
    
    # Panel 2: Country Distribution (Map Chart alternative - Bar Chart)
    print("Panel 2: Country Distribution...")
    country_counts = df['Country'].value_counts().head(10)
    fig.add_trace(
        go.Bar(
            y=country_counts.index,
            x=country_counts.values,
            orientation='h',
            marker=dict(color='rgb(231, 76, 60)'),
            text=country_counts.values,
            textposition='outside',
            name='Country'
        ),
        row=1, col=2
    )
    
    # Panel 3: Education Level (Line Chart style - Bar with markers)
    print("Panel 3: Education Level...")
    edu_counts = df['EdLevel'].value_counts().head(8)
    fig.add_trace(
        go.Bar(
            x=list(range(len(edu_counts))),
            y=edu_counts.values,
            marker=dict(color='rgb(142, 68, 173)'),
            text=[f"{x[:30]}..." if len(str(x)) > 30 else x for x in edu_counts.index],
            textposition='outside',
            textangle=-45,
            name='Education'
        ),
        row=2, col=1
    )
    
    # Panel 4: Age by Education (Stacked Bar Chart)
    print("Panel 4: Age by Education...")
    # Create crosstab
    age_edu = pd.crosstab(df['Age'], df['EdLevel'])
    top_edu_levels = df['EdLevel'].value_counts().head(5).index
    
    for edu_level in top_edu_levels:
        if edu_level in age_edu.columns:
            fig.add_trace(
                go.Bar(
                    x=age_edu.index,
                    y=age_edu[edu_level],
                    name=edu_level[:30],
                    text=age_edu[edu_level],
                    textposition='inside',
                    textfont=dict(size=8)
                ),
                row=2, col=2
            )
    
    # Update layout
    fig.update_xaxes(title_text="Count", row=1, col=2)
    fig.update_xaxes(title_text="Education Level", tickangle=45, row=2, col=1)
    fig.update_xaxes(title_text="Age Group", tickangle=45, row=2, col=2)
    
    fig.update_yaxes(title_text="Country", row=1, col=2)
    fig.update_yaxes(title_text="Count", row=2, col=1)
    fig.update_yaxes(title_text="Count", row=2, col=2)
    
    fig.update_layout(
        title_text="<b>Demographics Dashboard</b>",
        title_font_size=24,
        height=900,
        width=1600,
        template='plotly_white',
        barmode='stack',
        showlegend=True,
        legend=dict(orientation="v", yanchor="top", y=0.48, xanchor="left", x=1.02)
    )
    
    # Save
    print("Saving Demographics dashboard...")
    fig.write_html(f"{OUTPUT_DIR}dashboard_3_demographics.html")
    fig.write_image(f"{OUTPUT_DIR}dashboard_3_demographics.png", width=1600, height=900)
    print("✅ Demographics dashboard saved!")
    
    return fig

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("MODULE 05: DASHBOARD CREATION WITH PYTHON")
    print("Creating Professional Dashboards for Employer Showcase")
    print("="*70)
    
    # Load data
    try:
        df = pd.read_csv(DATA_FILE)
        print(f"\n✅ Data loaded successfully: {len(df)} records")
    except FileNotFoundError:
        print(f"\n❌ Error: Could not find {DATA_FILE}")
        print("Please download the survey data first.")
        exit(1)
    
    # Create all dashboards
    dashboard1 = create_current_tech_dashboard(df)
    dashboard2 = create_future_tech_dashboard(df)
    dashboard3 = create_demographics_dashboard(df)
    
    print("\n" + "="*70)
    print("✅ ALL DASHBOARDS CREATED SUCCESSFULLY!")
    print("="*70)
    print(f"\nOutputs saved to: {OUTPUT_DIR}")
    print("\nFiles created:")
    print("  1. dashboard_1_current_tech.html")
    print("  2. dashboard_1_current_tech.png")
    print("  3. dashboard_2_future_tech.html")
    print("  4. dashboard_2_future_tech.png")
    print("  5. dashboard_3_demographics.html")
    print("  6. dashboard_3_demographics.png")
    print("\nNext step: Run pdf_generator.py to create PDF presentation")
    print("="*70)
