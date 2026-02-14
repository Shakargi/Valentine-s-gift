import streamlit as st
import base64
import os

st.set_page_config(layout="wide", page_title="Valentine's Gift")

from HomePage import show_home_page
from Gallery import show_gallery_page
from Playlist import Playlist as show_playlist_page

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    if os.path.exists(png_file):
        bin_str = get_base64_of_bin_file(png_file)
        page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        [data-testid="stHeader"] {{
            background-color: transparent;
        }}
        </style>
        """
        st.markdown(page_bg_img, unsafe_allow_html=True)

def show_login_page():
    set_background("assets/backGround.png")
    
    st.markdown("""
    <style>
        .login-container {
            background-color: rgba(255, 245, 247, 0.9);
            border: 2px solid #ff4b61;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            text-align: center;
        }
        /* עיצוב כפתור הלוגין */
        div.stButton > button {
            background-color: #ff4b61;
            color: white;
            border-radius: 10px;
            border: none;
            width: 100%;
            font-weight: bold;
            padding: 10px;
        }
        div.stButton > button:hover {
            background-color: #ff1f3a;
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        st.markdown("<h1 style='text-align: center; color: #ff4b61;'>Valentine's Login ❤️</h1>", unsafe_allow_html=True)
        
        with st.container(border=True):
            password = st.text_input("Enter Password", type="password")
            
            if st.button("Log In"):
                if password == "PookieFletset" or password == "1": 
                    st.session_state['logged_in'] = True
                    st.rerun()
                else:
                    st.error("Incorrect Password! Try again 💔")

# --- פונקציה לדף "נתונים אישיים" (Placeholder) ---
def show_personal_data_page():
    # כפתור חזרה
    if st.button("⬅️ Back to Home"):
        st.session_state['page'] = 'home'
        st.rerun()
        
    st.title("About Us ❤️")
    st.write("Here you can add personal letters, stats, or text.")
    # כאן תוכל להוסיף את התוכן האמיתי כשתכתוב אותו

# --- ה-Router הראשי (מנהל את התצוגה) ---
def main():
    # 1. אם לא מחובר -> הצג מסך התחברות
    if not st.session_state['logged_in']:
        show_login_page()
        
    # 2. אם מחובר -> בדוק באיזה דף אנחנו נמצאים
    else:
        # כפתור צף קטן לחזרה לבית (אופציונלי, קיים גם בתוך הדפים)
        # st.sidebar.button("Home", on_click=lambda: st.session_state.update(page='home'))

        if st.session_state['page'] == 'home':
            show_home_page()
            
        elif st.session_state['page'] == 'gallery':
            # בתוך הגלריה הוספנו כפתור חזרה בקוד הקודם, 
            # אבל אם חסר שם, הוסף: if st.button("Back"): st.session_state['page']='home'; st.rerun()
            show_gallery_page()
            # כפתור חזרה ידני למקרה שאין בתוך הקובץ
            if st.sidebar.button("⬅️ Back to Home"):
                st.session_state['page'] = 'home'
                st.rerun()

        elif st.session_state['page'] == 'playlist':
            show_playlist_page()
            # כפתור חזרה
            if st.sidebar.button("⬅️ Back to Home"):
                st.session_state['page'] = 'home'
                st.rerun()

        elif st.session_state['page'] == 'personal_data':
            show_personal_data_page()

if __name__ == "__main__":
    main()
