import streamlit as st

def init_page():
    """This MUST run first before any other Streamlit command."""
    st.set_page_config(page_title="Client Finder", page_icon="🤖")

def build_layout():
    """Draws the main look of your website."""
    st.title("Your Next Client finder")
    st.write("Welcome! Type a message below to talk to my marketing AI agent.")
    return st.chat_input(placeholder="Type your question for the agent here...")

def show_user_message(text):
    with st.chat_message("user"):
        st.write(text)

def show_agent_message(text):
    with st.chat_message("assistant"):
        st.write(text)
        
