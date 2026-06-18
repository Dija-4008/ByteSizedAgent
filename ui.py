import streamlit as st

def build_layout():
    """Draws the main look of your website."""
    st.set_page_config(page_title="Client Finder", page_icon="🤖")
    st.title("Your Next Client finder")
    st.write("Welcome! Type a message below to talk to my marketing AI agent.")
    
    # Draw the chat input box at the bottom and return what the user types
    return st.chat_input(placeholder="Type your question for the agent here...")

def show_user_message(text):
    """Draws the user's chat bubble."""
    with st.chat_message("user"):
        st.write(text)

def show_agent_message(text):
    """Draws the AI agent's chat bubble."""
    with st.chat_message("assistant"):
        st.write(text)
      
