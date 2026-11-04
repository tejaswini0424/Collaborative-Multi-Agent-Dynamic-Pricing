
import joblib
import pandas as pd
from pathlib import Path


class DemandAgent:

    def __init__(self):
        BASE_DIR = Path(__file__).resolve().parent.parent
        model_path = BASE_DIR / "saved_models" / "demand_model.pkl"

        self.model = joblib.load(model_path)

    def predict_demand(
        self,
        product_price,
        competitor_price,
        inventory,
        marketing_spend
    ):

        input_data = pd.DataFrame([{
            "product_price": product_price,
            "competitor_price": competitor_price,
            "inventory": inventory,
            "marketing_spend": marketing_spend
        }])

        predicted_demand = self.model.predict(input_data)[0]

        return max(0, round(float(predicted_demand), 2))


if __name__ == "__main__":

    agent = DemandAgent()

    demand = agent.predict_demand(
        product_price=1000,
        competitor_price=1100,
        inventory=200,
        marketing_spend=150
    )

    print("Demand Agent Prediction:", demand)
