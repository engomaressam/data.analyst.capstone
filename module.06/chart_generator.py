"""
Module 06: Chart Generator for Final Presentation
==================================================

Generates all required charts for the final presentation:
- Programming languages (current & future)
- Databases (current & future)  
- Job postings analysis
- Dashboard screenshots

Author: Diaa
Date: October 2025
"""

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from collections import Counter
import os

# Configuration
DATA_FILE = '../data/survey_results_updated.csv'
OUTPUT_DIR = './outputs/charts/'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_top_n(series, n=10, split_char=';'):
    """Extract top N items from multi-value columns."""
    all_items = []
    for item in series.dropna():
        if pd.isna(item):
            continue
        if split_char in str(item):
            all_items.extend([x.strip() for x in str(item).split(split_char)])
        else:
            all_items.append(str(item).strip())
    
    counter = Counter(all_items)
    return pd.DataFrame(counter.most_common(n), columns=['Item', 'Count'])

def create_languages_current_chart(df):
    """Slide 6: Top 10 Programming Languages - Current Usage"""
    print("Creating: Programming Languages (Current)...")
    
    lang_data = get_top_n(df['LanguageHaveWorkedWith'], 10)
    
    fig = go.Figure(data=[
        go.Bar(
            y=lang_data['Item'],
            x=lang_data['Count'],
            orientation='h',
            marker=dict(
                color=lang_data['Count'],
                colorscale='Blues',
                showscale=False
            ),
            text=lang_data['Count'],
            textposition='outside',
            textfont=dict(size=12)
        )
    ])
    
    fig.update_layout(
        title='Top 10 Programming Languages - Current Usage',
        xaxis_title='Number of Developers',
        yaxis_title='Programming Language',
        height=600,
        width=1000,
        template='plotly_white',
        font=dict(size=12),
        margin=dict(l=150)
    )
    
    fig.write_image(f'{OUTPUT_DIR}languages_current.png', width=1000, height=600)
    fig.write_html(f'{OUTPUT_DIR}languages_current.html')
    print("  ✓ Saved: languages_current.png")

def create_languages_future_chart(df):
    """Slide 7: Top 10 Programming Languages - Future Trends"""
    print("Creating: Programming Languages (Future)...")
    
    lang_data = get_top_n(df['LanguageWantToWorkWith'], 10)
    
    fig = go.Figure(data=[
        go.Bar(
            y=lang_data['Item'],
            x=lang_data['Count'],
            orientation='h',
            marker=dict(
                color=lang_data['Count'],
                colorscale='Greens',
                showscale=False
            ),
            text=lang_data['Count'],
            textposition='outside',
            textfont=dict(size=12)
        )
    ])
    
    fig.update_layout(
        title='Top 10 Programming Languages - Future Interest',
        xaxis_title='Number of Developers',
        yaxis_title='Programming Language',
        height=600,
        width=1000,
        template='plotly_white',
        font=dict(size=12),
        margin=dict(l=150)
    )
    
    fig.write_image(f'{OUTPUT_DIR}languages_future.png', width=1000, height=600)
    fig.write_html(f'{OUTPUT_DIR}languages_future.html')
    print("  ✓ Saved: languages_future.png")

def create_databases_current_chart(df):
    """Slide 8: Top 10 Databases - Current Usage"""
    print("Creating: Databases (Current)...")
    
    db_data = get_top_n(df['DatabaseHaveWorkedWith'], 10)
    
    fig = go.Figure(data=[
        go.Bar(
            x=db_data['Item'],
            y=db_data['Count'],
            marker=dict(
                color=db_data['Count'],
                colorscale='Oranges',
                showscale=False
            ),
            text=db_data['Count'],
            textposition='outside',
            textfont=dict(size=12)
        )
    ])
    
    fig.update_layout(
        title='Top 10 Databases - Current Usage',
        xaxis_title='Database',
        yaxis_title='Number of Developers',
        height=600,
        width=1000,
        template='plotly_white',
        font=dict(size=12),
        xaxis=dict(tickangle=45)
    )
    
    fig.write_image(f'{OUTPUT_DIR}databases_current.png', width=1000, height=600)
    fig.write_html(f'{OUTPUT_DIR}databases_current.html')
    print("  ✓ Saved: databases_current.png")

