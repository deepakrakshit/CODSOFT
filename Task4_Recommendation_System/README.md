# Task 4 – Recommendation System

## Objective

Create a simple recommendation system that suggests items to users based on their preferences. This project implements a Content-Based Filtering algorithm to recommend movies based on genre similarity.

## Technologies Used

- Python 3
- Python Standard Library (Sets, Dictionaries)

## Features

- Interactive command-line interface
- Pure procedural Python implementation (No OOP or external libraries)
- Content-Based Filtering algorithm
- Similarity scoring based on genre intersection
- Ranked output (best matches appear first)
- Case-insensitive search and input validation

## Project Structure

```text
Task4_Recommendation_System/
│
├── recommendation.py
└── README.md
```

## How to Run

```bash
python recommendation.py
```

## Sample Conversation

```text
==================================================
             CodBot Movie Recommender             
==================================================
Available movies: The Matrix, Inception, The Dark Knight, Pulp Fiction, Interstellar, The Avengers, The Godfather, Toy Story, Spirited Away
Type 'exit' to quit.

Enter a movie you like: inception

Because you liked 'Inception' (Action, Sci-Fi, Thriller):
Top Recommendations:
- The Matrix (Match Score: 2)
- The Avengers (Match Score: 2)
- The Dark Knight (Match Score: 1)
- Interstellar (Match Score: 1)

--------------------------------------------------

Enter a movie you like: exit
Goodbye!
```

## Future Improvements

- Integrate Pandas and Scikit-Learn to handle large CSV datasets (e.g., MovieLens).
- Implement Collaborative Filtering based on user ratings.
- Expand the dataset to include directors and actors for more accurate similarity scoring.

## Author

**Deepak Rakshit** Developed as part of the **CodSoft Artificial Intelligence Internship**.