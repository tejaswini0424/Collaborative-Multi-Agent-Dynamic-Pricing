
import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
BASE_DIR = Path(__file__).resolve().parent.parent
df = pd.read_csv(BASE_DIR / "dataset" / "ecommerce_pricing.csv")

# Select input features
features = [
    "product_price",
    "competitor_price",
    "inventory",
    "marketing_spend"
]

X = df[features]
y = df["units_sold"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train demand prediction model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)

print("Demand Prediction Model Trained Successfully!")
print("Mean Absolute Error:", mean_absolute_error(y_test, predictions))
print("R2 Score:", r2_score(y_test, predictions))

# Save trained model
model_folder = BASE_DIR / "saved_models"
model_folder.mkdir(exist_ok=True)

joblib.dump(model, model_folder / "demand_model.pkl")

print("Model saved successfully!")
