import streamlit as st

def init_page():
    """Sets the page title and injects custom CSS to match your exact design."""
    st.set_page_config(page_title="Client Finder", layout="wide")
    
   # Custom CSS with Web Font Import
    custom_css = """
    <style>
        /* Import Cascadia Code/Mono from a public CDN so it loads on ALL devices */
        @import url('https://cdn.jsdelivr.net/npm/@fontsource/cascadia-code/index.css');

        /* Hide default Streamlit headers and footers */
        #MainMenu, header, footer {visibility: hidden;}
        
        /* Main page layout */
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
            color: #777777;
            margin-bottom: 5rem;
            font-family: Arial, sans-serif;
        }
        .nav-link {
            margin-left: 20px;
            text-decoration: none;
            color: #777777 !important;
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
        }
        
        /* The Dark Gray Pill Box with imported font */
        .custom-chat-input {
            width: 100% !important;
            height: 160px !important;       
            background-color: #555555 !important; 
            border: 3.5px solid #000000 !important; 
            border-radius: 45px !important;  
            color: #ffffff !important;
            
            /* Using the imported web font and explicitly setting a light font-weight (300) */
            font-family: "Cascadia Code", "Cascadia Mono", monospace !important;
            font-weight: 300 !important;
            font-size: 1.1rem !important;
            
            padding: 25px 35px !important;
            outline: none !important;
            box-shadow: 4px 4px 0px #333333, 8px 8px 0px #aaaaaa !important; 
            resize: none !important;
        }
        
        /* Style the placeholder text inside the dark box */
        .custom-chat-input::placeholder {
            color: #cccccc !important;
            opacity: 0.8;
            font-family: "Cascadia Code", "Cascadia Mono", monospace !important;
            font-weight: 300 !important;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def build_layout():
    """Draws the custom visual design."""
    # 1. Top Right Links
    st.markdown(
        '<div class="nav-container"><a class="nav-link" href="#">AboutUs</a><a class="nav-link" href="#">FAQ</a></div>', 
        unsafe_allow_html=True
    )
    
    # 2. Main Large Title (Removed the '!' and made it bigger via CSS)
    st.markdown('<div class="main-title">Your next<br>client finder</div>', unsafe_allow_html=True)
    
    # 3. Custom Chat Box using a Streamlit Form to capture the enter key
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input(
            label="", 
            placeholder="Welcome! Type a message to talk to my marketing AI agent...",
            label_visibility="collapsed"
        )
        
        # Hidden submit button so pressing 'Enter' submits the form
        submit_button = st.form_submit_button(label="Send", use_container_width=False)
        
    # Injecting the custom pill shape classes onto the standard input element dynamically
    st.markdown(
        """
        <script>
            var inputs = window.parent.document.getElementsByTagName('input');
            for (var i = 0; i < inputs.length; i++) {
                if (inputs[i].placeholder.startsWith('Welcome!')) {
                    inputs[i].className += ' custom-chat-input';
                    inputs[i].parentElement.className += ' chat-box-container';
                }
            }
        </script>
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
