import streamlit as st

def init_page():
    """Sets the page title and injects custom CSS to handle your color themes."""
    st.set_page_config(page_title="Client Finder", page_icon="🤖", layout="wide")
    
    # 1. Add a simple Theme Toggle at the top left using Session State
    if "theme" not in st.session_state:
        st.session_state.theme = "Custom Light Green"
        
    # Draw theme buttons at the very top left
    col1, col2, _ = st.columns([1.5, 1.5, 7])
    with col1:
        if st.button("🍃 Light Green"):
            st.session_state.theme = "Custom Light Green"
            st.rerun()
    with col2:
        if st.button("🌙 Night Mode"):
            st.session_state.theme = "Night Mode"
            st.rerun()

    # Determine styles based on chosen theme
    if st.session_state.theme == "Night Mode":
        bg_color = "#121212"
        title_color = "#FFFDD0"  # Creamy title for dark mode
        nav_color = "#888888"
        box_bg = "#222222"
        box_border = "#ffffff"
        text_color = "#ffffff"
        shadow_effect = "4px 4px 0px #444444"
    else:
        # Your classic Custom Light Green Theme configurations
        bg_color = "#99dfa1"
        title_color = "#8B4513"  # Saddle Brown
        nav_color = "#FFFDD0"    # Creamy
        box_bg = "#555555"       # Previous dark gray fill
        box_border = "#000000"
        text_color = "#ffffff"   # White text
        shadow_effect = "4px 4px 0px #333333, 8px 8px 0px #aaaaaa"

    custom_css = f"""
    <style>
        /* Hide default Streamlit headers and footers */
        #MainMenu, header, footer {{visibility: hidden;}}
        
        /* Application Background Color */
        .main, .stApp {{
            background-color: {bg_color} !important; 
            transition: background-color 0.3s ease;
        }}
        
        .main .block-container {{
            padding-top: 0.5rem;
            max-width: 1000px; /* Made wider to give you a wide layout */
            margin: 0 auto;
        }}
        
        /* Navigation Links at top right */
        .nav-container {{
            text-align: right;
            font-size: 1.2rem;
            margin-top: -2.5rem; /* Shoved up to balance out the theme buttons */
            margin-bottom: 4rem;
            font-family: Arial, sans-serif;
        }
        .nav-link {{
            margin-left: 20px;
            text-decoration: none;
            color: {nav_color} !important; 
            font-weight: bold;
        }}
        
        /* Center Title - New Elegance with Georgia Font */
        .main-title {{
            text-align: center;
            font-size: 5.5rem; 
            font-family: 'Georgia', serif !important; /* Changed font style */
            font-weight: bold !important;
            color: {title_color} !important; 
            line-height: 1.1;
            margin-bottom: 3rem;
        }}
        
        /* Centered form box wrapper */
        .stForm {{
            max-width: 900px;  /* Expanded container to match wide layout request */
            margin: 0 auto;
            border: none !important; 
            padding: 0 !important;
            background: transparent !important;
        }}
        
        /* Wide Custom Chat Box Container */
        .custom-chat-input, 
        .custom-chat-input input, 
        .custom-chat-input textarea {{
            width: 100% !important;
            height: 140px !important;       
            background-color: {box_bg} !important; 
            border: 3.5px solid {box_border} !important; 
            border-radius: 40px !important;  
            
            /* Text changed to clean white, small and Times New Roman */
            color: {text_color} !important; 
            font-family: 'Times New Roman', Times, serif !important;
            font-weight: normal !important;
            font-size: 1.05rem !important; /* Small clean text sizing */
            
            padding: 20px 30px !important;
            outline: none !important;
            box-shadow: {shadow_effect} !important; 
            resize: none !important;
        }}
        
        /* White placeholder formatting */
        .custom-chat-input::placeholder,
        .custom-chat-input input::placeholder {{
            color: #ffffff !important; 
            opacity: 0.75;
            font-family: 'Times New Roman', Times, serif !important;
            font-weight: normal !important;
        }}
        
        /* Send Button returned underneath the chat box */
        .stForm button {{
            display: block !important;
            margin: 20px auto 0 auto !important; /* Centers it smoothly at the bottom */
            background-color: {box_bg} !important;
            color: #ffffff !important;
            border: 3px solid {box_border} !important;
            border-radius: 20px !important;
            font-family: 'Times New Roman', Times, serif !important;
            font-weight: bold !important;
            padding: 10px 30px !important;
            box-shadow: 3px 3px 0px #333333 !important;
            cursor: pointer;
        }}
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def build_layout():
    """Draws the custom visual design."""
    # 1. Top Right Links (Creamy or dark gray depending on theme)
    st.markdown(
        '<div class="nav-container"><a class="nav-link" href="#">AboutUs</a><a class="nav-link" href="#">FAQ</a></div>', 
        unsafe_allow_html=True
    )
    
    # 2. Main Large Title using Georgia font
    st.markdown('<div class="main-title">your next<br>ai finder</div>', unsafe_allow_html=True)
    
    # 3. Custom Chat Box Form
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input(
            label="Chat Input", 
            placeholder="Welcome! Type a message to talk to my marketing AI agent...",
            label_visibility="collapsed"
        )
        
        # Form submit action button positioned at bottom
        submit_button = st.form_submit_button(label="Send")
        
    # Injects styling properties into the native interactive input elements
    st.markdown(
        """
        <script>
            var inputs = window.parent.document.getElementsByTagName('input');
            for (var i = 0; i < inputs.length; i++) {
                if (inputs[i].placeholder && inputs[i].placeholder.startsWith('Welcome!')) {
                    inputs[i].className += ' custom-chat-input';
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
