# Collaborative Multi-Agent Reinforcement Learning Framework for Dynamic Pricing in E-Commerce

## Project Overview
This project develops an AI-powered dynamic pricing system using multiple intelligent agents and Reinforcement Learning to recommend optimal product prices in an e-commerce environment.

## Objectives
- Predict customer demand using Machine Learning.
- Analyze competitor pricing.
- Adjust prices based on inventory levels.
- Apply Reinforcement Learning for pricing decisions.
- Combine multiple agents to generate final pricing recommendations.
- Provide predictions through a FastAPI backend and Streamlit dashboard.

## Technologies Used
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Gymnasium
- Stable-Baselines3 (PPO)
- FastAPI
- Streamlit
- Plotly

## Project Modules

1. **Data Preprocessing:** Generates and prepares the e-commerce pricing dataset.
2. **Exploratory Data Analysis:** Analyzes pricing, revenue, demand, and feature correlations.
3. **Demand Prediction:** Uses Random Forest Regression to predict product demand.
4. **Demand Agent:** Predicts demand using the trained model.
5. **Competitor Agent:** Recommends prices based on competitor prices.
6. **Inventory Agent:** Adjusts prices according to inventory levels.
7. **Pricing Environment:** Simulates pricing decisions and rewards.
8. **Reinforcement Learning:** Trains a PPO agent to make pricing decisions.
9. **Collaborative Pricing:** Combines recommendations from multiple agents.
10. **FastAPI Backend:** Provides a pricing prediction API.
11. **Streamlit Dashboard:** Displays dynamic pricing recommendations.

## Dataset
The project uses a generated e-commerce dataset containing:
- Date
- Product ID
- Category
- Product Cost
- Competitor Price
- Inventory
- Marketing Spend
- Product Price
- Units Sold
- Revenue
- Profit

## Model Performance
The Random Forest demand prediction model achieved:

- Mean Absolute Error (MAE): 26.12
- R² Score: 0.6381

## How to Run the Project

### 1. Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### 2. Start FastAPI
```bash
python -m uvicorn backend.main:app --reload
```

### 3. Open API Documentation
http://127.0.0.1:8000/docs

### 4. Start Streamlit Dashboard
Open another terminal and run:
```bash
python -m streamlit run dashboard/app.py
```

## Expected Output
The system provides:
- Predicted product demand.
- Competitor-based pricing recommendations.
- Inventory-based price adjustments.
- Reinforcement Learning pricing decisions.
- Final collaborative price recommendations.
- Interactive dynamic pricing dashboard.

## Future Enhancements
- Integration with real-time e-commerce data.
- Advanced multi-agent reinforcement learning.
- Improved demand forecasting.
- Real-world deployment and monitoring.

## Conclusion
This project demonstrates how Machine Learning, multiple intelligent agents, and Reinforcement Learning can work together to support automated dynamic pricing decisions in e-commerce platforms.