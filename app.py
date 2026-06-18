import streamlit as st
import requests
import ui  # 👈 This imports your layout rules from ui.py!

# 1. Tell ui.py to build the website storefront and listen for an input
user_message = ui.build_layout()

# 2. Grab your secret password
BAND_API_KEY = st.secrets["BAND_API_KEY"]

# 3. If the user typed a message, run the background logic
if user_message:
    # Display what the user typed using the UI file rule
    ui.show_user_message(user_message)
        
    with st.spinner("Agent is thinking..."):
        try:
            url = "https://api.band.ai/v1/chat/completions" 
            headers = {
                "Authorization": f"Bearer {BAND_API_KEY}", 
                "Content-Type": "application/json"
            }
            data = {
                "model": "@20rummy05/head", 
                "messages": [{"role": "user", "content": user_message}]
            }
            
            # Send data to Band.ai
            response = requests.post(url, json=data, headers=headers)
            result = response.json()
            agent_reply = result["choices"][0]["message"]["content"]
            
            # Display the AI reply using the UI file rule
            ui.show_agent_message(agent_reply)
            
        except Exception as e:
            st.error("Oops! Something went wrong connecting to your Band.ai agent.")
