import streamlit as st
import pandas as pd
import joblib
from utils.data_preprocessing import preprocess_data

# Load trained model
model = joblib.load("model/leak_detection_model.pkl")

st.title("AquaLeak AI – Smart Water Leak Detection")

st.write("Upload your water usage CSV to detect potential leaks.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Uploaded data:")
    st.dataframe(data.head())

    processed_data = preprocess_data(data)
    predictions = model.predict(processed_data)

    data['Leak_Anomaly'] = predictions
    st.write("Detection Results:")
    st.dataframe(data)

    # Highlight anomalies
    anomalies = data[data['Leak_Anomaly'] == -1]
    st.write("Potential leak points detected:")
    st.dataframe(anomalies)
