# 🎬 Movie Recommender System

A professional **Machine Learning powered Movie Recommendation Web App** built using **Python, Scikit-learn, and Streamlit**.

This project recommends movies similar to a selected title using **content-based filtering with cosine similarity**, and displays results in a clean **Netflix-style interface with movie posters**.

---

## 👨‍💻 Author

**Krish**  
Engineering Student | Machine Learning Enthusiast  

---

## 🎯 Purpose of this Repository

The goal of this project is to:

- Learn practical Machine Learning workflows
- Build a real-world recommendation system
- Practice data preprocessing & feature engineering
- Create an interactive web app using Streamlit
- Deploy a complete ML project end-to-end
- Showcase a portfolio-ready application

This repository demonstrates how to go from **raw movie metadata → ML model → web app → deployment**.

---

## 🚀 What This App Does

1. User selects a movie  
2. System finds similar movies using cosine similarity  
3. Returns top recommendations  
4. Fetches posters using OMDb API  
5. Displays results in a modern UI  

---

## ✨ Features

- 🎯 Content-based recommendation engine  
- 🎥 Movie posters using OMDb API  
- 🌌 Cinematic background UI  
- ⚡ Fast loading with caching  
- 🖥 Interactive Streamlit web app  
- ☁️ Easy deployment  
- 🧠 Fully offline ML model  

---

## 🧠 How the Recommendation System Works

### Step 1 — Data Preparation
Combine overview, genres, cast, and director into one **tags** column.

### Step 2 — Vectorization
Text → numeric vectors using **CountVectorizer**.

### Step 3 — Similarity
Compute **Cosine Similarity matrix**.

### Step 4 — Recommendation
Sort similarity scores and return top matches.

---

## 🏗 System Architecture

Movie Data → Feature Engineering → Vectorization → Cosine Similarity → Top‑K → Posters → Streamlit UI

---

## 🛠 Tools, Sites, Datasets & Methods Used

### Datasets
- TMDB movie metadata (offline CSV)

### APIs
- OMDb API (movie posters)

### Libraries
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Requests
- Pickle

### Methods
- Text preprocessing
- Bag-of-Words
- CountVectorizer
- Cosine similarity
- Content-based filtering

---

## 📂 Project Structure

movie-recommender/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── bg.jpg
│
└── System/
    ├── movies.pkl
    └── similarity.pkl

---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/movie-recommender.git
cd movie-recommender
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
streamlit run app.py
```

Open:
http://localhost:8501

---

## 🔑 API Setup

Get free OMDb key:
https://www.omdbapi.com/apikey.aspx

Update inside app.py:

API_KEY = "your_key_here"

---

## ☁️ Deployment

Use Streamlit Cloud:
https://share.streamlit.io

Push repo → select app.py → deploy.

---

## 📈 Future Improvements

- Collaborative filtering
- Search autocomplete
- User ratings
- Trending movies
- Trailer integration
- Database backend

---

## 📜 License

MIT License

---

## ⭐ Support

If you found this useful, give it a ⭐ on GitHub!
