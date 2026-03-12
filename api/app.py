import sys
import os

# Add project root to path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from fastapi import FastAPI
from pydantic import BaseModel
import joblib

from src.simulation_engine import simulate_promotion
from src.optimization_engine import optimize_inventory
from src.feature_pipeline import create_features


app = FastAPI(title="Decision Intelligence API")


# Load model
MODEL_PATH = os.path.join(ROOT_DIR, "models", "demand_forecast_model.pkl")
model = joblib.load(MODEL_PATH)


class StrategyRequest(BaseModel):
    store: int
    family: str
    promotion: int
    price: float
    cost: float


@app.get("/")
def home():
    return {"message": "Decision Intelligence API running"}


@app.post("/recommend-strategy")
def recommend_strategy(request: StrategyRequest):

    features = create_features(
        store=request.store,
        family=request.family,
        promotion=request.promotion
    )

    base_demand = model.predict(features)[0]

    adjusted_demand = simulate_promotion(
        base_demand,
        request.family,
        request.promotion
    )

    inventory, profit = optimize_inventory(
        adjusted_demand,
        request.price,
        request.cost
    )

    return {
        "predicted_demand": float(adjusted_demand),
        "recommended_inventory": int(inventory),
        "expected_profit": float(profit)
    }