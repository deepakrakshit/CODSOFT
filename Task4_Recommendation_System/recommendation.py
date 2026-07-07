MOVIE_DATABASE = {
    "The Matrix": ["Action", "Sci-Fi"],
    "Inception": ["Action", "Sci-Fi", "Thriller"],
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Pulp Fiction": ["Crime", "Drama"],
    "Interstellar": ["Sci-Fi", "Drama"],
    "The Avengers": ["Action", "Sci-Fi"],
    "The Godfather": ["Crime", "Drama"],
    "Toy Story": ["Animation", "Comedy", "Family"]
}

def get_movie_genres(movie_title):
    for title, genres in MOVIE_DATABASE.items():
        if title.lower() == movie_title.lower():
            return title, genres
    return None, None

def get_basic_recommendations(target_title, target_genres):
    """Finds any movie that shares at least one genre with the target."""
    recommendations = []
    
    for title, genres in MOVIE_DATABASE.items():
        # Don't recommend the movie the user just searched for
        if title.lower() == target_title.lower():
            continue
            
        # Check if there is any overlap in genres using Python sets
        shared_genres = set(target_genres).intersection(set(genres))
        if len(shared_genres) > 0:
            recommendations.append(title)
            
    return recommendations

def main():
    print("Version 2: Basic Overlap Recommendation")
    search_query = input("Enter a movie you like (e.g., The Matrix, Inception): ")
    
    title, genres = get_movie_genres(search_query)
    
    if not title:
        print("Sorry, that movie is not in our database.")
        return
        
    print(f"\nSince you liked {title} ({', '.join(genres)}):")
    recommendations = get_basic_recommendations(title, genres)
    
    print("You might also like:")
    for rec in recommendations:
        print(f"- {rec}")

if __name__ == "__main__":
    main()