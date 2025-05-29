# 🎬 Python Capstone Project: Movie Suggestion Bot
# Purpose is to take info from the user about their favorite movie genre and scrape the top-rated movies from IMDB of that genre.
# requests + bs4 + pandas are used for web scraping and data handling.

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Ask for a genre to scrape movies from IMDB.
def scrape_movies_by_genre():
    try:
        genre = input("🎞️ Enter a movie genre (e.g., action, drama, comedy): ").lower()
        url = f"https://www.imdb.com/search/title/?genres={genre}&sort=user_rating,desc&title_type=feature"
        headers = {"User-Agent": "Mozilla/5.0"}

        print(f"[INFO] Scraping movies from IMDB for genre: {genre}...")

        response = requests.get(url, headers=headers)
        response.raise_for_status()  # if there is an HTTP error, raise an exception

        soup = BeautifulSoup(response.text, "html.parser")

        # IMBD scraping logic
        movie_items = soup.find_all("li", class_="ipc-metadata-list-summary-item")
        if not movie_items:
            raise ValueError("No movies found. Genre may be invalid or IMDB layout changed.")

        movies = []
        for item in movie_items:
            # Movie name
            title_tag = item.select_one("div.sc-4b408797-0.eFrxXF a h3")
            title = title_tag.text.strip() if title_tag else "N/A"

            # Year of release
            year_tag = item.select_one("div.sc-4b408797-7.fUdAcX span")
            year = year_tag.text.strip() if year_tag else "N/A"

            # IMDB rating
            rating_tag = item.select_one("span[data-testid='ratingGroup--imdb-rating'] span.ipc-rating-star--rating")
            rating = rating_tag.text.strip() if rating_tag else "N/A"

            movies.append({
                "Title": title,
                "Year": year,
                "Rating": rating,
                "Genre": genre
            })

        # Pandas ile CSV olarak kaydet
        df = pd.DataFrame(movies)
        filename = f"{genre}_movies.csv"
        df.to_csv(filename, index=False)

        print(f"[✅ SUCCESS] Scraped and saved {len(df)} movies to {filename}.\n")
        print(df.head(5))  # Show first 5 movies as an example
        return True

    except requests.RequestException as e:
        print(f"[ERROR] Network issue: {e}")
    except Exception as e:
        print(f"[ERROR] {e}")
    return False


# Call the function to start the scraping process
if __name__ == "__main__":
    print("🎬 Welcome to my Movie Suggestion Bot - Final Project")
    scrape_movies_by_genre()
