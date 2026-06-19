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
    try:
        response = requests.get(
            "https://app.band.ai/api/v1/agent/me",
            headers={
                "X-API-Key": st.secrets["BAND_API_KEY"]
            }
        )

        st.write("Status Code:", response.status_code)
        st.write("Response:", response.text)

    except Exception as e:
        st.error(f"Backend Connection Error: {e}")

# 5. Render the chat history container BELOW the interface
st.markdown("---")  
for msg in st.session_state.messages:
    if msg["role"] == "user":
        ui.show_user_message(msg["content"])
    elif msg["role"] == "assistant":
        ui.show_agent_message(msg["content"])
