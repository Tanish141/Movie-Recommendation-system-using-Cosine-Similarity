### 🎬 Movie Recommendation System using Cosine Similarity
Welcome to the Movie Recommendation System! 🚀
This project uses TF-IDF Vectorization and Cosine Similarity to recommend movies based on their genres. It is a simple, content-based recommendation system built in Python. 🐍

---

### ✨ Features
🔹 Content-Based Filtering: Recommends movies based on similarity in genres.
🔹 Cosine Similarity: Calculates similarity scores between movies.
🔹 Interactive Input: User can input a movie title to get recommendations.
🔹 Accuracy Check: Evaluate how well the recommendations align with the dataset.

---

### 🛠️ Technologies Used
Python 🐍
Pandas: For data manipulation and preprocessing.
Scikit-learn: TF-IDF Vectorizer and Cosine Similarity.
Terminal/CLI: User inputs and interaction.

---

### 📊 Dataset
The project uses a dataset containing movie details:

Columns: movie_id, title, and genre.
The dataset includes various movies with genres like Action, Sci-Fi, Drama, etc.
Sample Dataset:

movie_id	title	genre
1	The Matrix	Action, Sci-Fi
2	John Wick	Action, Thriller
3	The Godfather	Crime, Drama
4	Pulp Fiction	Crime, Drama
5	The Dark Knight	Action, Crime, Drama

---

### ⚙️ How the System Works
TF-IDF Vectorization:
The genres are transformed into numerical vectors using TF-IDF (Term Frequency-Inverse Document Frequency).

Cosine Similarity:
Similarity scores between movies are calculated using the Cosine Similarity function.

Recommendations:
Based on the input movie, the system returns the most similar movies.

User Input:
The user can input a movie title, and the system will recommend similar movies.

Accuracy Check:
The system evaluates how well the similarity-based model performs using test data.

---

### 🚀 How to Run the Project
Follow these steps to run the project on your local machine:

Clone the Repository:

bash
Copy code
git clone https://github.com/Tanish141/movie-recommendation-system.git
cd movie-recommendation-system
Install Required Libraries: Ensure Python and pip are installed, then run:

bash
Copy code
pip install pandas scikit-learn
Run the Script: Run the Python script in your terminal:

bash
Copy code
python movie_recommendation.py
Provide User Input:
Input a movie title from the dataset when prompted, for example:

css
Copy code
Enter a movie title: The Matrix
Output:
The system will recommend similar movies:

vbnet
Copy code
Movies recommended for 'The Matrix':
Movie: John Wick
Movie: The Dark Knight

---

### ✅ Accuracy
The model provides a simple way to evaluate the accuracy by comparing the recommendations against the dataset. Results are displayed as part of the output.

---

### 🎥 Example Run
Example terminal interaction:

bash
Copy code
Movie Data:
   movie_id             title                   genre
0         1       The Matrix           Action, Sci-Fi
1         2        John Wick       Action, Thriller
2         3    The Godfather           Crime, Drama
3         4    Pulp Fiction           Crime, Drama
4         5 The Dark Knight Action, Crime, Drama

Enter a movie title: The Matrix

Movies recommended for 'The Matrix':
Movie: John Wick
Movie: The Dark Knight

---

### 🏅 Learning Outcomes
By working on this project, you will learn:

How to preprocess text data using TF-IDF Vectorization.
Calculating pairwise similarity using Cosine Similarity.
Building an interactive recommendation system.
Evaluating the performance of content-based filtering systems.

---

### 🤝 Contributions
Contributions are welcome! 🚀
If you'd like to improve or extend the project, feel free to fork the repository, create a feature branch, and submit a pull request.

---

### 📧 Contact
If you have any questions or suggestions, feel free to reach out:

Email: mrtanish14@gmail.com
GitHub: [Tanish141](https://github.com/Tanish141)

---

### 🎉 Happy Coding!
### ✨ Star this repository if you found it helpful! 🌟
