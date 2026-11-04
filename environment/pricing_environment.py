
import gymnasium as gym
from gymnasium import spaces
import numpy as np


class PricingEnvironment(gym.Env):

    def __init__(self):
        super().__init__()

        # State: current price, competitor price, inventory
        self.observation_space = spaces.Box(
            low=np.array([0, 0, 0], dtype=np.float32),
            high=np.array([5000, 5000, 1000], dtype=np.float32),
            dtype=np.float32
        )

        # Actions: decrease, maintain, increase price
        self.action_space = spaces.Discrete(3)

        self.current_price = 1000
        self.competitor_price = 1100
        self.inventory = 200

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.current_price = 1000
        self.competitor_price = 1100
        self.inventory = 200

        state = np.array([
            self.current_price,
            self.competitor_price,
            self.inventory
        ], dtype=np.float32)

        return state, {}

    def step(self, action):

        if action == 0:
            self.current_price *= 0.95

        elif action == 2:
            self.current_price *= 1.05

        demand = max(
            0,
            100 - (self.current_price - self.competitor_price) * 0.05
        )

        units_sold = min(demand, self.inventory)

        reward = units_sold * (self.current_price - 500)

        self.inventory -= units_sold

        terminated = self.inventory <= 0
        truncated = False

        state = np.array([
            self.current_price,
            self.competitor_price,
            self.inventory
        ], dtype=np.float32)

        return state, float(reward), terminated, truncated, {}


if __name__ == "__main__":

    env = PricingEnvironment()

    state, info = env.reset()

    print("Initial State:", state)

    action = 2
    state, reward, terminated, truncated, info = env.step(action)

    print("Next State:", state)
    print("Reward:", reward)
