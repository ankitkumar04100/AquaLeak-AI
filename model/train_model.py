import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
from utils.data_preprocessing import preprocess_data

# Load sample dataset
data = pd.read_csv("../data/sample_usage.csv")
processed_data = preprocess_data(data)

# Train Isolation Forest model
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(processed_data)

# Save trained model
joblib.dump(model, "leak_detection_model.pkl")
print("Model trained and saved successfully!")