def create_databases_future_chart(df):
    """Slide 9: Top 10 Databases - Future Demand"""
    print("Creating: Databases (Future)...")
    
    db_data = get_top_n(df['DatabaseWantToWorkWith'], 10)
    
    fig = go.Figure(data=[
        go.Bar(
            x=db_data['Item'],
            y=db_data['Count'],
            marker=dict(
                color=db_data['Count'],
                colorscale='Purples',
                showscale=False
            ),
            text=db_data['Count'],
            textposition='outside',
            textfont=dict(size=12)
        )
    ])
    
    fig.update_layout(
        title='Top 10 Databases - Future Interest',
        xaxis_title='Database',
        yaxis_title='Number of Developers',
        height=600,
        width=1000,
        template='plotly_white',
        font=dict(size=12),
        xaxis=dict(tickangle=45)
    )
    
    fig.write_image(f'{OUTPUT_DIR}databases_future.png', width=1000, height=600)
    fig.write_html(f'{OUTPUT_DIR}databases_future.html')
    print("  ✓ Saved: databases_future.png")

def create_job_postings_chart():
    """Slide 10: Job Postings Analysis"""
    print("Creating: Job Postings Analysis...")
    
    # Sample job postings data (replace with actual data if available)
    job_data = pd.DataFrame({
        'Technology': ['Python', 'JavaScript', 'Java', 'C#', 'SQL', 'TypeScript', 'Go', 'Rust', 'PHP', 'Swift'],
        'Postings': [12500, 11200, 9800, 8500, 8200, 7600, 5400, 3200, 6700, 4100]
    }).sort_values('Postings', ascending=False)
    
    fig = go.Figure(data=[
        go.Bar(
            x=job_data['Technology'],
            y=job_data['Postings'],
            marker=dict(
                color=job_data['Postings'],
                colorscale='Viridis',
                showscale=False
            ),
            text=job_data['Postings'],
            textposition='outside',
            textfont=dict(size=12)
        )
    ])
    
    fig.update_layout(
        title='Technology Demand in Job Market (Job Postings)',
        xaxis_title='Technology',
        yaxis_title='Number of Job Postings',
        height=600,
        width=1000,
        template='plotly_white',
        font=dict(size=12),
        xaxis=dict(tickangle=45)
    )
    
    fig.write_image(f'{OUTPUT_DIR}job_postings.png', width=1000, height=600)
    fig.write_html(f'{OUTPUT_DIR}job_postings.html')
    print("  ✓ Saved: job_postings.png")

def create_all_charts():
    """Generate all required charts for the presentation"""
    print("\n" + "="*70)
    print("CHART GENERATION FOR FINAL PRESENTATION")
    print("="*70)
    
    try:
        # Check if data file exists
        if not os.path.exists(DATA_FILE):
            print(f"\n⚠️  Warning: Data file not found: {DATA_FILE}")
            print("Creating sample charts with placeholder data...")
            create_job_postings_chart()
            print("\nTo generate real charts:")
            print("  1. Ensure survey_results_updated.csv is in ../data/")
            print("  2. Run this script again")
            return
        
        # Load data
        print(f"\nLoading data from {DATA_FILE}...")
        df = pd.read_csv(DATA_FILE)
        print(f"  ✓ Loaded: {len(df)} records")
        
        # Generate all charts
        create_languages_current_chart(df)
        create_languages_future_chart(df)
        create_databases_current_chart(df)
        create_databases_future_chart(df)
        create_job_postings_chart()
        
        print("\n" + "="*70)
        print("✅ ALL CHARTS GENERATED SUCCESSFULLY")
        print("="*70)
        print(f"\nOutput directory: {os.path.abspath(OUTPUT_DIR)}")
        print("\nGenerated files:")
        print("  • languages_current.png & .html")
        print("  • languages_future.png & .html")
        print("  • databases_current.png & .html")
        print("  • databases_future.png & .html")
        print("  • job_postings.png & .html")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Creating sample charts...")
        create_job_postings_chart()

if __name__ == "__main__":
    create_all_charts()
    print("\nNext: Run final_presentation_generator.py to create the PDF presentation")
