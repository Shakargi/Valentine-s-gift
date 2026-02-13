import streamlit as st
import base64


st.session_state.loginState = False

def login():
    set_png_as_page_bg("assets/backGround.png")
    color_container()
    color_button()
    _, col2, _ = st.columns([1, 3, 1])
    with col2:
        st.title(":red[Valentine's Login]", )
    left, mainCol, right = st.columns([2,3,2])
    password = ""
    with st.container(border=True, key="container"):
        password = st.text_input(":red[Password]", type="password")
        st.button("Log In", key="button")



def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)


def color_container():
    login_style = """
    <style>
        .st-key-container{
            background-color: #fff5f7;
            border: 2px solid #ff4b61;
            padding: 30px;
            border-radius: 20px;
        }
    </style>
    """
    st.markdown(login_style, unsafe_allow_html=True)


def color_button():
    login_style = """
        <style>
            .st-key-button{
                background-color: #ff4b61;
                color: white;
                border-radius: 10px;
                border: none;
                width: 100%; 
                height: 3em;
                font-weight: bold;
                transition: 0.1s;
            }
        </style>
        """
    st.markdown(login_style, unsafe_allow_html=True)
login()