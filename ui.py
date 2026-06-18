import streamlit as st

def init_page():
    """Sets the page title and injects custom CSS to match your exact design."""
    st.set_page_config(page_title="Client Finder", layout="wide")
    
  # Custom CSS strictly forcing the Consolas system font
   # Custom CSS with light green screen and light yellow text
    custom_css = """
    <style>
        /* Hide default Streamlit headers and footers */
        #MainMenu, header, footer {visibility: hidden;}
        
        /* Main page layout - Turns the screen light green */
        .main, .stApp {
            background-color: #e2f0d9 !important; /* Light pastel green screen background */
        }
        
        .main .block-container {
            padding-top: 2rem;
            max-width: 900px;
            margin: 0 auto;
            font-family: 'Times New Roman', Times, serif;
        }
        
        /* Navigation Links at top right */
        .nav-container {
            text-align: right;
            font-size: 1.2rem;
            color: #555555;
            margin-bottom: 5rem;
            font-family: Arial, sans-serif;
        }
        .nav-link {
            margin-left: 20px;
            text-decoration: none;
            color: #555555 !important;
        }
        
        /* Center Title */
        .main-title {
            text-align: center;
            font-size: 5.5rem; 
            font-weight: normal;
            color: #000000;
            line-height: 1.1;
            margin-bottom: 3rem;
        }
        
        /* Centered form container to limit box width */
        .stForm {
            max-width: 680px;  
            margin: 0 auto;
            border: none !important; 
            padding: 0 !important;
            background: transparent !important;
        }
        
        /* The Dark Gray Pill Box with Light Yellow Font */
        .custom-chat-input, 
        .custom-chat-input input, 
        .custom-chat-input textarea {
            width: 100% !important;
            height: 160px !important;       
            background-color: #555555 !important; 
            border: 3.5px solid #000000 !important; 
            border-radius: 45px !important;  
            
            /* Text font colors changed to light yellow */
            color: #ffffcc !important; /* Light yellow typed text */
            
            font-family: 'Times New Roman', Times, serif !important;
            font-weight: bold !important;
            font-size: 1.2rem !important; 
            
            padding: 25px 35px !important;
            outline: none !important;
            box-shadow: 4px 4px 0px #333333, 8px 8px 0px #aaaaaa !important; 
            resize: none !important;
        }
        
        /* Light yellow placeholder text configuration */
        .custom-chat-input::placeholder,
        .custom-chat-input input::placeholder {
            color: #ffffcc !important; /* Light yellow placeholder text */
            opacity: 0.8;
            font-family: 'Times New Roman', Times, serif !important;
            font-weight: bold !important;
        }
    </style>
    """, 
        unsafe_allow_html=True
    )
    
    if submit_button and user_input:
        return user_input
    return None

def show_user_message(text):
    with st.chat_message("user"):
        st.write(text)

def show_agent_message(text):
    with st.chat_message("assistant"):
        st.write(text)
