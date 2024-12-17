# Import Libraries
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load Dataset
file_path = 'Movie Recommendation system using Cosine Similarity/Dataset/movies_metadata.csv'
df = pd.read_csv(file_path, low_memory=False)

# Extract only required columns: 'title' and 'genres'
df = df[['id', 'title', 'genres']].dropna().head(1000)  # Using first 1000 rows for efficiency

# Preprocess genres: Convert JSON-like format into simple text
import ast
def extract_genres(genre_str):
    try:
        genres = [genre['name'] for genre in ast.literal_eval(genre_str)]
        return ', '.join(genres)
    except:
        return ''

df['genres'] = df['genres'].apply(extract_genres)

# Define a TF-IDF Vectorizer to transform the genre text into vectors
tfidf = TfidfVectorizer(stop_words='english')

# Fit and transform the genre column into a matrix of TF-IDF features
tfidf_matrix = tfidf.fit_transform(df['genres'])

# Compute the Cosine Similarity Matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to recommend movies based on cosine similarity
def get_recommendations(title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    indices = pd.Series(df.index, index=df['title']).drop_duplicates()
    if title not in indices:
        return ["Movie not found in the dataset."], []

    idx = indices[title]

    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices of the top 5 most similar movies (excluding itself)
    sim_scores = sim_scores[1:6]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the titles and indices of the most similar movies
    return df['title'].iloc[movie_indices].tolist(), movie_indices

# Function to calculate "accuracy" based on genre overlap
def calculate_genre_accuracy(input_title, recommendations, movie_indices):
    # Get the genres of the input movie
    input_genres = df[df['title'] == input_title]['genres'].values[0]
    input_genres_set = set(input_genres.split(', '))

    # Calculate overlap for each recommendation
    matches = 0
    for idx in movie_indices:
        rec_genres = df.iloc[idx]['genres']
        rec_genres_set = set(rec_genres.split(', '))
        if len(input_genres_set & rec_genres_set) > 0:  # Check for common genres
            matches += 1

    # Return accuracy as a proportion of matches
    accuracy = matches / len(recommendations) if recommendations else 0
    return accuracy

# Take input from user
movie_title = input("Enter a movie title: ")

# Get recommendations
recommended_movies, movie_indices = get_recommendations(movie_title)

# Display recommendations
print(f"\nMovies recommended for '{movie_title}':")
for movie in recommended_movies:
    print(f"Movie: {movie}")

# Calculate and display "accuracy"
accuracy = calculate_genre_accuracy(movie_title, recommended_movies, movie_indices)
print(f"\nRecommendation Accuracy (based on genre overlap): {accuracy * 100:.2f}")
