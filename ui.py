import streamlit as st

def init_page():
    """Sets the page title and injects custom CSS to match your exact design."""
    st.set_page_config(page_title="Client Finder", page_icon="🤖", layout="wide")
    
    # Custom CSS to strip standard Streamlit layout and style the UI
    # Custom CSS to match the exact shape and dark gray fill
    custom_css = """
    <style>
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
            font-size: 4.5rem;
            font-weight: normal;
            color: #000000;
            line-height: 1.1;
            margin-bottom: 3rem;
        }
        
        /* Centered form container to limit box width */
        .stForm {
            max-width: 680px;  /* Narrows the box width significantly */
            margin: 0 auto;
            border: none !important; /* Removes Streamlit's default form border */
            padding: 0 !important;
        }
        
        /* The Dark Gray Pill Box */
        .custom-chat-input {
            width: 100% !important;
            height: 160px !important;       /* Made it significantly taller */
            background-color: #555555 !important; /* Darker grey fill */
            border: 3.5px solid #000000 !important; /* Thick crisp outline */
            border-radius: 45px !important;  /* Rounded capsule ends */
            color: #ffffff !important;
            font-family: monospace !important;
            font-size: 1.1rem !important;
            padding: 25px 35px !important;
            outline: none !important;
            
            /* The 3D layered shadow effect from the screenshot */
            box-shadow: 4px 4px 0px #333333, 8px 8px 0px #aaaaaa !important; 
            resize: none !important;
        }
        
        /* Style the placeholder text inside the dark box */
        .custom-chat-input::placeholder {
            color: #cccccc !important;
            opacity: 0.8;
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
        
