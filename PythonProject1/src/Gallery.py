import streamlit as st
import base64
import os

# 1. חובה: הגדרת הדף לרוחב מלא
st.set_page_config(layout="wide", page_title="Our Gallery")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def show_gallery_page():
    background_image_path = "assets/backGround.png"
    
    # טיפול ברקע
    if os.path.exists(background_image_path):
        bin_str = get_base64_of_bin_file(background_image_path)
        background_css = f"""
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            background-repeat: no-repeat;
        """
    else:
        background_css = "background-color: #1e1e1e;"

    # הזרקת CSS חכם (רספונסיבי)
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
            padding-left: 1rem;
            padding-right: 1rem;
            max-width: 100%;
        }}

        .gallery-title {{
            font-family: 'Helvetica Neue', sans-serif;
            color: #FF69B4 !important;
            text-align: center;
            font-size: 4em; /* גודל למחשב */
            margin-bottom: 30px;
            font-weight: bold;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.9);
            -webkit-text-stroke: 1px black;
        }}

        div[data-testid="stImage"] img {{
            border-radius: 12px !important;
            transition: all 0.3s ease-in-out !important;
            box-shadow: 0 4px 8px rgba(0,0,0,0.4);
            object-fit: cover !important; /* דואג שהתמונה לא תימתח */
        }}

        div[data-testid="stImage"] img:hover {{
            transform: scale(1.15) !important;
            box-shadow: 0 0 20px rgba(255, 105, 180, 0.9) !important;
            z-index: 9999;
            border: 2px solid #FF69B4;
        }}

        
        
        @media only screen and (max-width: 768px) {{
            .gallery-title {{
                font-size: 2.5em !important;
                margin-bottom: 15px;
            }}

            [data-testid="stHorizontalBlock"] {{
                flex-wrap: wrap !important;
                gap: 10px !important;
            }}
            
            [data-testid="column"] {{
                flex: 1 1 calc(50% - 20px) !important;
                min-width: 140px !important;
                max-width: 50% !important;
            }}
            
            div[data-testid="stImage"] img:hover {{
                transform: none !important;
                box-shadow: 0 4px 8px rgba(0,0,0,0.4) !important;
                border: none !important;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 class="gallery-title">Our Moments</h1>', unsafe_allow_html=True)

    folder_path = "assets/pictures"
    

    num_columns = 6 
    cols = st.columns(num_columns)

    i = 1
    image_found = True

    while image_found:
        filename = f"img ({i}).jpeg"
        filepath = os.path.join(folder_path, filename)

        if os.path.exists(filepath):
            # בחירת עמודה
            current_col = cols[(i-1) % num_columns]
            with current_col:
                st.image(filepath, use_container_width=True)
            i += 1
        else:
            image_found = False

if __name__ == "__main__":
    show_gallery_page()
