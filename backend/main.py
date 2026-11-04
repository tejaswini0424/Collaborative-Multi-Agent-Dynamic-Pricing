
from fastapi import FastAPI
from pydantic import BaseModel, Field

from collaboration.collaborative_pricing import CollaborativePricing

app = FastAPI(
    title="Collaborative Multi-Agent Dynamic Pricing API",
    description="AI-powered e-commerce dynamic pricing system",
    version="1.0"
)

# Load pricing system
pricing_system = CollaborativePricing()


class PricingRequest(BaseModel):
    current_price: float = Field(gt=0)
    competitor_price: float = Field(gt=0)
    inventory: int = Field(ge=0)
    marketing_spend: float = Field(ge=0)


@app.get("/")
def home():
    return {
        "message": "Collaborative Dynamic Pricing API is running"
    }


@app.post("/predict")
def predict_price(request: PricingRequest):

    final_price = pricing_system.recommend_final_price(
        current_price=request.current_price,
        competitor_price=request.competitor_price,
        inventory=request.inventory,
        marketing_spend=request.marketing_spend
    )

    return {
        "current_price": request.current_price,
        "competitor_price": request.competitor_price,
        "predicted_price": final_price,
        "inventory": request.inventory,
        "status": "success"
    }
