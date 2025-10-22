import gradio as gr
import pickle
import numpy as np

# Load your trained model
with open("aqi_model.pkl", "rb") as f:
    model = pickle.load(f)

# Prediction function
def predict_aqi(pm25, pm10, no2, nh3, so2, co, o3):
    features = np.array([[pm25, pm10, no2, nh3, so2, co, o3]])
    prediction = model.predict(features)[0]  # adjust if your model uses predict_proba
    return f"✨ Predicted AQI Category: {prediction}"

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## AQI Predictor")
    
    with gr.Row():
        pm25_input = gr.Number(label="PM2.5")
        pm10_input = gr.Number(label="PM10")
        no2_input = gr.Number(label="NO₂")
    
    with gr.Row():
        nh3_input = gr.Number(label="NH₃")
        so2_input = gr.Number(label="SO₂")
        co_input = gr.Number(label="CO")
        o3_input = gr.Number(label="O₃")
    
    output = gr.Textbox(label="Predicted AQI Category")
    
    btn = gr.Button("Predict")
    btn.click(predict_aqi, 
              inputs=[pm25_input, pm10_input, no2_input, nh3_input, so2_input, co_input, o3_input], 
              outputs=output)

demo.launch()
