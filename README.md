# Retail AI — Decision Intelligence Platform

Retail AI is a **data science decision intelligence platform** designed to help retail managers simulate pricing and promotion strategies and identify the most profitable decisions.

The system combines **machine learning, simulation, optimization, and interactive dashboards** to support retail strategy planning.

---

## Features

• Demand forecasting using machine learning
• Promotion impact simulation
• Inventory optimization
• Profitability analysis
• Interactive decision dashboard

---

## Architecture

The platform consists of four main components:

```
Machine Learning Model
        ↓
Demand Forecast
        ↓
Promotion Simulation
        ↓
Inventory Optimization
        ↓
Strategy Recommendation
```

---

## Project Structure

```
decision-intelligence-platform

api/
    FastAPI backend

src/
    forecasting models
    optimization engine
    simulation engine

dashboards/
    Streamlit analytics dashboard

data/
    raw and processed datasets
```

---

## Technologies Used

Python
FastAPI
Streamlit
XGBoost
OR-Tools
Pandas
Plotly

---

## How to Run

### Start API

```
uvicorn api.app:app --reload
```

### Run Dashboard

```
cd dashboards
streamlit run streamlit_app.py
```

---

## Example Dashboard

Retail managers can:

• simulate pricing strategies
• analyze promotion impact
• optimize inventory decisions
• discover profitable strategies

---

## Author
kishan patel
Data Science Portfolio Project

```
```
