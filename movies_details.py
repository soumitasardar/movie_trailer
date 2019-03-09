import media
import fresh_tomatoes

'''
Below are the list of instance created for class Movie
'''
avatar = media.Movie("Avatar",
                     "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar"
                     "-Teaser-Poster.jpg", "On the lush alien world of Pandora"
                     " live the Na'vi, beings who appear primitive but are hig"
                     "hly evolved.",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")

lagaan = media.Movie("LAGAAN",
                     "https://upload.wikimedia.org/wikipedia/en/b/b6/"
                     "Lagaan.jpg",
                     "The year is 1893 and India is under British occupation.",
                     "https://www.youtube.com/watch?v=6BF-cO1ANc0")

ratatouille = media.Movie("Ratatouille",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/Rat"
                          "atouillePoster.jpg",
                          "Remy dreams of becoming a great chef.",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

# To display the list of movies in a website with the trailer,
# we have used fresh_tomatoes.py file

movie_list = [avatar, lagaan, ratatouille]
website = fresh_tomatoes.open_movies_page(movie_list)
print website
