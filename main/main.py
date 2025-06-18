import streamlit as st
import importlib.util
from pathlib import Path



# Configure page
st.set_page_config(
    page_title="McKinstry Data Tools",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)


def load_tool(tool_file):
    """Dynamically load and run a tool"""
    try:
        spec = importlib.util.spec_from_file_location("tool", tool_file)
        tool_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(tool_module)
        tool_module.run()
    except Exception as e:
        st.error(f"Error loading tool: {e}")

def main_navigation():
    # Header section with gradient background
    st.markdown("""
    <div class="header-container">
        <h1 class="main-title">McKinstry Data Tools</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Tools grid
    st.markdown("<div class='tools-grid'>", unsafe_allow_html=True)
    
    # Define available tools
    tools = [
        {
            "name": "Siemens BAS Data Cleaner",
            "description": "Clean and process Siemens BAS CSV exports with timestamp rounding.",
            "file": "siemens_BAS_cleaner.py",
            "status": "active",
            "category": "Data Processing"
        },
        {
            "name": "Placeholder Tool 1",
            "description": "Placeholder description for Tool 1",
            "file": "excel_analyzer.py",
            "status": "coming_soon",
            "category": "Coming Soon"
        },
        {
            "name": "Placeholder Tool 2",
            "description": "Placeholder for Tool 2",
            "file": "time_series_forecaster.py",
            "status": "coming_soon",
            "category": "Coming Soon"
        },
        {
            "name": "Placeholder Tool 3",
            "description": "Placeholder description for Tool 3",
            "file": "db_query_builder.py",
            "status": "coming_soon",
            "category": "Coming Soon"
        }
    ]
    
    # Create tool cards in a responsive grid
    cols = st.columns(2)
    
    for i, tool in enumerate(tools):
        with cols[i % 2]:
            # Tool card container
            status_class = "active" if tool["status"] == "active" else "coming-soon"
            
            card_html = f"""
            <div class="tool-card {status_class}">
                <div class="tool-header">
                    <span class="tool-icon"></span>
                    <div class="tool-meta">
                        <h3 class="tool-name">{tool["name"]}</h3>
                        <span class="tool-category">{tool["category"]}</span>
                    </div>
                </div>
                <p class="tool-description">{tool["description"]}</p>
                <div class="tool-footer">
                    {"<span class='status-badge active'>Available</span>" if tool["status"] == "active" else "<span class='status-badge coming-soon'>Coming Soon</span>"}
                </div>
            </div>
            """
            
            st.markdown(card_html, unsafe_allow_html=True)
            
            # Add button for active tools
            if tool["status"] == "active":
                st.markdown('<div class="tool-launch-button">', unsafe_allow_html=True)
                if st.button(f"Launch {tool['name']}", key=f"launch_{i}", use_container_width=True):
                    st.session_state.current_tool = tool["file"]
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="tool-launch-disabled">', unsafe_allow_html=True)
                st.button("Coming Soon", disabled=True, key=f"disabled_{i}", use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>Made by <a href="https://www.linkedin.com/in/anthonyradke/" target="_blank">Anthony Radke</a></p>
    </div>
    """, unsafe_allow_html=True)

# Main app logic
def main():
    # Custom CSS for modern styling
    st.markdown("""
    <style>
    /* Import modern font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global styles */
    .stApp {
        font-family: 'Inter', sans-serif;
        background-color: #0e1117;
        min-height: 100vh;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Header styling */
    .header-container {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;  /* centers all content horizontally */
        justify-content: center;
        padding: 3rem 0 4rem 0;
        margin-bottom: 2rem;
        text-align: center;
    }


    .main-subtitle {
        font-size: 1.2rem;
        color: #a0aec0;
        font-weight: 300;
        margin-top: 0.5rem;
    }

    .main-title {
        font-size: 3.5rem;
        font-weight: 700;
        color: #fafafa;
        margin-bottom: 0.5rem;
        text-shadow: 0 4px 8px rgba(0,0,0,0.5);
        text-align: center;  /* just in case */
    }

    
    
    /* Tools grid */
    .tools-grid {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
    }
    
    /* Tool cards */
    .tool-card {
        background-color: #262730;
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        border: 1px solid #3d4043;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        height: 240px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .tool-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 48px rgba(0, 0, 0, 0.4);
        border-color: #667eea;
    }
    
    .tool-card.coming-soon {
        opacity: 0.7;
    }
    
    .tool-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #667eea, #764ba2);
    }
    
    /* Tool header */
    .tool-header {
        display: flex;
        align-items: center;
        margin-bottom: 1rem;
    }
        
    .tool-icon {
        font-size: 2.5rem;
        display: inline-block;
        vertical-align: middle;
        margin-right: 1rem;
    }

    .tool-icon:empty {
        margin-right: 0;  /* remove spacing if no icon */
    }

    .tool-meta {
        flex: 1;
    }
    
    .tool-name {
        font-size: 1.4rem;
        font-weight: 600;
        color: #fafafa;
        margin: 0 0 0 0;
    }
    
    .tool-category {
        font-size: 0.85rem;
        color: #667eea;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Tool description */
    .tool-description {
        color: #a0aec0;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 1.5rem;
        flex-grow: 1;
    }

    
    .status-badge {
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .status-badge.active {
        background: linear-gradient(135deg, #48bb78, #38a169);
        color: white;
    }
    
    .status-badge.coming-soon {
        background: #3d4043;
        color: #a0aec0;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 3rem 0 2rem 0;
        margin-top: 3rem;
    }
    
    .footer p {
        color: #a0aec0;
        font-size: 0.9rem;
        margin: 0;
    }
    
    .footer a {
        color: #667eea;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    
    .footer a:hover {
        color: #5a67d8;
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Navigation logic
    if "current_tool" not in st.session_state:
        st.session_state.current_tool = None
    
    if st.session_state.current_tool:
        # Show back button
        st.markdown('<div class="back-button">', unsafe_allow_html=True)
        if st.button("← Back to Tools", key="back_button"):
            st.session_state.current_tool = None
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Load and run the selected tool
        tool_path = Path("main") / st.session_state.current_tool
        if tool_path.exists():
            load_tool(tool_path)
        else:
            st.error(f"Tool file '{st.session_state.current_tool}' not found!")
            if st.button("Return to Main Menu"):
                st.session_state.current_tool = None
                st.rerun()
    else:
        # Show main navigation
        main_navigation()

if __name__ == "__main__":
    main()