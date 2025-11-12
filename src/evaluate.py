import joblib
from sklearn.metrics import accuracy_score

def evaluate_model(model_path, data, target_col="species"):
    model = joblib.load(model_path)
    X = data.drop(columns=[target_col])
    y = data[target_col]
    preds = model.predict(X)
    return accuracy_score(y, preds)
