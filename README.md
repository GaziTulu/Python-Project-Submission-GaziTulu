# Python-Project-Submission-GaziTulu
# Movie Suggestion Bot

This is a **Python Capstone Project** designed to scrape and suggest top-rated movies from IMDb based on the user's favorite genre. It leverages web scraping and data handling techniques using `requests`, `BeautifulSoup`, and `pandas`.

##  Features

- Takes user input for a movie genre (e.g., action, comedy, drama)
- Scrapes top-rated feature films of that genre from IMDb
- Extracts movie title, release year, and IMDb rating
- Saves the results as a CSV file for easy access
- Displays the top 5 results directly in the terminal

## It Uses

- 
- `requests` – For making HTTP requests to IMDb
- `BeautifulSoup (bs4)` – For parsing and extracting data from HTML
- `pandas` – For data manipulation and CSV export

## Installation

1. Clone the repository:
   
   git clone https://github.com/yourusername/movie-suggestion-bot.git
   cd movie-suggestion-bot
   

2. Install required packages:
   
   pip install -r requirements.txt
   

3. Run the script:
   
   python movie_suggester.py
   

## Example Output

```
Welcome to my Movie Suggestion Bot - Capstone Final Project
Enter a movie genre (e.g., action, drama, comedy): drama
Scraping movies from IMDB for genre: drama...
Scraped and saved 50 movies to drama_movies.csv.
```

Sample of the output:

| Title                  | Year | Rating | Genre |
|------------------------|------|--------|--------|
| The Shawshank Redemption | 1994 | 9.3    | drama |
| Forrest Gump           | 1994 | 8.8    | drama |
| ...                    | ...  | ...    | ...    |

