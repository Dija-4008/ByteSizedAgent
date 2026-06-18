import streamlit as st
import ui
import requests

# 1. Initialize page configuration FIRST
ui.init_page()

# 2. CRITICAL: Initialize chat history array if it doesn't exist yet
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Render layout and catch text when submitted
user_query = ui.build_layout()

# 4. Only run the backend API call if someone actually sent a message
if user_query:
    # This will now work perfectly because 'messages' is guaranteed to exist!
    st.session_state.messages.append({"role": "user", "content": user_query})
    ui.show_user_message(user_query)
    
    # Send the query to your backend agent server
    try:
        response = requests.post(
            "https://api.band.ai/v1/chat/completions",
            headers={"Authorization": f"Bearer {st.secrets['BAND_API_KEY']}"},
            json={"model": "@20rummy05/head", "messages": [{"role": "user", "content": user_query}]}
        )
        
        # Pull response text safely
        result = response.json()
        agent_reply = result["choices"][0]["message"]["content"]
        
        # Save and show response
        st.session_state.messages.append({"role": "assistant", "content": agent_reply})
        ui.show_agent_message(agent_reply)
        
    except Exception as e:
        st.error(f"Backend Connection Error: {e}")
