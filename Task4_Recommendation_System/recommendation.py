# A simple hardcoded dataset of movies and their genres
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
    """Fetches the genres for a given movie title (case-insensitive)."""
    for title, genres in MOVIE_DATABASE.items():
        if title.lower() == movie_title.lower():
            return title, genres
    return None, None

def main():
    print("Version 1: Movie Database Initialized")
    target = "Inception"
    title, genres = get_movie_genres(target)
    
    if title:
        print(f"Movie found: {title}")
        print(f"Genres: {', '.join(genres)}")
    else:
        print("Movie not found in database.")

if __name__ == "__main__":
    main()