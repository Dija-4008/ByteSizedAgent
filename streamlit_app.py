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
    # Save the new user message to session state
    st.session_state.messages.append({"role": "user", "content": user_query})
    
    # Send the query directly to OpenAI's server
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {st.secrets['BAND_API_KEY']}"}, 
            json={
                "model": "gpt-4o",  
                "messages": st.session_state.messages 
            }
        )
        
        result = response.json()
        
        if "choices" in result:
            agent_reply = result["choices"][0]["message"]["content"]
            # Save the response
            st.session_state.messages.append({"role": "assistant", "content": agent_reply})
            # Force a rerun to clear the input box and let the message history loop render everything cleanly
            st.rerun()
        else:
            st.error(f"OpenAI returned an unexpected message structure: {result}")
        
    except Exception as e:
        st.error(f"Backend Connection Error: {e}")

# 5. NOW render the chat history container BELOW the interface
# This keeps the history in one clean, un-duplicated block!
st.markdown("---")  # Visual separator line
for msg in st.session_state.messages:
    if msg["role"] == "user":
        ui.show_user_message(msg["content"])
    elif msg["role"] == "assistant":
        ui.show_agent_message(msg["content"])
