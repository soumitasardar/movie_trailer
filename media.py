import webbrowser


class Movie():
    def __init__(self, movie_title, movie_poster, movie_storyline,
                 movie_trailer_url):
        '''Created a structure in order to store the movie details.
        self :- examples or instancces of this class
        This structure takes 4 string type parameters
        movie_title :- Name of the movie
        movie_poster :- image for the movie
        moview_storyline :- Movie description
        movie_trailer :- its a url of youtube video
        '''
        self.title = movie_title
        self.poster_image_url = movie_poster
        self.storyline = movie_storyline
        self.trailer_youtube_url = movie_trailer_url


def show_trailer(self):
    '''
    This function is for displaying the trailer for a selected movie
    '''
    webbrowser.open(self.trailer_youtube_url)


def show_poster(self):
    '''
    This function is for displaying the poster for a movie
    '''
    return webbrowser.open(self.poster)
