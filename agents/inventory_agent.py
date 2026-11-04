
class InventoryAgent:

    def recommend_price(self, current_price, inventory):

        if inventory < 50:
            recommended_price = current_price * 1.10

        elif inventory > 300:
            recommended_price = current_price * 0.95

        else:
            recommended_price = current_price

        return round(recommended_price, 2)


if __name__ == "__main__":

    agent = InventoryAgent()

    price = agent.recommend_price(
        current_price=1000,
        inventory=30
    )

    print("Inventory Agent Recommended Price:", price)

