import streamlit as st

def init_page():
    """Sets the page title and injects custom CSS to match your exact design."""
    st.set_page_config(page_title="Client Finder", page_icon="🤖", layout="wide")
    
    # Custom CSS to strip standard Streamlit layout and style the UI
    custom_css = """
    <style>
        /* Hide default Streamlit headers and footers */
        #MainMenu, header, footer {visibility: hidden;}
        .embeddedApp_innerWindow__7w9m4 {background-color: #ffffff;}
        
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
            font-size: 4rem;
            font-weight: normal;
            color: #000000;
            line-height: 1.1;
            margin-bottom: 4rem;
        }
        
        /* Custom Pill Chat Box */
        .chat-box-container {
            display: flex;
            justify-content: center;
            width: 100%;
        }
        
        .custom-chat-input {
            width: 80%;
            height: 140px;
            background-color: #888888;
            border: 3px solid #000000;
            border-radius: 40px;
            color: #ffffff;
            font-family: monospace;
            font-size: 1.1rem;
            padding: 20px 30px;
            outline: none;
            box-shadow: 5px 5px 0px #666666; /* Drop shadow effect */
            resize: none;
        }
        
        .custom-chat-input::placeholder {
            color: #dddddd;
            opacity: 0.9;
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
    
    # 2. Main Large Title (Matches lowercase serif look)
    st.markdown('<div class="main-title">your next<br>client finder!</div>', unsafe_allow_html=True)
    
    # 3. Custom Chat Box using a Streamlit Form to capture the enter key
    with st.form(key="chat_form", clear_on_submit=True):
        # We use a standard text input but wrap it with our CSS classes
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
        
