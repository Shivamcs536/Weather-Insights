# 🌦️ Weather Insights

A Streamlit web app that delivers real-time weather data and machine-learning-powered forecasts for any city in the world — current conditions, next-day rain prediction, and short-term temperature & humidity trends, complete with interactive visualizations.

**🔗 Live Demo:** [your-app-name.streamlit.app](https://your-app-name.streamlit.app)

---

## Features

- 🌍 **Real-time weather data** for any city, powered by the OpenWeatherMap API
- ☔ **Rain prediction** for tomorrow using a Random Forest classifier trained on historical weather data
- 📈 **Short-term forecasts** for temperature and humidity using Random Forest regression
- 📊 **Interactive graphs** to visualize upcoming trends
- 🖥️ Clean, sidebar-navigated interface built with Streamlit

## Tech Stack

- **Frontend/App:** Streamlit
- **Data & ML:** pandas, NumPy, scikit-learn
- **Visualization:** Matplotlib, Seaborn
- **API:** OpenWeatherMap REST API

## How It Works

1. The app fetches live weather data for a user-entered city via the OpenWeatherMap API.
2. A Random Forest classifier, trained on historical weather records (`weather.csv`), predicts whether it will rain tomorrow.
3. Random Forest regression models forecast how temperature and humidity are likely to trend over the next few hours.
4. Results are displayed as metrics, tables, and charts across four pages: Home, Current Data, Future Temperature & Humidity, and Graphs.

## Running Locally

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/weather-insights.git
cd weather-insights
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your API key**

Create a file at `.streamlit/secrets.toml` with:
```toml
API_KEY = "your_openweathermap_api_key"
```
Get a free key at [openweathermap.org/api](https://openweathermap.org/api).

**4. Run the app**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

## Project Structure

```
weather-insights/
├── app.py              # Streamlit UI and page logic
├── backend.py          # API calls, data prep, and ML models
├── weather.csv          # Historical weather data used for training
├── requirements.txt     # Python dependencies
└── .streamlit/
    └── secrets.toml     # API key (not committed to GitHub)
```

## Notes

- The rain prediction and forecasting models are trained fresh on each request using `weather.csv`, so no pre-trained model files are needed.
- Your API key is kept out of the public repo via Streamlit's secrets management — see the setup step above.

## License

This project is open source and available under the [MIT License](LICENSE).
