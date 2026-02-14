import streamlit as st
import base64

def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    if bin_str:
        page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        [data-testid="stHeader"] {{ background-color: rgba(0,0,0,0); }}
        </style>
        """
        st.markdown(page_bg_img, unsafe_allow_html=True)

def get_vinyl_html():
    size = "450px"
    label_size = "150px"
    return f"""
    <div style="display: flex; justify-content: center; align-items: center; padding: 20px 0;">
        <style>
            @keyframes spin {{ from {{ transform: rotate(0deg); }} to {{ transform: rotate(360deg); }} }}
            .vinyl-disk {{
                width: {size}; height: {size}; border-radius: 50%;
                background: conic-gradient(from 0deg, transparent 0deg, rgba(255,255,255,0.05) 45deg, transparent 90deg, rgba(255,255,255,0.05) 135deg, transparent 180deg, rgba(255,255,255,0.05) 225deg, transparent 270deg, rgba(255,255,255,0.05) 315deg, transparent 360deg),
                            repeating-radial-gradient(circle, #111, #111 2px, #1a1a1a 3px, #111 4px);
                box-shadow: 0 0 40px rgba(0,0,0,0.6);
                animation: spin 8s linear infinite;
                display: flex; justify-content: center; align-items: center;
            }}
            .label-red {{
                width: {label_size}; height: {label_size};
                background: radial-gradient(circle, #FA8FBA 0%, #F6C1C7 100%);
                border-radius: 50%; border: 4px solid #000;
                display: flex; justify-content: center; align-items: center;
            }}
            .center-hole {{ width: 15px; height: 15px; background: #222; border-radius: 50%; }}
        </style>
        <div class="vinyl-disk">
            <div class="label-red"><div class="center-hole"></div></div>
        </div>
    </div>
    """

def get_spotify_html():
    src="https://open.spotify.com/embed/playlist/30NW4NAyQhilR8tTpOeaFt?utm_source=generator"
    return f"""
    <div style="width: 100%; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
        <iframe src="{src}" width="100%" height="380" frameBorder="0" 
        allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    </div>
    """

def Playlist():
    set_png_as_page_bg("assets/backGround.png")
    
    vinyl_content = get_vinyl_html()
    spotify_content = get_spotify_html()
    
    full_layout = f"""
    <style>
        .glass-card {{
            background: rgba(255, 255, 255, 0.50);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-radius: 40px;
            border: 1px solid rgba(255, 255, 255, 0.25);
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
            max-width: 600px;
            margin: 20px auto;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px;
        }}
        .title {{
            font-family: 'Cursive', sans-serif;
            color: #ff4b61;
            font-size: 2.2rem;
            text-align: center;
            margin: 0;
            text-shadow: 1px 1px 4px rgba(0,0,0,0.1);
        }}
    </style>
    
    <div class="glass-card">
        <h1 class="title" style="color: hotpink;">The Songs That Remind Me of Us</h1>
        {vinyl_content}
        {spotify_content}
    </div>
    """
    
    # הזרקה אחת ויחידה של הכל למסך
    st.markdown(full_layout, unsafe_allow_html=True)

if __name__ == "__main__":
    Playlist()