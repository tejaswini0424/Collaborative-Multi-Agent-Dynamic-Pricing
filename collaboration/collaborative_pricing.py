
import numpy as np
from pathlib import Path

from stable_baselines3 import PPO

from agents.demand_agent import DemandAgent
from agents.competitor_agent import CompetitorAgent
from agents.inventory_agent import InventoryAgent


class CollaborativePricing:

    def __init__(self):

        BASE_DIR = Path(__file__).resolve().parent.parent

        self.demand_agent = DemandAgent()
        self.competitor_agent = CompetitorAgent()
        self.inventory_agent = InventoryAgent()

        self.rl_agent = PPO.load(
            BASE_DIR / "saved_models" / "pricing_rl_agent"
        )

    def recommend_final_price(
        self,
        current_price,
        competitor_price,
        inventory,
        marketing_spend
    ):

        # Demand Agent
        predicted_demand = self.demand_agent.predict_demand(
            current_price,
            competitor_price,
            inventory,
            marketing_spend
        )

        # Competitor Agent
        competitor_price_recommendation = (
            self.competitor_agent.recommend_price(
                competitor_price, current_price
            )
        )

        # Inventory Agent
        inventory_price_recommendation = (
            self.inventory_agent.recommend_price(
                current_price, inventory
            )
        )

        # Reinforcement Learning Agent
        state = np.array(
            [current_price, competitor_price, inventory],
            dtype=np.float32
        )

        action, _ = self.rl_agent.predict(
            state, deterministic=True
        )

        if int(action) == 0:
            rl_price = current_price * 0.95
        elif int(action) == 2:
            rl_price = current_price * 1.05
        else:
            rl_price = current_price

        # Combine all pricing recommendations
        final_price = (
            current_price
            + competitor_price_recommendation
            + inventory_price_recommendation
            + rl_price
        ) / 4

        print("\n--- Collaborative Multi-Agent Pricing Results ---")
        print("Predicted Demand:", predicted_demand)
        print("Competitor Recommendation:", competitor_price_recommendation)
        print("Inventory Recommendation:", inventory_price_recommendation)
        print("RL Agent Recommendation:", round(rl_price, 2))
        print("Final Recommended Price:", round(final_price, 2))

        return round(final_price, 2)


if __name__ == "__main__":

    system = CollaborativePricing()

    system.recommend_final_price(
        current_price=1000,
        competitor_price=1100,
        inventory=200,
        marketing_spend=150
    )

