"""
train_model.py
---------------
This script trains an ensemble model (SVM + Gradient Boosting) 
on the Iris dataset and saves:
- model.joblib  → Trained ensemble model
- scaler.joblib → StandardScaler used for feature scaling
"""
import os
import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build models
svm_clf = SVC(probability=True, kernel='rbf', C=1.0, gamma='scale', random_state=42)
gb_clf = GradientBoostingClassifier(random_state=42)

# Ensemble using VotingClassifier
ensemble = VotingClassifier(estimators=[
    ('svm', svm_clf),
    ('gb', gb_clf)
], voting='soft')

# Train model
ensemble.fit(X_train_scaled, y_train)

# Evaluate
y_pred = ensemble.predict(X_test_scaled)
acc = accuracy_score(y_test, y_pred)
print(f"✅ Model trained successfully with accuracy: {acc * 100:.2f}%")

# Create directories if they don’t exist
os.makedirs("models", exist_ok=True)
os.makedirs("scaler", exist_ok=True)

# Save model and scaler inside their folders
joblib.dump(ensemble, "models/model.joblib")
joblib.dump(scaler, "scaler/scaler.joblib")

print("💾 model.joblib and scaler.joblib have been saved successfully in their folders!")
