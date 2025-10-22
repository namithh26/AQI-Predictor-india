# 🌿 Air Quality Index (AQI) Prediction App

A machine learning project that predicts the **Air Quality Category** of Indian cities based on key pollutants like PM2.5, PM10, NO2, NH3, SO2, CO, and O3.

---

## 🚀 Overview

This project uses real-world air quality data collected from **Kaggle** for **10 major Indian cities**.  
After performing **data cleaning** and **Exploratory Data Analysis (EDA)**, a **Random Forest Classifier** model was trained to predict the AQI category (Good, Satisfactory, Moderate, Poor, Very Poor, Severe).

The app allows users to input pollutant values and get the predicted AQI category instantly.

---

## 🧠 Machine Learning Workflow

1. **Data Collection** – 10 city CSVs from Kaggle  
2. **Data Cleaning & EDA** – handled missing values, visualized distributions  
3. **Feature Selection** – pollutants as features, AQI category as target  
4. **Model Training** – Random Forest Classifier  
5. **Model Evaluation** – Achieved ~99% accuracy  
6. **Deployment** – Built an interactive demo using Gradio and deployed on Hugging Face Spaces  

---

## 🧰 Tech Stack

- **Python**
- **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**
- **Scikit-learn**
- **Joblib / Pickle**
- **Gradio**
- **Google Colab**
- **Hugging Face Spaces**

---

## 💡 Features

✅ Predicts AQI category based on pollutant inputs  
✅ Includes city-based input  
✅ High accuracy Random Forest model  
✅ Simple web interface (Gradio)  
✅ Public demo hosted on Hugging Face  

---

## 🌆 Cities Included

- Delhi  
- Mumbai  
- Chennai  
- Bengaluru  
- Hyderabad  
- Jaipur  
- Kolkata  
- Lucknow  
- Visakhapatnam  
- Gwalior  

---

## 📊 Example Output

| PM2.5 | PM10 | NO2 | NH3 | SO2 | CO | O3 | Predicted Category |
|-------|------|-----|-----|-----|----|----|--------------------|
| 98 | 68 | 120 | 89 | 70 | 135 | 111 | Moderately Polluted |

---

## 🔗 Live Demo

👉 [View on Hugging Face](https://huggingface.co/spaces/Namithh/AQI-Predictor-project)

---

## 👨‍💻 Contributors

- **NAMITHA M**
- **Arshidha Asharaf**
- **Shamna Sherin**
- **Abhinav KV**

---


---

⭐ If you like this project, give it a **star** on GitHub and share it with your peers!
