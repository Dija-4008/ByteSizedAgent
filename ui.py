import streamlit as st

def init_page():
    """Sets the page title and injects custom CSS to match your exact design."""
    st.set_page_config(page_title="Client Finder", page_icon="🤖", layout="wide")
    
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
        
        /* Navigation Links at top right - Updated to bold Times New Roman */
        .nav-container {
            text-align: right;
            font-size: 1.2rem;
            color: #555555;
            margin-bottom: 5rem;
            font-family: 'Times New Roman', Times, serif !important;
            font-weight: bold !important;
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
        
        /* The Dark Gray Pill Box - Increased height to 220px */
        .custom-chat-input, 
        .custom-chat-input input, 
        .custom-chat-input textarea {
            width: 100% !important;
            height: 220px !important;       
            background-color: #555555 !important; 
            border: 3.5px solid #000000 !important; 
            border-radius: 45px !important;  
            
            /* Text font colors changed to light yellow */
            color: #ffffcc !important; 
            
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
            color: #ffffcc !important; 
            opacity: 0.8;
            font-family: 'Times New Roman', Times, serif !important;
            font-weight: bold !important;
        }

        /* Target the Send button to make it a little bit transparent */
        div[data-testid="stFormSubmitButton"] button {
            opacity: 0.6 !important;
            transition: opacity 0.2s ease;
        }
        /* Optional hover effect so users know it's clickable */
        div[data-testid="stFormSubmitButton"] button:hover {
            opacity: 0.9 !important;
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
    
    # 2. Main Large Title
    st.markdown('<div class="main-title" style="font-family: \'Times New Roman\', Times, serif; font-weight: bold;color: #4a2c11;">Your Next<br>Client Finder</div>', unsafe_allow_html=True)    
    # 3. Custom Chat Box using a Streamlit Form to capture the enter key
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input(
            label="Chat Input", 
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
                if (inputs[i].placeholder && inputs[i].placeholder.startsWith('Welcome!')) {
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
