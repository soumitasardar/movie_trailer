				Movie Trailer website
This is a simple script written in python in order to create a website with list of movies along with its poster and trailer.

Installation:
create a folder in your system
Open terminal or command prompt and go to that created folder
give command: git clone https://github.com/soumitasardar/movie_trailer.git
To run this project:
Python movies_details

Code description:
* Define a Python Class in order to create a structure of movies information.
* Then defining __init__function to grab the movies details in order to create a structure of movies details.
	def __init__(self,movie_name,movie_poster,movie_storyline,movie_url)
* Then you can define another function or method to open a trailer for the respective movie instances.
* Many other things can also be done, as per the requirements and saved in media.py file.
	Once done, use a different movies_details.py file by calling the constructor media.Movie() to instantiate movie objects or instances.
* For that, let's say 1st instance of movie we create by first importing the class .py file name and calling the constructor media.Movie() and providing all the necessary information regarding that movie sequentially as mentioned in the Python Class.
* Similarly, various numbers of instances can be created with many movie details.
	After creating the instances of movies, now it’s time to show this all in a website.
* For that, either you can create your own .py file by including HTML and use the trailer link provided in every movie OR you can use fresh_tomatoes .py file provided here and save that it the same folder where your project is saved.
* After this, create a list of movies which you want to display in the website.
* You can use fresh_tomatoes file and the function "open_movies_trailer()" inside it.

Result:
The moment you run movies_details.py either by python IDE or in any terminal, you can able to see:
	A website open with list of movies along with the posters and on selecting a particular movie, trailer will start playing.	

License:
Movie Trailer Website is released under MIT License, where you can contribute in the code and create your own project.

