from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
import requests

API_KEY = "b8f830dc551085dd9eec089828098795"

app = FastAPI(
    title="Movie Recommendation System"
)

templates = Jinja2Templates(directory="templates")

movies = joblib.load("movies.pkl")
similarity = joblib.load("similarity.pkl")


def recommend(movie_name):

    movie_name = movie_name.strip()

    movie_index = movies[
        movies["title"].str.lower() == movie_name.lower()
    ].index

    if len(movie_index) == 0:
        return None

    movie_index = movie_index[0]

    distances = sorted(
        list(enumerate(similarity[movie_index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommendations = []

    for movie in distances[1:6]:

        recommendations.append({
    "title": movies.iloc[movie[0]].title,
    "poster": fetch_poster(
        movies.iloc[movie[0]].id
    )
})

    return recommendations


@app.get("/", response_class=HTMLResponse)
def home(request: Request):

   return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={
        "recommendations": None,
        "movie_name": ""
    }
)

@app.post("/", response_class=HTMLResponse)
def get_recommendations(
    request: Request,
    movie_name: str = Form(...)
):

    recommendations = recommend(movie_name)

    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={
        "recommendations": recommendations,
        "movie_name": movie_name
    }
)





def fetch_poster(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

    data = requests.get(url).json()

    poster_path = data.get("poster_path")

    if poster_path:
        return "https://image.tmdb.org/t/p/w500" + poster_path

    return None
