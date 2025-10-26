# ==== Imports (Python 3.11/3.12 friendly) ====
import numpy as np
import pandas as pd
from os.path import exists

from sklearn.metrics import mean_squared_error, mean_absolute_error
from catboost import CatBoostRegressor


# ==== Helpers ====
def add_calendar_features(df: pd.DataFrame) -> pd.DataFrame:
    d = df["date"]
    out = pd.DataFrame(index=df.index)
    out["year"] = d.dt.year
    out["month"] = d.dt.month
    out["day"] = d.dt.day
    out["dayofweek"] = d.dt.dayofweek          # 0=Mon
    out["weekofyear"] = d.dt.isocalendar().week.astype(int)
    out["is_weekend"] = (out["dayofweek"] >= 5).astype(int)
    out["month_start"] = (d.dt.day <= 3).astype(int)
    out["month_end"] = (d.dt.days_in_month - d.dt.day <= 3).astype(int)
    return out

def add_group_lags(df: pd.DataFrame, group_cols, target_col="sales",
                   lags=(7, 14, 28), roll_windows=(7, 28)) -> pd.DataFrame:
    """
    Create lag features and rolling means per group (e.g., per store-item).
    Assumes df sorted by date.
    """
    g = df.groupby(group_cols, sort=False)[target_col]
    for lag in lags:
        df[f"lag_{lag}"] = g.shift(lag)
    for w in roll_windows:
        df[f"roll_mean_{w}"] = g.shift(1).rolling(w).mean()
        df[f"roll_std_{w}"] = g.shift(1).rolling(w).std()
    return df


# ==== Load & prepare data ====
df_path = "ML/Exp - 10/train.csv"
if not exists(df_path):
    raise FileNotFoundError(f"File not found: {df_path}")

df = pd.read_csv(df_path)

# Cast types
df["store"] = df["store"].astype(str)
df["item"]  = df["item"].astype(str)
df["date"]  = pd.to_datetime(df["date"])

# Sort by time (critical for lags)
df.sort_values(["store", "item", "date"], inplace=True, ignore_index=True)

# Optional downsample for speed while prototyping
# df = df.sample(n=19_000, random_state=0).sort_values(["store", "item", "date"]).reset_index(drop=True)

# Add features
cal = add_calendar_features(df)
df = pd.concat([df, cal], axis=1)
df = add_group_lags(df, group_cols=["store", "item"], target_col="sales",
                    lags=(7, 14, 28), roll_windows=(7, 28))

# Drop rows that don't have full lag history yet
min_lag = 28
df = df[df["date"] >= (df["date"].min() + pd.Timedelta(days=min_lag))].reset_index(drop=True)

# Time-based split
train = df[df["date"] < "2017-01-01"].copy()
test  = df[df["date"] >= "2017-01-01"].copy()

# Features / target
feature_cols = [
    # identifiers (CatBoost can handle strings directly)
    "store", "item",
    # calendar
    "year", "month", "day", "dayofweek", "weekofyear", "is_weekend", "month_start", "month_end",
    # lags & rolling stats
    "lag_7", "lag_14", "lag_28",
    "roll_mean_7", "roll_std_7",
    "roll_mean_28", "roll_std_28",
]
X_train = train[feature_cols]
y_train = train["sales"]
X_test  = test[feature_cols]
y_test  = test["sales"]

print("Train range:", train["date"].min(), "→", train["date"].max(), f"| rows: {len(train):,}")
print("Test  range:",  test["date"].min(),  "→", test["date"].max(),  f"| rows: {len(test):,}")

# ==== Model: CatBoost (handles string categoricals natively) ====
model = CatBoostRegressor(
    loss_function="RMSE",
    depth=8,
    learning_rate=0.1,
    n_estimators=800,
    random_seed=0,
    verbose=False
)

# Fit
model.fit(X_train, y_train)

# Predict & metrics
pred = model.predict(X_test)
rmse = mean_squared_error(y_test, pred, squared=False)
mae  = mean_absolute_error(y_test, pred)
mape = np.mean(np.abs((y_test - pred) / np.maximum(1e-9, y_test))) * 100

print(f"RMSE: {rmse:.3f} | MAE: {mae:.3f} | MAPE: {mape:.2f}%")
print("Success")
