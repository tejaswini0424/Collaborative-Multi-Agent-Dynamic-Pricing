
import numpy as np
from stable_baselines3 import PPO
from environment.pricing_environment import PricingEnvironment

# Load trained reinforcement learning model
model = PPO.load("saved_models/pricing_rl_agent")

# Create pricing environment
env = PricingEnvironment()

# Reset environment
obs, info = env.reset()

total_reward = 0

print("Reinforcement Learning Evaluation Started\n")

# Evaluate for 10 steps
for step in range(10):

    action, _states = model.predict(obs, deterministic=True)

    obs, reward, terminated, truncated, info = env.step(action)

    total_reward += reward

    print(f"Step: {step + 1}")
    print(f"Action: {action}")
    print(f"Reward: {reward}")
    print(f"Updated State: {obs}\n")

    if terminated or truncated:
        obs, info = env.reset()

print("Total Evaluation Reward:", total_reward)
print("\nEvaluation Completed Successfully!")
