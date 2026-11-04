
class CompetitorAgent:

    def recommend_price(self, competitor_price, current_price):

        if current_price > competitor_price:
            recommended_price = competitor_price * 0.98

        elif current_price < competitor_price:
            recommended_price = competitor_price * 1.02

        else:
            recommended_price = current_price

        return round(recommended_price, 2)


if __name__ == "__main__":

    agent = CompetitorAgent()

    price = agent.recommend_price(
        competitor_price=1100,
        current_price=1200
    )

    print("Competitor Agent Recommended Price:", price)

