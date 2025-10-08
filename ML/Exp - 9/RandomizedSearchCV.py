# randomized_rf_iris.py
import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, StratifiedKFold, RandomizedSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from scipy.stats import randint

# 1) Data
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=42
)

# 2) CV + pipeline (scaling is harmless here; RF doesn't strictly need it)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

rf_pipe = Pipeline([
    ("scaler", StandardScaler(with_mean=False)),   # keep False to avoid warnings on sparse inputs
    ("rf", RandomForestClassifier(random_state=42))
])

# 3) Search space (prefix with step name 'rf__')
param_distributions = {
    "rf__n_estimators": randint(100, 600),
    "rf__max_depth": randint(2, 20),
    "rf__min_samples_split": randint(2, 20),
    "rf__min_samples_leaf": randint(1, 10),
    "rf__max_features": ["sqrt", "log2", None],
    "rf__bootstrap": [True, False],
}

# 4) RandomizedSearchCV
rs = RandomizedSearchCV(
    estimator=rf_pipe,
    param_distributions=param_distributions,
    n_iter=40,                 # budget
    scoring="accuracy",
    cv=cv,
    n_jobs=-1,
    random_state=42,
    verbose=0
)

rs.fit(X_train, y_train)

# 5) Results
print("Best params (Randomized):", rs.best_params_)
print("Best CV score:", round(rs.best_score_, 4))

y_pred = rs.predict(X_test)
print("Test accuracy:", round(accuracy_score(y_test, y_pred), 4))
print(classification_report(y_test, y_pred, target_names=load_iris().target_names))

# (optional) See top candidates
def top_candidates(search, n=5):
    df = pd.DataFrame(search.cv_results_)
    cols = ["rank_test_score", "mean_test_score", "std_test_score", "params"]
    return df[cols].sort_values("rank_test_score").head(n)

print("\nTop candidates:\n", top_candidates(rs, 5))

# (optional) Feature importances from the best RF
best_rf = rs.best_estimator_.named_steps["rf"]
print("\nFeature importances (best RF):", np.round(best_rf.feature_importances_, 3))
