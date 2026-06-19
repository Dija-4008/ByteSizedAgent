import streamlit as st
import ui
import requests

# 1. Initialize page configuration FIRST
ui.init_page()

# 2. Initialize chat history array if it doesn't exist yet
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Render landing page layout (Title & Chat input box)
user_query = ui.build_layout()

# 4. Process the backend API call if someone sent a message
if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    
    try:
        # Send the query directly to Groq Cloud's API
        response = requests.get(
            "https://app.band.ai/api/v1/agent/me",
            headers={
                "X-API-Key": st.secrets["BAND_API_KEY"]
            }
        )

st.write(response.status_code)
st.write(response.text)
        result = response.json()
        
        if "choices" in result:
            agent_reply = result["choices"][0]["message"]["content"]
            st.session_state.messages.append({"role": "assistant", "content": agent_reply})
            st.rerun()
        else:
            st.error(f"Groq returned an unexpected structure: {result}")
        
    except Exception as e:
        st.error(f"Backend Connection Error: {e}")

# 5. Render the chat history container BELOW the interface
st.markdown("---")  
for msg in st.session_state.messages:
    if msg["role"] == "user":
        ui.show_user_message(msg["content"])
    elif msg["role"] == "assistant":
        ui.show_agent_message(msg["content"])
