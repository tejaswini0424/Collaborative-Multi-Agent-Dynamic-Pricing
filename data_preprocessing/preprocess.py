
import pandas as pd
import numpy as np
from pathlib import Path

# Generate a reproducible e-commerce dataset
np.random.seed(42)

rows = 2000

categories = ["Electronics", "Clothing", "Home", "Beauty", "Sports"]

df = pd.DataFrame({
    "date": pd.date_range(start="2025-01-01", periods=rows, freq="h"),
    "product_id": np.random.randint(1001, 1021, rows),
    "category": np.random.choice(categories, rows),
    "product_cost": np.random.uniform(100, 2000, rows).round(2),
    "competitor_price": np.random.uniform(150, 3000, rows).round(2),
    "inventory": np.random.randint(20, 500, rows),
    "marketing_spend": np.random.uniform(10, 500, rows).round(2)
})

# Generate selling prices
df["product_price"] = (
    df["product_cost"] * np.random.uniform(1.1, 1.8, rows)
).round(2)

# Simulate customer demand
price_difference = (
    df["competitor_price"] - df["product_price"]
) / df["competitor_price"]

base_demand = np.random.randint(20, 150, rows)

demand = (
    base_demand
    + price_difference * 50
    + df["marketing_spend"] * 0.08
    + np.random.normal(0, 10, rows)
)

df["units_sold"] = np.maximum(
    0,
    np.minimum(demand.astype(int), df["inventory"])
)

# Calculate revenue and profit
df["revenue"] = (
    df["product_price"] * df["units_sold"]
).round(2)

df["profit"] = (
    (df["product_price"] - df["product_cost"])
    * df["units_sold"]
).round(2)

# Save dataset in the dataset folder
project_folder = Path(__file__).resolve().parent.parent
dataset_folder = project_folder / "dataset"
dataset_folder.mkdir(exist_ok=True)

output_file = dataset_folder / "ecommerce_pricing.csv"
df.to_csv(output_file, index=False)

print("E-commerce dataset created successfully!")
print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nDataset saved at:", output_file)

