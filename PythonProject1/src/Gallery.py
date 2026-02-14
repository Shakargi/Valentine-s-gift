import streamlit as st
import base64
import os

def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception as e:
        return None

def show_gallery_page():
    # --- 1. מנגנון חכם למציאת הנתיבים ---
    # אנחנו בודקים כמה אופציות נפוצות לנתיב, כדי שזה יעבוד לא משנה מאיפה הרצת את הפרויקט
    possible_image_folders = [
        "assets/pictures",       # מה שהוגדר
        "../assets/pictures",    # רמה אחת אחורה
        "pictures",              # אם התיקייה נקראת פשוט pictures
        "../pictures",           # אם התיקייה pictures נמצאת מחוץ ל-src
        "src/assets/pictures"    # אם מריצים מחוץ ל-src
    ]
    
    possible_backgrounds = [
        "assets/backGround.png",
        "../assets/backGround.png",
        "pictures/backGround.png",
        "../pictures/backGround.png",
        "src/assets/backGround.png"
    ]

    folder_path = None
    for path in possible_image_folders:
        if os.path.exists(path):
            folder_path = path
            break
            
    background_path = None
    for path in possible_backgrounds:
        if os.path.exists(path):
            background_path = path
            break

    # --- 2. טיפול ברקע ---
    if background_path:
        bin_str = get_base64_of_bin_file(background_path)
        if bin_str:
            background_css = f"""
                background-image: url("data:image/png;base64,{bin_str}");
                background-size: cover;
                background-attachment: fixed;
                background-position: center;
                background-repeat: no-repeat;
            """
        else:
            background_css = "background-color: #1e1e1e;"
    else:
        background_css = "background-color: #1e1e1e;"

    # --- 3. הזרקת CSS ---
    st.markdown(
        f"""
        <style>
        .stApp {{
            {background_css}
        }}

        header[data-testid="stHeader"] {{
            background-color: transparent !important;
        }}
        
        .block-container {{
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 100%;
        }}

        .gallery-title {{
            font-family: 'Helvetica Neue', sans-serif;
            color: #FF69B4 !important;
            text-align: center;
            font-size: 4em;
            margin-bottom: 30px;
            font-weight: bold;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.9);
            -webkit-text-stroke: 1px black;
        }}

        div[data-testid="stImage"] img {{
            border-radius: 12px !important;
            transition: all 0.3s ease-in-out !important;
            box-shadow: 0 4px 8px rgba(0,0,0,0.4);
            object-fit: cover !important;
        }}

        div[data-testid="stImage"] img:hover {{
            transform: scale(1.15) !important;
            box-shadow: 0 0 20px rgba(255, 105, 180, 0.9) !important;
            z-index: 9999;
            border: 2px solid #FF69B4;
        }}
        
        @media only screen and (max-width: 768px) {{
            .gallery-title {{ font-size: 2.5em !important; }}
            [data-testid="stHorizontalBlock"] {{ flex-wrap: wrap !important; gap: 10px !important; }}
            [data-testid="column"] {{ flex: 1 1 calc(50% - 20px) !important; min-width: 140px !important; max-width: 50% !important; }}
            div[data-testid="stImage"] img:hover {{ transform: none !important; }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 class="gallery-title">Our Moments</h1>', unsafe_allow_html=True)

    # --- 4. הצגת התמונות או הודעת שגיאה ---
    if not folder_path:
        # הודעת דיבאג שתעזור לנו להבין איפה הבעיה
        st.error("⚠️ לא נמצאה תיקיית תמונות!")
        st.write(f"📂 הנתיב הנוכחי של התוכנה: `{os.getcwd()}`")
        st.write("🔍 ניסיתי לחפש בנתיבים הבאים ולא מצאתי:")
        for p in possible_image_folders:
            st.code(p)
        return

    # אם נמצאה התיקייה, מציגים את התמונות
    num_columns = 6 
    cols = st.columns(num_columns)

    i = 2
    image_found = True
    images_shown = 0

    while image_found:
        filename = f"img ({i}).jpeg"
        filepath = os.path.join(folder_path, filename)

        if os.path.exists(filepath):
            current_col = cols[(i-1) % num_columns]
            with current_col:
                st.image(filepath, use_container_width=True)
            images_shown += 1
            i += 1
        else:
            # אם לא מצאנו את תמונה מס' 1, אולי השמות שונים? ננסה פורמט אחר
            if i == 1:
                st.warning(f"נמצאה התיקייה `{folder_path}` אבל לא נמצא הקובץ `img (1).jpeg` בתוכה.")
                st.write("הקבצים הקיימים בתיקייה הם:")
                st.write(os.listdir(folder_path)[:5]) # מציג את 5 הקבצים הראשונים לבדיקה
            image_found = False

if __name__ == "__main__":
    show_gallery_page()
