import gradio as gr
import joblib
import numpy as np

# Load the model safely with joblib instead of pickle
model = joblib.load("aqi_model.pkl")

# AQI categories
categories = {
    0: "Good",
    1: "Satisfactory",
    2: "Moderately Polluted",
    3: "Poor",
    4: "Very Poor",
    5: "Severe"
}

# Prediction function
def predict_aqi(city, PM25, PM10, NO2, NH3, SO2, CO, O3):
    features = np.array([[PM25, PM10, NO2, NH3, SO2, CO, O3]])
    prediction = model.predict(features)[0]
    return f"🌆 City: {city}\n✨ Predicted AQI Category: {categories[int(prediction)]}"

# Gradio interface
iface = gr.Interface(
    fn=predict_aqi,
    inputs=[
        gr.Textbox(label="City Name", placeholder="Enter city name"),
        gr.Number(label="PM2.5"),
        gr.Number(label="PM10"),
        gr.Number(label="NO2"),
        gr.Number(label="NH3"),
        gr.Number(label="SO2"),
        gr.Number(label="CO"),
        gr.Number(label="O3"),
    ],
    outputs="text",
    title="🌍 Air Quality Predictor (AQI)",
    description="Predict the air quality category based on pollutant levels across cities."
)

iface.launch(server_name="0.0.0.0", server_port=7860, ssr_mode=True)

