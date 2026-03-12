
import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

api_url = "http://127.0.0.1:8000/recommend-strategy"

# ------------------------------------------------
# HEADER
# ------------------------------------------------

st.title("Strategy Simulator")

st.write(
"""
Simulate pricing and promotion strategies to evaluate demand,
inventory requirements, and expected profit.
"""
)

st.divider()

# ------------------------------------------------
# FILTER BAR
# ------------------------------------------------

st.subheader("Strategy Inputs")

col1, col2, col3, col4, col5 = st.columns(5)

store = col1.selectbox("Store", list(range(1,55)))
family = col2.selectbox(
    "Product Family",
    ["BEVERAGES","DAIRY","MEATS","PRODUCE"]
)
promotion = col3.toggle("Promotion")
price = col4.slider("Price",5,20,10)
cost = col5.slider("Cost",1,10,6)

st.divider()

# ------------------------------------------------
# MODEL PREDICTION
# ------------------------------------------------

payload = {
    "store":store,
    "family":family,
    "promotion":int(promotion),
    "price":price,
    "cost":cost
}

response = requests.post(api_url,json=payload)

if response.status_code == 200:

    data = response.json()

    demand = data["predicted_demand"]
    inventory = data["recommended_inventory"]
    profit = data["expected_profit"]

    # KPI ROW

    st.subheader("Key Metrics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Predicted Demand", round(demand))
    col2.metric("Recommended Inventory", inventory)
    col3.metric("Expected Profit", f"${round(profit)}")

st.divider()

# ------------------------------------------------
# PROFIT VS PRICE ANALYSIS
# ------------------------------------------------

st.subheader("Pricing Analysis")

prices = list(range(5,21))
profits = []

for p in prices:

    payload["price"] = p

    r = requests.post(api_url,json=payload)

    if r.status_code == 200:
        profits.append(r.json()["expected_profit"])
    else:
        profits.append(None)

df = pd.DataFrame({
    "Price":prices,
    "Profit":profits
})

fig = px.line(
    df,
    x="Price",
    y="Profit",
    markers=True,
    title="Profit vs Price Curve"
)

st.plotly_chart(fig,use_container_width=True)

st.divider()

# ------------------------------------------------
# STRATEGY COMPARISON
# ------------------------------------------------

st.subheader("Strategy Comparison")

colA, colB = st.columns(2)

with colA:

    st.write("Strategy A")

    price_A = st.slider("Price A",5,20,10)

    payload_A = {
        "store":store,
        "family":family,
        "promotion":int(promotion),
        "price":price_A,
        "cost":cost
    }

    rA = requests.post(api_url,json=payload_A)

    if rA.status_code == 200:
        profit_A = rA.json()["expected_profit"]
        st.metric("Profit A",f"${round(profit_A)}")

with colB:

    st.write("Strategy B")

    price_B = st.slider("Price B",5,20,12)

    payload_B = {
        "store":store,
        "family":family,
        "promotion":int(promotion),
        "price":price_B,
        "cost":cost
    }

    rB = requests.post(api_url,json=payload_B)

    if rB.status_code == 200:
        profit_B = rB.json()["expected_profit"]
        st.metric("Profit B",f"${round(profit_B)}")
