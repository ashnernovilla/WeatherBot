# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 01:46:49 2024

@author: ASHNER_NOVILLA
"""



import requests
from datetime import datetime
import streamlit as st

st.title("Simple Weather :blue[ChatBot] 🤖")

st.caption("This is a simple weather query bot.")
st.caption("Author: Ashner Novilla :sunglasses:")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# When a user submits a prompt
if prompt := st.chat_input("Enter the City Name to Check Weather "):
    # Append user input to chat history
    st.session_state.history.append({"role": "user", "content": prompt})
    
    # Fetch weather data from the API
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={prompt}&appid=79007029562c2ab46617d801d8018750')
    json_data = r.json()
    
    try:
    # Prepare the response text from the weather data
        result = f"The temperature in {json_data['name']} is {round(json_data['main']['temp']-273.15, 2)}°C, but it feels like {round(json_data['main']['feels_like']-273.15, 2)}°C, " \
                 f"having a humidity of {json_data['main']['humidity']}%. The weather condition is {json_data['weather'][0]['description']}, " \
                 f"with sunrise at {(datetime.utcfromtimestamp(json_data['sys']['sunrise'] + json_data['timezone']).strftime('%H:%M:%S'))} " \
                 f"and sunset at {(datetime.utcfromtimestamp(json_data['sys']['sunset'] + json_data['timezone']).strftime('%H:%M:%S'))}."
    
    except:
        result = 'Please enter the country or the city only. Also please check your network connection. '
        pass
    # Append the bot response to the history
    st.session_state.history.append({"role": "assistant", "content": result})

# Display all previous chat messages
for chat in st.session_state.history:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])
