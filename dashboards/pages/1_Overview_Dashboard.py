
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Overview Dashboard")

st.write("High-level analytics of retail strategy performance.")

# Example metrics (can later connect to real data)

col1,col2,col3 = st.columns(3)

col1.metric("Total Stores","54")
col2.metric("Products","33")
col3.metric("Active Promotions","12")

# Example chart

data = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr"],
    "Profit":[20000,24000,22000,26000]
})

fig = px.line(
    data,
    x="Month",
    y="Profit",
    markers=True,
    title="Monthly Profit Trend"
)

st.plotly_chart(fig,use_container_width=True)

