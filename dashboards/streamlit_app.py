
import streamlit as st

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="Retail AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------
# GLOBAL STYLE
# ------------------------------------------------

st.markdown("""
<style>

/* Main background */

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg,#eef2f7,#ffffff);
}

/* Sidebar */

[data-testid="stSidebar"] {
    background-color:#111827;
}

/* Sidebar text */

[data-testid="stSidebar"] * {
    color:white;
}

/* Sidebar logo */

.sidebar-title {
    font-size:28px;
    font-weight:700;
}

/* KPI cards */

[data-testid="stMetric"] {
    background:white;
    padding:20px;
    border-radius:10px;
    box-shadow:0 3px 10px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------

st.sidebar.markdown(
"""
<div class="sidebar-title">📊 Retail AI</div>
Decision Intelligence Platform
""",
unsafe_allow_html=True
)

st.sidebar.markdown("---")

st.sidebar.markdown("### Modules")

st.sidebar.page_link(
    "pages/1_Overview_Dashboard.py",
    label="📊 Overview Dashboard"
)

st.sidebar.page_link(
    "pages/2_Strategy_Simulator.py",
    label="🎛 Strategy Simulator"
)

st.sidebar.page_link(
    "pages/3_Strategy_Lab.py",
    label="🧪 Strategy Lab"
)

st.sidebar.page_link(
    "pages/4_AI_Insights.py",
    label="🤖 AI Insights"
)

st.sidebar.markdown("---")

st.sidebar.caption("AI Retail Strategy Platform")

# ------------------------------------------------
# MAIN PAGE
# ------------------------------------------------

st.title("Retail Decision Intelligence Platform")

st.write(
"""
This platform enables **retail managers and analysts** to simulate pricing and promotion strategies,
forecast demand using machine learning, and identify the most profitable inventory decisions.
"""
)

st.divider()

# ------------------------------------------------
# KPI SUMMARY
# ------------------------------------------------

st.subheader("Platform Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Stores Analyzed", "54")
col2.metric("Product Categories", "33")
col3.metric("Decision Engine", "Active")

st.divider()

# ------------------------------------------------
# PLATFORM DESCRIPTION
# ------------------------------------------------

st.subheader("What This Platform Does")

st.write(
"""
This system combines **machine learning, simulation, and optimization** to support retail decision-making.

Capabilities include:

• Demand forecasting using ML models  
• Promotion impact simulation  
• Inventory optimization  
• Profitability analysis  
• Strategy experimentation through an interactive dashboard
"""
)

st.divider()

# ------------------------------------------------
# NAVIGATION GUIDE
# ------------------------------------------------

st.subheader("Platform Modules")

col1, col2 = st.columns(2)

with col1:
    st.info(
        """
📊 **Overview Dashboard**

High-level analytics and retail performance insights.
"""
    )

    st.info(
        """
🎛 **Strategy Simulator**

Test pricing and promotion strategies and see predicted demand and profit.
"""
    )

with col2:
    st.info(
        """
🧪 **Strategy Lab**

Automatically explore multiple pricing strategies and identify the most profitable options.
"""
    )

    st.info(
        """
🤖 **AI Insights**

Understand how the machine learning model makes predictions.
"""
    )

st.success(
"""
Use the **modules in the sidebar** to explore each capability of the platform.
"""
)

