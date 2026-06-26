movies = joblib.load("movies.pkl")
cv = joblib.load("vectorizer.pkl")

vector = cv.transform(movies["tags"])
similarity = cosine_similarity(vector)

joblib.dump(similarity, "similarity.pkl")
