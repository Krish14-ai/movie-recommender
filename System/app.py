import streamlit as st
import pickle
import requests
import base64
import random
from pathlib import Path


# =====================================================
# CONFIG
# =====================================================

<<<<<<< HEAD
API_KEY = ""  # add your own OMDb API key 
POSTER_WIDTH = 180
=======
API_KEY = "62f7cb32"
POSTER_WIDTH = 220

BASE_DIR = Path(__file__).parent   # <- magic line (fixes ALL path issues)
>>>>>>> a6b86d4 (add large pickle files via LFS 2)


# =====================================================
# PAGE SETTINGS
# =====================================================

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)


# =====================================================
# BACKGROUND
# =====================================================

def set_bg():
    bg_path = BASE_DIR / "bg.jpeg"

    with open(bg_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>

        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            font-family: "Poppins", sans-serif;
        }}

        div[data-testid="stVerticalBlock"] {{
            background-color: rgba(0,0,0,0.78);
            padding: 24px 28px;
            border-radius: 18px;
            backdrop-filter: blur(8px);
        }}

        h1,h2,h3,h4,h5,h6,p,label,span {{ 
            color: #fdfdfd !important;
        }}

        /* Buttons */
        .stButton>button {{
            background: linear-gradient(135deg, #ff416c, #ff4b2b);
            color: #ffffff;
            border-radius: 999px;
            border: none;
            padding: 0.6rem 1.6rem;
            font-weight: 600;
            letter-spacing: 0.03em;
            box-shadow: 0 10px 25px rgba(0,0,0,0.35);
            transition: transform 0.12s ease-out, box-shadow 0.12s ease-out, filter 0.12s ease-out;
        }}

        .stButton>button:hover {{
            transform: translateY(-1px);
            box-shadow: 0 16px 35px rgba(0,0,0,0.45);
            filter: brightness(1.05);
        }}

        /* Selectbox */
        div[data-baseweb="select"]>div {{
            border-radius: 999px !important;
            background-color: rgba(15,15,20,0.86);
            border: 1px solid rgba(255,255,255,0.14);
        }}

        /* Movie cards */
        .movie-card {{
            background: radial-gradient(circle at top left, rgba(255,255,255,0.12), rgba(0,0,0,0.75));
            border-radius: 18px;
            padding: 10px 10px 14px;
            box-shadow: 0 12px 28px rgba(0,0,0,0.7);
            border: 1px solid rgba(255,255,255,0.09);
            transition: transform 0.15s ease-out, box-shadow 0.15s ease-out, border-color 0.15s ease-out;
        }}

        .movie-card:hover {{
            transform: translateY(-4px) scale(1.01);
            box-shadow: 0 16px 40px rgba(0,0,0,0.9);
            border-color: rgba(255,255,255,0.25);
        }}

        .movie-title {{
            font-weight: 600;
            font-size: 0.96rem;
            text-align: center;
            margin-top: 6px;
        }}

        .movie-meta {{
            font-size: 0.76rem;
            opacity: 0.85;
            text-align: center;
        }}

        .rating-badge {{
            display: inline-block;
            padding: 2px 9px;
            border-radius: 999px;
            background: rgba(255, 205, 86, 0.15);
            border: 1px solid rgba(255, 205, 86, 0.7);
            font-size: 0.75rem;
            margin-top: 4px;
        }}

        .plot-text {{
            font-size: 0.78rem;
            line-height: 1.35;
            margin-top: 4px;
            opacity: 0.92;
        }}

        /* Sidebar */
        section[data-testid="stSidebar"] {{
            background: rgba(3, 7, 18, 0.94);
            border-right: 1px solid rgba(148,163,184,0.25);
            backdrop-filter: blur(10px);
        }}

        </style>
        """,
        unsafe_allow_html=True
    )


<<<<<<< HEAD
set_bg(r'System/bg.jpeg')
=======
set_bg()
>>>>>>> a6b86d4 (add large pickle files via LFS 2)


# =====================================================
# LOAD DATA
# =====================================================

@st.cache_resource
def load_data():
    with open(BASE_DIR / "similarity.pkl", "rb") as f:
        similarity = pickle.load(f)

    with open(BASE_DIR / "movies.pkl", "rb") as f:
        movies = pickle.load(f)

    return similarity, movies


similarity, movies = load_data()
titles = movies["title"].values


# =====================================================
# RECOMMENDER
# =====================================================

def recommend(movie, k=5):
    idx = movies[movies["title"] == movie].index[0]
    distances = similarity[idx]

    scores = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:k+1]

    return [movies.iloc[i[0]]["title"] for i in scores]


# =====================================================
# POSTER FETCH
# =====================================================

@st.cache_data
def get_movie_details(title):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={title}"
    data = requests.get(url).json()
    return data or {}


# =====================================================
# UI
# =====================================================

st.markdown(
    """
    <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:0.5rem;">
        <span style="font-size:2.2rem;">🎬</span>
        <div>
            <h1 style="margin:0;font-size:2.15rem;">Movie Recommender</h1>
            <p style="margin:0.15rem 0 0;font-size:0.9rem;opacity:0.9;">
                Discover your next favourite film powered by content-based similarity.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")


# Sidebar controls
with st.sidebar:
    st.markdown("### 🎛️ Controls")
    num_recs = st.slider("Number of recommendations", 3, 10, 5)
    show_plot = st.checkbox("Show story overview", value=True)
    show_meta = st.checkbox("Show year, genre & rating", value=True)

    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.write(
        "This app uses a similarity matrix trained on the TMDB dataset and enriches "
        "each recommendation with live details from OMDb (posters, ratings & more)."
    )


st.markdown("#### 1️⃣ Tell us a movie you like")
selected_movie = st.selectbox("Choose a movie", titles)


col_main, col_side = st.columns([3, 1])
with col_main:
    recommend_clicked = st.button("Recommend 🎥")
with col_side:
    surprise_clicked = st.button("Surprise me ✨")


def chunk_list(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i : i + size]


if recommend_clicked or surprise_clicked:

    base_movie = selected_movie
    if surprise_clicked:
        base_movie = random.choice(list(titles))

    st.markdown("#### 2️⃣ Because you liked")

    base_details = get_movie_details(base_movie)
    base_poster = base_details.get("Poster", "")
    base_year = base_details.get("Year", "")
    base_genre = base_details.get("Genre", "")

    base_cols = st.columns([1, 2])
    with base_cols[0]:
        if base_poster and base_poster != "N/A":
            st.image(base_poster, width=POSTER_WIDTH)
    with base_cols[1]:
        meta_bits = " • ".join(
            part for part in [str(base_year or "").strip(), base_genre] if part
        )
        st.markdown(
            f"**{base_movie}**" + (f"  \n*{meta_bits}*" if meta_bits else ""),
        )
        base_plot = base_details.get("Plot", "")
        if base_plot and base_plot != "N/A":
            st.markdown(
                f"<p class='plot-text'>{base_plot}</p>",
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.markdown("#### 3️⃣ You might also enjoy")

    with st.spinner("Finding recommendations..."):
        results = recommend(base_movie, k=num_recs)

    for row in chunk_list(results, 5):
        cols = st.columns(len(row))
        for col, movie in zip(cols, row):
            with col:
                details = get_movie_details(movie)
                poster = details.get("Poster", "")
                year = details.get("Year", "")
                genre = details.get("Genre", "")
                rating = details.get("imdbRating", "N/A")
                plot = details.get("Plot", "")

                with st.container():
                    st.markdown("<div class='movie-card'>", unsafe_allow_html=True)

                    if poster and poster != "N/A":
                        st.image(poster, width=POSTER_WIDTH)

                    st.markdown(
                        f"<div class='movie-title'>{movie}</div>",
                        unsafe_allow_html=True,
                    )

                    if show_meta and (year or genre or rating):
                        meta_parts = []
                        if year:
                            meta_parts.append(str(year))
                        if genre:
                            meta_parts.append(genre.split(",")[0])
                        meta_text = " • ".join(meta_parts)

                        if meta_text:
                            st.markdown(
                                f"<div class='movie-meta'>{meta_text}</div>",
                                unsafe_allow_html=True,
                            )

                        if rating and rating != "N/A":
                            st.markdown(
                                f"<div class='movie-meta'><span class='rating-badge'>⭐ {rating}/10 IMDb</span></div>",
                                unsafe_allow_html=True,
                            )

                    if show_plot and plot and plot != "N/A":
                        st.markdown(
                            f"<div class='plot-text'>{plot}</div>",
                            unsafe_allow_html=True,
                        )

                    st.markdown("</div>", unsafe_allow_html=True)
