# ---------------------------------------------------------
# model.py (TRAIN + SAVE)
# ---------------------------------------------------------

import pandas as pd
import joblib
import os
from xgboost import XGBRegressor

# Load your walmart dataset
df = pd.read_csv("train.csv")

# Feature engineering
df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["WeekOfYear"] = df["Date"].dt.isocalendar().week
df.drop("Date", axis=1, inplace=True)

# Feature selection
X = df.drop("Weekly_Sales", axis=1)
y = df["Weekly_Sales"]

# Train model
model = XGBRegressor(
    n_estimators=400,
    learning_rate=0.08,
    max_depth=6,
    subsample=0.9,
    colsample_bytree=0.9,
    random_state=42
)
model.fit(X, y)

# Save feature names
feature_columns = list(X.columns)

# Bundle everything
bundle = {
    "model": model,
    "feature_columns": feature_columns
}

# Create model folder if not exists
os.makedirs("model", exist_ok=True)

# Save model
joblib.dump(bundle, "model/model.pkl")

print("✔ Model trained and saved successfully at model/model.pkl")
