import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Load the Iris dataset
iris_df = pd.read_csv("iris_dataset.csv")

print(iris_df)

X, y = iris_df.drop("target", axis=1), iris_df.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create a pipeline
pipeline = Pipeline(
    [
        ("scaler", StandardScaler()),  # Standardize features
        (
            "classifier",
            RandomForestClassifier(n_estimators=100),
        ),  # Random Forest classifier
    ]
)

# Fit the pipeline on the training data
pipeline.fit(X_train, y_train)

# Save the pipeline to a file
joblib.dump(pipeline, "saved_iris_pipeline.pkl")
