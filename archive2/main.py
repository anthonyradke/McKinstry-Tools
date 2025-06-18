import streamlit as st
import importlib
from datetime import datetime
import sys
import os

# Configure the page
st.set_page_config(
    page_title="Tool Hub",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern, sleek design
def inject_css():
    st.markdown("""
    <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* Global styles */
        .main {
            font-family: 'Inter', sans-serif;
        }
        
        /* Hero section */
        .hero {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 3rem 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            text-align: center;
            color: white;
        }
        
        .hero h1 {
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 1rem;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        
        .hero p {
            font-size: 1.2rem;
            font-weight: 300;
            opacity: 0.9;
        }
        
        /* Tool cards */
        .tool-card {
            background: white;
            border-radius: 15px;
            padding: 2rem;
            margin: 1rem 0;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            border: 1px solid #f0f0f0;
            position: relative;
            overflow: hidden;
        }
        
        .tool-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        }
        
        .tool-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        .tool-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1rem;
        }
        
        .tool-title {
            font-size: 1.5rem;
            font-weight: 600;
            color: #2c3e50;
            margin: 0;
        }
        
        .tool-icon {
            font-size: 2rem;
            margin-right: 0.5rem;
        }
        
        .tool-description {
            color: #7f8c8d;
            font-size: 1rem;
            line-height: 1.6;
            margin-bottom: 1.5rem;
        }
        
        .tool-meta {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
        }
        
        .status-badge {
            padding: 0.4rem 1rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .status-available {
            background: #d4edda;
            color: #155724;
        }
        
        .status-progress {
            background: #fff3cd;
            color: #856404;
        }
        
        .status-down {
            background: #f8d7da;
            color: #721c24;
        }
        
        /* Launch button styling - targeting the tool card buttons specifically */
        .tool-card .stButton > button,
        .tool-card button[kind="primary"] {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: white !important;
            border: none !important;
            padding: 0.8rem 2rem !important;
            border-radius: 25px !important;
            font-weight: 500 !important;
            cursor: pointer !important;
            transition: all 0.3s ease !important;
            text-decoration: none !important;
            width: 100% !important;
            height: 45px !important;
        }
        
        .tool-card .stButton > button:hover,
        .tool-card button[kind="primary"]:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3) !important;
            color: white !important;
            text-decoration: none !important;
            background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%) !important;
        }
        
        .tool-card .stButton > button:disabled,
        .tool-card button[kind="primary"]:disabled {
            background: #6c757d !important;
            opacity: 0.5 !important;
            cursor: not-allowed !important;
            transform: none !important;
        }
        
        /* Sidebar styling */
        .stSidebar .stButton > button {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%) !important;
            color: #495057 !important;
            border: 1px solid #dee2e6 !important;
            margin-bottom: 0.5rem !important;
            font-weight: 500 !important;
            border-radius: 8px !important;
            transition: all 0.3s ease !important;
        }
        
        .stSidebar .stButton > button:hover {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: white !important;
            transform: translateX(2px) !important;
        }
        
        .stSidebar .stButton > button:disabled {
            opacity: 0.5 !important;
            background: #6c757d !important;
            color: white !important;
        }
        
        /* Stats section */
        .stats-container {
            display: flex;
            gap: 2rem;
            margin: 2rem 0;
            flex-wrap: wrap;
        }
        
        .stat-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
            text-align: center;
            flex: 1;
            min-width: 200px;
        }
        
        .stat-number {
            font-size: 2.5rem;
            font-weight: 700;
            color: #667eea;
            margin-bottom: 0.5rem;
        }
        
        .stat-label {
            color: #7f8c8d;
            font-weight: 500;
            text-transform: uppercase;
            font-size: 0.9rem;
            letter-spacing: 0.5px;
        }
        
        /* Dark mode support */
        @media (prefers-color-scheme: dark) {
            .tool-card {
                background: #2c3e50;
                border-color: #34495e;
            }
            
            .tool-title {
                color: #ecf0f1;
            }
            
            .tool-description {
                color: #bdc3c7;
            }
            
            .stat-card {
                background: #2c3e50;
            }
        }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'current_tool' not in st.session_state:
    st.session_state.current_tool = None

# Auto-refresh timer for live updates
if 'last_refresh' not in st.session_state:
    st.session_state.last_refresh = datetime.now()

# Check if we need to refresh (every 30 seconds)
if (datetime.now() - st.session_state.last_refresh).seconds > 30:
    st.session_state.last_refresh = datetime.now()
    st.rerun()

# Inject CSS at the beginning of every page load
inject_css()

# Sidebar navigation
with st.sidebar:
    st.markdown("### 🛠️ Navigation")
    
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.current_tool = None
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 📊 Tools")
    
    if st.button("📈 Siemens BAS Cleaner", use_container_width=True):
        st.session_state.current_tool = "siemens_cleaner"
        st.rerun()
    
    if st.button("🔧 Tool 2 (Coming Soon)", use_container_width=True, disabled=True):
        st.session_state.current_tool = "tool2"
    
    if st.button("⚡ Tool 3 (Coming Soon)", use_container_width=True, disabled=True):
        st.session_state.current_tool = "tool3"
    
    st.markdown("---")
    st.markdown("### ℹ️ Info")
    
    # Live updating time using Streamlit's built-in auto-refresh
    current_time = datetime.now().strftime("%H:%M:%S")
    st.write(f"**Current Time:** {current_time}")
    st.write("**Status:** All systems operational")
    
    # Add a small refresh button for manual updates
    if st.button("🔄 Refresh", key="refresh_info", help="Refresh current time"):
        st.rerun()

# Main content area
if st.session_state.current_tool is None:
    # Home page
    st.markdown("""
    <div class="hero">
        <h1>🛠️ Tool Hub</h1>
        <p>Your centralized platform for data processing and automation tools</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats section
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">1</div>
            <div class="stat-label">Active Tools</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">2</div>
            <div class="stat-label">In Development</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">100%</div>
            <div class="stat-label">Uptime</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("## 🔧 Available Tools")
    
    # Tool cards
    tools_data = [
        {
            "icon": "📈",
            "title": "Siemens BAS Data Cleaner",
            "description": "Advanced CSV processing tool for Siemens Building Automation System data. Features timestamp rounding, data consolidation, and multiple export formats with intelligent column naming.",
            "status": "available",
            "status_text": "Available",
            "key": "siemens_cleaner"
        },
        {
            "icon": "🔧",
            "title": "Data Analyzer Pro",
            "description": "Comprehensive data analysis tool with statistical insights, visualization capabilities, and automated reporting features. Perfect for business intelligence and data science workflows.",
            "status": "progress",
            "status_text": "In Development",
            "key": "tool2"
        },
        {
            "icon": "⚡",
            "title": "Automation Suite",
            "description": "Powerful automation toolkit for repetitive tasks, file processing, and workflow optimization. Includes scheduling, monitoring, and notification systems.",
            "status": "progress",
            "status_text": "In Development",
            "key": "tool3"
        }
    ]
    
    for tool in tools_data:
        status_class = f"status-{tool['status']}"
        
        # Create a container for the tool card
        tool_container = st.container()
        
        with tool_container:
            st.markdown(f"""
            <div class="tool-card">
                <div class="tool-header">
                    <div style="display: flex; align-items: center;">
                        <span class="tool-icon">{tool['icon']}</span>
                        <h3 class="tool-title">{tool['title']}</h3>
                    </div>
                    <span class="status-badge {status_class}">{tool['status_text']}</span>
                </div>
                <p class="tool-description">{tool['description']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Add the button directly after the card description, inside the card styling
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if tool['status'] == 'available':
                    if st.button("🚀 Launch Tool", key=f"launch_{tool['key']}", help=f"Launch {tool['title']}", use_container_width=True):
                        st.session_state.current_tool = tool['key']
                        st.rerun()
                else:
                    st.button("🔒 Coming Soon", key=f"disabled_{tool['key']}", disabled=True, use_container_width=True)
            
            # Add some spacing between cards
            st.markdown("<br>", unsafe_allow_html=True)

elif st.session_state.current_tool == "siemens_cleaner":
    # Load the Siemens cleaner tool
    try:
        # Add current directory to Python path if not already there
        current_dir = os.path.dirname(os.path.abspath(__file__))
        if current_dir not in sys.path:
            sys.path.insert(0, current_dir)
        
        # Try different import methods
        try:
            import siemens_BAS_cleaner
            # Check if it has a run function
            if hasattr(siemens_BAS_cleaner, 'run'):
                siemens_BAS_cleaner.run()
            else:
                # If no run function, try to execute the module
                st.error("The siemens_BAS_cleaner module doesn't have a 'run()' function.")
                st.info("Please ensure your siemens_BAS_cleaner.py file has a 'run()' function that contains the Streamlit app code.")
        except ImportError:
            # Try alternative import methods
            try:
                spec = importlib.util.spec_from_file_location("siemens_BAS_cleaner", "siemens_BAS_cleaner.py")
                siemens_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(siemens_module)
                if hasattr(siemens_module, 'run'):
                    siemens_module.run()
                else:
                    st.error("The siemens_BAS_cleaner module doesn't have a 'run()' function.")
            except Exception as e:
                st.error(f"Could not load siemens_BAS_cleaner module: {str(e)}")
                st.info("Please ensure siemens_BAS_cleaner.py is in the same directory as main.py")
                
                # Show current directory contents for debugging
                files = os.listdir('.')
                py_files = [f for f in files if f.endswith('.py')]
                st.write("Python files in current directory:", py_files)
                
    except Exception as e:
        st.error(f"Error loading Siemens BAS Cleaner: {str(e)}")
        st.info("Click 'Home' in the sidebar to return to the main page.")

elif st.session_state.current_tool == "tool2":
    st.title("🔧 Data Analyzer Pro")
    st.info("This tool is currently in development. Check back soon!")
    
elif st.session_state.current_tool == "tool3":
    st.title("⚡ Automation Suite")
    st.info("This tool is currently in development. Check back soon!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #7f8c8d; padding: 2rem 0;">
    <p>Built with ❤️ using Streamlit | © 2024 Tool Hub</p>
</div>
""", unsafe_allow_html=True)