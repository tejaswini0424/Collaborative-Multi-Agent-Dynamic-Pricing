
from stable_baselines3 import PPO
from pathlib import Path
from environment.pricing_environment import PricingEnvironment

# Create pricing environment
env = PricingEnvironment()

# Create PPO reinforcement learning model
model = PPO(
    "MlpPolicy",
    env,
    verbose=1,
    learning_rate=0.0003,
    n_steps=256,
    batch_size=64,
    gamma=0.99
)

# Train the agent
print("Training Reinforcement Learning Agent...")

model.learn(total_timesteps=10000)

# Save trained model
BASE_DIR = Path(__file__).resolve().parent.parent
model_folder = BASE_DIR / "saved_models"
model_folder.mkdir(exist_ok=True)

model.save(model_folder / "pricing_rl_agent")

print("Reinforcement Learning Agent Trained Successfully!")
print("Model saved successfully!")
