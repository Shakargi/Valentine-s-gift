import streamlit as st
import base64
import os

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def show_home_page():
    # --- 1. רקע ---
    background_image_path = "assets/backGround.png"
    
    if os.path.exists(background_image_path):
        bin_str = get_base64_of_bin_file(background_image_path)
        background_css = f"""
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        """
    else:
        background_css = "background-color: #fce4ec;"

    # --- 2. CSS למירכוז מושלם והתאמה לנייד ---
    st.markdown(
        f"""
        <style>
        /* ייבוא פונטים */
        @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

        .stApp {{
            {background_css}
        }}

        header[data-testid="stHeader"] {{
            background-color: transparent !important;
        }}

        /* --- עיצוב הטקסט --- */
        .main-title {{
            font-family: 'Great Vibes', cursive;
            color: #d4af37; /* זהב */
            font-size: 80px; /* גודל גדול למחשב */
            margin-bottom: 0px;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            line-height: 1.2;
            padding-top: 30px;
        }}

        .sub-text {{
            font-family: 'Playfair Display', serif;
            color: #5d4037;
            font-size: 24px;
            font-style: italic;
            text-align: center;
            margin-bottom: 40px;
            text-shadow: 0px 0px 5px rgba(255,255,255,0.8);
        }}

        /* --- מירכוז הכפתורים - הפתרון הסופי --- */
        
        /* מכריח את כל איזור הכפתורים להיות פלקס ולמרכז את התוכן */
        div.stButton {{
            display: flex;
            justify-content: center;
            width: 100%;
        }}

        /* עיצוב הכפתור עצמו */
        div.stButton > button {{
            background-color: rgba(255, 255, 255, 0.9); /* לבן כמעט אטום */
            color: #5d4037;
            border: 2px solid #d4af37;
            border-radius: 50px;
            font-family: 'Playfair Display', serif;
            font-size: 22px;
            padding: 12px 0;
            width: 300px; /* רוחב קבוע בסיסי */
            max-width: 90vw; /* שלא יחרוג מהמסך בפלאפונים צרים */
            transition: all 0.3s ease;
            font-weight: bold;
            margin-top: 15px; /* רווח בין כפתורים */
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        }}

        div.stButton > button:hover {{
            background-color: #d4af37;
            color: white;
            border-color: #d4af37;
            transform: scale(1.05);
            box-shadow: 0 6px 15px rgba(0,0,0,0.25);
        }}

        /* --- התאמה לפלאפון (Mobile Responsive) --- */
        @media only screen and (max-width: 768px) {{
            .main-title {{
                font-size: 50px; /* הקטנת הכותרת בפלאפון */
                padding-top: 20px;
            }}
            
            .sub-text {{
                font-size: 18px;
                margin-bottom: 30px;
            }}
            
            div.stButton > button {{
                width: 250px; /* כפתור קצת יותר צר בפלאפון */
                font-size: 20px;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # --- 3. תוכן הדף ---
    
    # בלי עמודות! פשוט מניחים את האלמנטים וה-CSS ימרכז אותם
    st.markdown('<div class="main-title">Welcome My Love</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-text">To the perfect evening of your life...</div>', unsafe_allow_html=True)
    
    st.write("") # רווח
    
    # הכפתורים - ה-CSS למעלה (display: flex; justify-content: center) דואג למרכז אותם אוטומטית
    if st.button("📸 Our Memories"):
        st.session_state['page'] = 'gallery'
        st.rerun()
        
    if st.button("🎵 Our Vibe"):
        st.session_state['page'] = 'playlist'
        st.rerun()

    if st.button("❤️ About Us"):
        st.session_state['page'] = 'personal_data'
        st.rerun()

if __name__ == "__main__":
    if 'page' not in st.session_state:
        st.session_state['page'] = 'home'
    show_home_page()
