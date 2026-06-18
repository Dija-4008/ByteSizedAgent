import streamlit as st
import ui
import requests

# 1. Start up your layout rules
ui.init_page()

# 2. Render layout and catch text when submitted
user_query = ui.build_layout()

# 3. Only run the backend API call if someone actually sent a message
if user_query:
    # Save the text in chat history right away so it displays
    st.session_state.messages.append({"role": "user", "content": user_query})
    ui.show_user_message(user_query)
    
    # Send the query to your backend agent server
    try:
        response = requests.post(
            "https://api.band.ai/v1/chat/completions", # Make sure this matches your agent host exactly!
            headers={"Authorization": f"Bearer {st.secrets['API_KEY']}"},
            json={"messages": [{"role": "user", "content": user_query}]}
        )
        
        # Pull response text safely
        agent_reply = response.json()["choices"][0]["message"]["content"]
        
        # Save and show response
        st.session_state.messages.append({"role": "assistant", "content": agent_reply})
        ui.show_agent_message(agent_reply)
        
    except Exception as e:
        st.error(f"Backend Connection Error: {e}")
