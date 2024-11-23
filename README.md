# WeatherBot
This project is a simple weather chatbot built using Streamlit. It allows users to enter a city name and receive weather information, including the current temperature, humidity, weather conditions, sunrise, and sunset times.

## Features

- Allows users to enter a city name.
- Fetches real-time weather data using the OpenWeatherMap API.
- Displays temperature, humidity, weather condition, sunrise, and sunset times.
- Displays the conversation history with the user and the bot.

## Technologies Used

- **Streamlit**: For creating the web app interface.
- **Requests**: For fetching weather data from the OpenWeatherMap API.
- **OpenWeatherMap API**: Provides real-time weather data.
- **Datetime**: For formatting the sunrise and sunset times.

## Setup

1. Clone the repository or download the files.

2. Create a virtual environment (optional but recommended):
    ```bash
       python -m venv venv
3. Activate the virtual environment:
    ```bash
       .\venv\Scripts\activate
4. Install the dependencies from requirements.txt:
    ```bash
       pip install -r requirements.txt
5. Run the app:
    ```bash
       streamlit run app.py
