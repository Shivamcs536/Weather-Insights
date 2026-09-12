import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from backend import get_predictions

# Streamlit UI
st.title("🌦️ Weather Insights")

st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Current Data", "Future Temperature & Humidity", "Graphs"])

# Move city input outside so it's available for all sections
st.sidebar.header("Enter City Name")
city = st.sidebar.text_input("City", "Hyderabad")

if page == "Home":
    st.header("Welcome to Weather Insights! 🌍")
    st.write("This app provides real-time weather updates, predicts rain, and forecasts temperature & humidity trends.")
    st.write("### Features:")
    st.markdown("- 🌡️ **Current Weather Data**")
    st.markdown("- ⛈️ **Rain Prediction for Tomorrow**")
    st.markdown("- 📈 **Future Temperature & Humidity Forecasts**")
    st.markdown("- 📊 **Graphs for better visualization**")

elif page == "Current Data":
    if city:
        results = get_predictions(city)
        
        if results:
            weather = results["weather"]
            st.subheader(f"🌍 Weather in {weather['city']}, {weather['country']}")
            st.metric("🌡️ Temperature", f"{weather['current_temp']}°C")
            st.metric("💧 Humidity", f"{weather['humidity']}%")
            st.metric("☁️ Condition", weather['description'].capitalize())
            
            st.subheader("☔ Rain Prediction")
            st.success(f"Will it rain tomorrow? **{results['rain_prediction']}**")
        else:
            st.error("City not found! Please enter a valid city name.")

elif page == "Future Temperature & Humidity":
    if city:
        results = get_predictions(city)
        
        if results:
            future_times = pd.date_range(start=pd.Timestamp.now(), periods=5, freq="h").strftime("%H:%M")
            df_pred = pd.DataFrame({
                "Time ⏳": future_times,
                "Temperature (°C) 🌡️": results["future_temp"],
                "Humidity (%) 💧": results["future_humidity"]
            })
            st.subheader("📅 Future Predictions")
            st.table(df_pred.style.set_properties(**{"font-size": "16px"}))

elif page == "Graphs":
    if city:
        results = get_predictions(city)
        
        if results:
            future_times = pd.date_range(start=pd.Timestamp.now(), periods=5, freq="h").strftime("%H:%M")
            
            # Temperature Line Chart
            fig1, ax1 = plt.subplots(figsize=(5, 3))
            sns.lineplot(x=future_times, y=results["future_temp"], marker="o", color="red", label="Temperature (°C)", ax=ax1)
            plt.xticks(rotation=45)
            plt.xlabel("Time")
            plt.ylabel("Temperature (°C)")
            plt.legend()
            st.pyplot(fig1)
            
            # Humidity Bar Chart
            fig2, ax2 = plt.subplots(figsize=(5, 3))
            sns.barplot(x=future_times, y=results["future_humidity"], ax=ax2, color="skyblue")
            plt.xticks(rotation=45)
            plt.xlabel("Time")
            plt.ylabel("Humidity (%)")
            st.pyplot(fig2)
