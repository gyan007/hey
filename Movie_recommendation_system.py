# ------------Content based recommender-------------

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- Step 1: Create sample dataset ---

movies = pd.DataFrame({
    "title": [
        "The Matrix", "The Matrix Reloaded", "John Wick",
        "Inception", "Interstellar", "The Dark Knight", "Tenet"
    ],
    "genres": [
        "Action Sci-Fi", "Action Sci-Fi", "Action Thriller",
        "Sci-Fi Thriller", "Sci-Fi Adventure", "Action Crime", "Sci-Fi Thriller"
    ],
    "overview": [
        "A hacker discovers reality is a simulation.",
        "Neo and allies fight the machines.",
        "Ex-hitman seeks vengeance.",
        "A thief enters dreams to steal secrets.",
        "Explorers travel through a wormhole in space.",
        "Batman faces the Joker in Gotham.",
        "A secret agent manipulates time to prevent World War III."
    ]
})

# --- Step 2: Create combined text for similarity ---
movies["text"] = (movies["genres"].fillna("") + " " + movies["overview"].fillna("")).str.lower()

# --- Step 3: Compute TF-IDF similarity ---
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(movies["text"])
similarity = cosine_similarity(X)

# --- Step 4: Build a mapping from title to index ---
title_to_index = {title.lower(): idx for idx, title in enumerate(movies["title"])}

# --- Step 5: Recommendation function ---
def recommend(movie_name, top_n=5):
    movie_name = movie_name.lower()
    if movie_name not in title_to_index:
        print("\n Movie not found! Please try again.\n")
        return
    index = title_to_index[movie_name]
    sim_scores = list(enumerate(similarity[index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1: top_n + 1]

    print(f"\n Because you watched **{movies.iloc[index]['title']}**, you might also like:\n")
    for i, (movie_idx, score) in enumerate(sim_scores):
        print(f"{i+1}. {movies.iloc[movie_idx]['title']}  (Similarity: {score:.2f})")

# --- Step 6: Take user input ---
print("Available movies:\n", ", ".join(movies['title']), "\n")
user_movie = input("Enter a movie you liked: ")
recommend(user_movie)



# --------------Collaborative filtering approach ----------------

import pandas as pd, numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# tiny ratings data
ratings = pd.DataFrame({
    "user":[1,1,1,2,2,2,3,3,4,4,5,5],
    "movie":["Matrix","Inception","John Wick","Matrix","Interstellar","Dark Knight",
             "Inception","Interstellar","John Wick","Dark Knight","Matrix","Interstellar"],
    "rating":[5,4,5,4,5,5,5,4,4,5,3,4]
})

# user-item matrix + user-user similarity
R = ratings.pivot_table(index="user", columns="movie", values="rating").fillna(0)
S = pd.DataFrame(cosine_similarity(R), index=R.index, columns=R.index)

def recommend(user_id, top_n=3, min_sim=0.1):
    if user_id not in R.index: return print("User not found.")
    sims = S.loc[user_id].drop(user_id); sims = sims[sims>min_sim]
    if sims.empty: return print("Not enough similar users.")
    preds = np.dot(sims.values, R.loc[sims.index].values) / (sims.values.sum()+1e-9)
    preds = pd.Series(preds, index=R.columns)
    recs = preds[R.loc[user_id]==0].sort_values(ascending=False).head(top_n)
    print(f"Top picks for user {user_id}:")
    for i,(m,score) in enumerate(recs.items(),1): print(f"{i}. {m} (score {score:.2f})")

print("Users:", list(R.index)); print("Movies:", ", ".join(R.columns))
uid = int(input("Enter your user ID: "))
recommend(uid, top_n=3)
