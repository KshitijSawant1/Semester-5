# train_model.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import sys

THRESHOLD = 0.70
MODEL_PATH = "model.joblib"

def train_and_save_model():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.25, random_state=42, stratify=iris.target
    )

    model = RandomForestClassifier(
        n_estimators=200, random_state=42, n_jobs=-1
    )
    model.fit(X_train, y_train)

    acc = model.score(X_test, y_test)
    print(f"Test Accuracy: {acc:.4f}")

    if acc < THRESHOLD:
        print(f"Model accuracy below threshold ({THRESHOLD}); failing the pipeline.")
        sys.exit(1)

    joblib.dump(model, MODEL_PATH)
    print(f"Model saved successfully at: {MODEL_PATH}")

if __name__ == "__main__":
    train_and_save_model()
