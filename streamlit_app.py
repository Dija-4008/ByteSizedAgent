import streamlit as st
import ui
import requests

# 1. Initialize page configuration FIRST
ui.init_page()

# 2. Initialize chat history array if it doesn't exist yet
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Re-display past chat messages on every page re-run so they stay visible
for msg in st.session_state.messages:
    if msg["role"] == "user":
        ui.show_user_message(msg["content"])
    elif msg["role"] == "assistant":
        ui.show_agent_message(msg["content"])

# 4. Render layout and catch text when submitted
user_query = ui.build_layout()

# 5. Only run the backend API call if someone actually sent a message
if user_query:
    # Save the new user message to session state and show it right away
    st.session_state.messages.append({"role": "user", "content": user_query})
    ui.show_user_message(user_query)
    
    # Send the query to the platform's API endpoint
    try:
        response = requests.post(
            "https://api.band.ai/v1/chat/completions",  # 👈 The correct machine endpoint for your platform
            headers={"Authorization": f"Bearer {st.secrets['BAND_API_KEY']}"}, 
            json={
                "model": "@20rummy05/head",  # 👈 Your exact Agent Handle goes here!
                "messages": st.session_state.messages # Passes full chat history for context memory
            }
        )
        
        # Pull response text safely
        result = response.json()
        
        if "choices" in result:
            agent_reply = result["choices"][0]["message"]["content"]
            
            # Save and show response
            st.session_state.messages.append({"role": "assistant", "content": agent_reply})
            ui.show_agent_message(agent_reply)
            
            # Force a rerun to clean up the form input box smoothly
            st.rerun()
        else:
            st.error(f"Platform returned an unexpected message structure: {result}")
        
    except Exception as e:
        st.error(f"Backend Connection Error: {e}")
