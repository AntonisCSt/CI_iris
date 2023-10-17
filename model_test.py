from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score


def test_answer():
    x = 5
    assert x == 5


def accuracy_calc(X: list[list], y: list, pipeline: any):
    y_pred = pipeline.predict(X)
    accuracy = accuracy_score(y, y_pred)
    return accuracy


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert x.upper() == 'HELLO'


def test_accuracy():
    iris_df = pd.read_csv('iris_dataset.csv')

    X, y = iris_df.drop('target', axis=1), iris_df.target

    # Get the directory of the current script
    current_dir = Path(__file__).resolve().parent

    # Construct the path using pathlib
    saved_pipeline_path = current_dir / 'saved_iris_pipeline.pkl'

    loaded_pipeline = joblib.load(saved_pipeline_path)

    accuracy = accuracy_calc(X[0:5], y[0:5], loaded_pipeline)
    assert accuracy >= 0.8, "Pipeline accuracy should be at least 80%"


# Excercise: add test that checks if there any missing values in the dataset
# Solution:
def test_missing_values():
    # Get the directory of the current script
    current_dir = Path(__file__).resolve().parent

    # Construct the path using pathlib
    iris_path = current_dir / 'iris_dataset.csv'

    iris_df = pd.read_csv(iris_path)

    # add column with nans
    # iris_df['missing_column'] = pd.Series(dtype=float)

    assert iris_df.isnull().values.any() == False
