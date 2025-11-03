<<<<<<< HEAD
import sys
import os
import pytest
import joblib
import pandas as pd

# Add parent directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_validation import load_data, validate_data 
from src.evaluate import evaluate_model


=======
import pytest
import pandas as pd
import joblib
from src.data_validation import load_data, validate_data
from src.evaluate import evaluate_model

>>>>>>> 5125f68 (Initial setup with CI and tests updated)
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
