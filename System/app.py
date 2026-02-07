import streamlit as st
import pickle
import requests
import base64

# =====================================================
# CONFIG
# =====================================================

API_KEY = ""  # add your own OMDb API key 
POSTER_WIDTH = 180


# =====================================================
# PAGE SETTINGS
# =====================================================

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)


# =====================================================
# BACKGROUND (LOCAL IMAGE + GLASS EFFECT)
# =====================================================

def set_bg(image_file="bg.jpeg"):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        /* glass card */
        div[data-testid="stVerticalBlock"] {{
            background-color: rgba(0,0,0,0.70);
            padding: 25px;
            border-radius: 15px;
        }}

        /* white text */
        h1,h2,h3,h4,h5,h6,p,label {{
            color: white !important;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )


set_bg(r'System/bg.jpeg')


# =====================================================
# LOAD DATA (cached for speed)
# =====================================================

@st.cache_resource
def load_data():
    similarity = pickle.load(open(r'D:\movie-recommender\System\similarity.pkl', "rb"))
    movies = pickle.load(open(r'D:\movie-recommender\System\movies.pkl', "rb"))
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
# POSTER FETCH (cached to avoid API spam)
# =====================================================

@st.cache_data
def get_poster(title):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={title}"
    data = requests.get(url).json()
    return data.get("Poster", "")


# =====================================================
# UI
# =====================================================

st.title("🎬 Movie Recommender System")
st.write("Pick a movie You like and I'll recommend something similar! 😄😄")


selected_movie = st.selectbox("Choose a movie", titles)


if st.button("Recommend"):

    with st.spinner("Finding recommendations..."):
        results = recommend(selected_movie)

    cols = st.columns(5)

    for col, movie in zip(cols, results):
        with col:
            poster = get_poster(movie)
            st.image(poster, width=POSTER_WIDTH)
            st.markdown(
                f"<p style='text-align:center'>{movie}</p>",
                unsafe_allow_html=True
            )
