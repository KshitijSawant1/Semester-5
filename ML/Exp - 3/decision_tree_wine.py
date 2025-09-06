import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_graphviz
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
import pydotplus
from IPython.display import Image, display

# Load the Wine dataset
wine = load_wine()
X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = pd.Series(wine.target)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Create Decision Tree classifier model
clf = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf.fit(X_train, y_train)

# Predict on test data
y_pred = clf.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Basic Tree Plot with light color map using matplotlib
plt.figure(figsize=(20, 10))
plot_tree(
    clf,
    feature_names=wine.feature_names,
    class_names=wine.target_names,
    filled=True,
    rounded=True,
    fontsize=10,
    impurity=False
)
plt.title("Decision Tree - Wine Dataset (Matplotlib)")
plt.show()

# DOT Export for Graphviz with lighter theme
dot_data = export_graphviz(
    clf,
    out_file=None,
    feature_names=wine.feature_names,
    class_names=wine.target_names,
    filled=True,
    rounded=True,
    special_characters=True
)

# Modify DOT data to use lighter fillcolors (optional manual color patch)
# You can replace some default colors like orange/red/blue with light tones
dot_data = dot_data.replace("fillcolor=\"orange\"", "fillcolor=\"#FFEFD5\"")  # papaya whip
dot_data = dot_data.replace("fillcolor=\"lightblue\"", "fillcolor=\"#E0FFFF\"")  # light cyan
dot_data = dot_data.replace("fillcolor=\"yellow\"", "fillcolor=\"#FFFFE0\"")  # light yellow

# Generate and display tree using Graphviz
graph = pydotplus.graph_from_dot_data(dot_data)
display(Image(graph.create_png()))
