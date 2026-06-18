import streamlit as st
import requests
import ui  

# 1. Initialize page configuration FIRST
ui.init_page()

# 2. Initialize chat history in session state if it doesn't exist yet
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Build the core layout
user_message = ui.build_layout()

# 4. Re-draw all previous messages from history so they don't disappear
for msg in st.session_state.messages:
    if msg["role"] == "user":
        ui.show_user_message(msg["content"])
    else:
        ui.show_agent_message(msg["content"])

# 5. Grab your secret password
BAND_API_KEY = st.secrets.get("BAND_API_KEY")

# 6. If the user typed a new message
if user_message:
    # Display and save user message
    ui.show_user_message(user_message)
    st.session_state.messages.append({"role": "user", "content": user_message})
        
    with st.spinner("Agent is thinking..."):
        try:
            url = "https://api.band.ai/v1/chat/completions" 
            headers = {
                "Authorization": f"Bearer {BAND_API_KEY}", 
                "Content-Type": "application/json"
            }
            data = {
                "model": "@20rummy05/head", 
                "messages": st.session_state.messages # Pass full history to the agent!
            }
            
            response = requests.post(url, json=data, headers=headers)
            result = response.json()
            agent_reply = result["choices"][0]["message"]["content"]
            
            # Display and save AI reply
            ui.show_agent_message(agent_reply)
            st.session_state.messages.append({"role": "assistant", "content": agent_reply})
            
        except Exception as e:
            st.error(f"Oops! Something went wrong: {e}")
