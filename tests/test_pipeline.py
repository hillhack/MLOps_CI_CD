import pytest
import pandas as pd
import joblib
from src.data_validation import load_data, validate_data
from src.evaluate import evaluate_model

@pytest.fixture
def data():
    return load_data("data/iris_data.csv")

@pytest.fixture
def model():
    return joblib.load("models/model.joblib")

def test_data_validation(data):
    assert validate_data(data)

def test_model_accuracy(data):
    acc = evaluate_model("models/model.joblib", data)
    assert acc > 0.7, f"Low model accuracy: {acc}"
