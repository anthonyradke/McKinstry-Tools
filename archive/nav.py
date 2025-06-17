import streamlit as st
from archive.siemens_BAS_cleaner import run as run_cleaner
from app_placeholder1 import run as run_tool_1
from app_placeholder2 import run as run_tool_2

st.set_page_config(page_title="McKinstry Tool Suite", layout="wide", page_icon="🛠️")

if "selected_page" not in st.session_state:
    st.session_state.selected_page = "🏠 Home"

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    [data-testid="stSidebar"] {
        width: 280px !important;
        background: rgba(17, 24, 39, 0.95) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
    }

    [data-testid="stSidebar"] > div:first-child {
        background: transparent !important;
    }

    [data-testid="stSidebar"] h1 {
        color: #f1f5f9 !important;
        font-size: 1.3rem !important;
        font-weight: 600 !important;
        margin: 0 0 1rem 0 !important;
        padding: 0 20px !important;
    }

    [data-testid="stSidebar"] .stRadio > div {
        background: transparent !important;
        gap: 4px;
    }

    [data-testid="stSidebar"] .stRadio label {
        background: transparent !important;
        color: rgba(255, 255, 255, 0.88) !important;
        font-weight: 500 !important;
        padding: 10px 16px !important;
        border-radius: 10px !important;
        margin: 2px 0 !important;
        transition: all 0.4s ease !important;
        display: flex !important;
        align-items: center !important;
        width: 220px !important;
        cursor: pointer !important;
    }

    [data-testid="stSidebar"] .stRadio label:hover {
        background: rgba(100, 116, 139, 0.2) !important;
        color: white !important;
        transform: translateX(3px);
    }

    [data-testid="stSidebar"] .stRadio label > div:first-child {
        display: none !important;
    }

    [data-testid="collapsedControl"] {
        position: fixed !important;
        top: 20px !important;
        left: 20px !important;
        z-index: 9999 !important;
        width: 50px !important;
        height: 50px !important;
        background: rgba(30, 41, 59, 0.95) !important;
        border: 2px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 50% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        transition: all 0.5s ease-in-out !important;
    }

    [data-testid="collapsedControl"]:hover {
        transform: scale(1.05);
    }

    [data-testid="collapsedControl"] svg {
        color: white !important;
        width: 24px !important;
        height: 24px !important;
    }

    .hero-section {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        padding: 4rem 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 3rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    }

    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, #ffffff, #94a3b8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
        font-weight: 300;
    }

    .tool-card {
        background: rgba(30, 41, 59, 0.75);
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        border: 1px solid rgba(255, 255, 255, 0.08);
        transition: all 0.4s ease;
        cursor: pointer;
        position: relative;
    }

    .tool-card:hover {
        transform: translateY(-5px);
        background: rgba(51, 65, 85, 0.9);
    }

    .tool-icon {
        font-size: 2.8rem;
        margin-bottom: 0.5rem;
        display: block;
    }

    .tool-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #f8fafc;
        margin-bottom: 0.5rem;
    }

    .tool-description {
        color: #cbd5e1;
        font-size: 0.95rem;
        line-height: 1.5;
    }

    .tool-features {
        list-style: none;
        padding-left: 0;
        margin-top: 1rem;
    }

    .tool-features li::before {
        content: "✓";
        color: #22c55e;
        margin-right: 8px;
    }

    .status-badge {
        display: inline-block;
        font-size: 0.75rem;
        font-weight: 500;
        background: #dcfce7;
        color: #166534;
        padding: 4px 10px;
        border-radius: 999px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("# 🛠️ Navigation")
    st.session_state.selected_page = st.radio(
        "",
        ["🏠 Home", "🧹 Siemens BAS Data Cleaner", "📊 Data Analytics Suite", "⚙️ System Optimizer"],
        index=["🏠 Home", "🧹 Siemens BAS Data Cleaner", "📊 Data Analytics Suite", "⚙️ System Optimizer"].index(st.session_state.selected_page)
    )

if st.session_state.selected_page == "🏠 Home":
    st.title("🛠️ McKinstry Tool Suite")

    st.markdown("""
        <div class="hero-section">
            <div class="hero-title">🛠️ McKinstry Tool Suite</div>
            <div class="hero-subtitle">Streamline your HVAC data processing with our powerful tools</div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧹 Siemens BAS Data Cleaner", use_container_width=True):
            st.session_state.selected_page = "🧹 Siemens BAS Data Cleaner"
    with col2:
        if st.button("📊 Data Analytics Suite", use_container_width=True):
            st.session_state.selected_page = "📊 Data Analytics Suite"

    col3, col4 = st.columns(2)
    with col3:
        if st.button("⚙️ System Optimizer", use_container_width=True):
            st.session_state.selected_page = "⚙️ System Optimizer"
    with col4:
        st.button("📋 Report Generator (Coming Soon)", use_container_width=True, disabled=True)

elif st.session_state.selected_page == "🧹 Siemens BAS Data Cleaner":
    run_cleaner()
elif st.session_state.selected_page == "📊 Data Analytics Suite":
    run_tool_1()
elif st.session_state.selected_page == "⚙️ System Optimizer":
    run_tool_2()
