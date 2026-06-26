# 🎬 Movie Recommendation System

A Content-Based Movie Recommendation System built using Machine Learning and deployed with FastAPI & Jinja2.

The system recommends similar movies based on genres and movie descriptions using Natural Language Processing techniques.

---

## Features

- Content-Based Recommendation
- Movie Search
- Similar Movie Suggestions
- Movie Posters (TMDB API)
- Interactive Web Interface
- FastAPI Deployment
- Jinja2 Templates

---

## Tech Stack

- Python
- Pandas
- Scikit-learn
- CountVectorizer
- Cosine Similarity
- FastAPI
- Jinja2
- HTML
- CSS
- Joblib
- TMDB API

---

## Dataset Features

The recommendation model uses:

- Genre
- Movie Overview
- Original Language

These features are combined into a single text column and transformed into vectors using CountVectorizer.

Similarity between movies is calculated using Cosine Similarity.

---

## Project Structure

```
Movie-Recommendation-System/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── vectorizer.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── notebook.ipynb
│
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/YourUsername/Movie-Recommendation-System.git
```

Go to the project

```bash
cd Movie-Recommendation-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000
```

---

## Example

Input

```
Batman Begins
```

Output

```
The Dark Knight
Batman Forever
Batman Returns
Batman: The Killing Joke
The Dark Knight Rises
```

---

## Machine Learning Pipeline

1. Data Cleaning
2. Feature Engineering
3. Combine Genre + Overview + Language
4. CountVectorizer
5. Cosine Similarity
6. Recommendation Generation
7. FastAPI Deployment

---

## Future Improvements

- Hybrid Recommendation System
- User Rating Based Recommendation
- Collaborative Filtering
- Deep Learning Recommendation
- Search Autocomplete
- Docker Deployment

---

## Author

Shahd Hassan

Machine Learning Engineer
