
import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="AI Dynamic Pricing Dashboard",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Collaborative Multi-Agent Dynamic Pricing")
st.subheader("AI-Powered E-Commerce Pricing System")

st.markdown("---")

st.sidebar.header("Product Information")

current_price = st.sidebar.number_input(
    "Current Product Price",
    min_value=1.0,
    value=1000.0
)

competitor_price = st.sidebar.number_input(
    "Competitor Price",
    min_value=1.0,
    value=1100.0
)

inventory = st.sidebar.number_input(
    "Available Inventory",
    min_value=0,
    value=200
)

marketing_spend = st.sidebar.number_input(
    "Marketing Spend",
    min_value=0.0,
    value=150.0
)

if st.sidebar.button("Predict Optimal Price", type="primary"):

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json={
                "current_price": current_price,
                "competitor_price": competitor_price,
                "inventory": inventory,
                "marketing_spend": marketing_spend
            },
            timeout=30
        )

        if response.status_code == 200:

            result = response.json()

            st.success("Price prediction completed successfully!")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Current Price",
                f"₹{result['current_price']:,.2f}"
            )

            col2.metric(
                "Competitor Price",
                f"₹{result['competitor_price']:,.2f}"
            )

            col3.metric(
                "Recommended Price",
                f"₹{result['predicted_price']:,.2f}",
                delta=round(
                    result["predicted_price"] - result["current_price"],
                    2
                )
            )

            st.markdown("---")

            st.subheader("Pricing Analysis")

            comparison = pd.DataFrame({
                "Price Type": [
                    "Current Price",
                    "Competitor Price",
                    "AI Recommended Price"
                ],
                "Price": [
                    result["current_price"],
                    result["competitor_price"],
                    result["predicted_price"]
                ]
            })

            st.bar_chart(
                comparison,
                x="Price Type",
                y="Price"
            )

            st.subheader("Prediction Details")

            st.write("Inventory:", result["inventory"])
            st.write("Prediction Status:", result["status"])

        else:
            st.error(f"API Error: {response.text}")

    except requests.exceptions.RequestException:
        st.error(
            "Cannot connect to the backend. "
            "Please make sure FastAPI is running."
        )

st.markdown("---")

st.caption(
    "Collaborative Multi-Agent Reinforcement Learning "
    "Framework for Dynamic Pricing in E-Commerce Platforms"
)
