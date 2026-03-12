
import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title("Strategy Lab")

api_url = "http://127.0.0.1:8000/recommend-strategy"

store = st.selectbox("Store",list(range(1,55)))
family = st.selectbox("Product Family",["BEVERAGES","DAIRY","MEATS","PRODUCE"])

min_price = st.slider("Minimum Price",5,20,8)
max_price = st.slider("Maximum Price",5,20,15)

promotion_options = st.multiselect("Promotion Options",[0,1],default=[0,1])

cost = st.slider("Cost",1,10,6)

if st.button("Run Strategy Search"):

    results = []

    for price in range(min_price,max_price+1):

        for promo in promotion_options:

            payload = {
                "store":store,
                "family":family,
                "promotion":promo,
                "price":price,
                "cost":cost
            }

            response = requests.post(api_url,json=payload)

            if response.status_code == 200:

                profit = response.json()["expected_profit"]

                results.append({
                    "Price":price,
                    "Promotion":promo,
                    "Profit":profit
                })

    df = pd.DataFrame(results)

    df = df.sort_values("Profit",ascending=False)

    st.subheader("Top Strategies")

    st.dataframe(df.head(10))

    fig = px.scatter(
        df,
        x="Price",
        y="Profit",
        color="Promotion",
        size="Profit",
        title="Strategy Landscape"
    )

    st.plotly_chart(fig,use_container_width=True)

