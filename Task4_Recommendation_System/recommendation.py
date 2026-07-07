# A simple hardcoded dataset of movies and their genres
MOVIE_DATABASE = {
    "The Matrix": ["Action", "Sci-Fi"],
    "Inception": ["Action", "Sci-Fi", "Thriller"],
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Pulp Fiction": ["Crime", "Drama"],
    "Interstellar": ["Sci-Fi", "Drama"],
    "The Avengers": ["Action", "Sci-Fi"],
    "The Godfather": ["Crime", "Drama"],
    "Toy Story": ["Animation", "Comedy", "Family"],
    "Spirited Away": ["Animation", "Family", "Fantasy"]
}

def get_movie_genres(movie_title):
    """Fetches the genres for a given movie title (case-insensitive)."""
    for title, genres in MOVIE_DATABASE.items():
        if title.lower() == movie_title.lower():
            return title, genres
    return None, None

def get_ranked_recommendations(target_title, target_genres):
    """
    Ranks movies based on the number of shared genres.
    Returns a sorted list of tuples: (movie_title, similarity_score)
    """
    recommendation_scores = []
    
    for title, genres in MOVIE_DATABASE.items():
        if title.lower() == target_title.lower():
            continue
            
        # The score is the number of genres the two movies share
        similarity_score = len(set(target_genres).intersection(set(genres)))
        
        if similarity_score > 0:
            recommendation_scores.append((title, similarity_score))
            
    # Sort the list by score in descending order (highest score first)
    recommendation_scores.sort(key=lambda x: x[1], reverse=True)
    return recommendation_scores

def main():
    print("==================================================")
    print("             CodBot Movie Recommender             ")
    print("==================================================")
    print("Available movies: " + ", ".join(MOVIE_DATABASE.keys()))
    print("Type 'exit' to quit.\n")
    
    while True:
        search_query = input("Enter a movie you like: ")
        
        if search_query.lower() == 'exit':
            print("Goodbye!")
            break
            
        title, genres = get_movie_genres(search_query)
        
        if not title:
            print("Sorry, that movie is not in our database. Try another one.\n")
            continue
            
        print(f"\nBecause you liked '{title}' ({', '.join(genres)}):")
        
        recommendations = get_ranked_recommendations(title, genres)
        
        if not recommendations:
            print("No similar movies found in the database.\n")
        else:
            print("Top Recommendations:")
            for rec_title, score in recommendations:
                print(f"- {rec_title} (Match Score: {score})")
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()