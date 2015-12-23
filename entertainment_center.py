""" This program is to create and display a dynamic web-page of favorite movie titles, information, artwork, trailers, etc.

    Web-page can be viewed by openining fresh_tomatoes.html inside the movies folder. 

""" 
# Import Libraries
import fresh_tomatoes
import media

## Create library of favorite movies
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "www.youtube.com/watch?v=uZNHIU3uHT4")
school_of_rock = media.Movie("School of Rock",
                             "Jack Black stars as a fall-back school teacher who insists on jammin' out!",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://youtu.be/3PsUJFEBC74")

hunger_games = media.Movie("Hunger Games",
                           "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games and must fight for her life.",
                           "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
                           "https://youtu.be/3PkkHsuMrho")

office_space = media.Movie("Office Space",
                           "1999 American workplace comedy film[2] written and directed by Mike Judge. The film satirizes the everyday work life of a typical mid-to-late-1990s software company.",
                           "https://upload.wikimedia.org/wikipedia/en/8/8e/Office_space_poster.jpg",
                           "https://youtu.be/Bm_hDKXibpc")
                           
                           
harry_potter_dh2 = media.Movie("Harry Potter and the Deathly Hallows: Part 2",
                               "Teenage wizard Harry Potter must finally face off with Lord Voldemort in the ultimate battle to save the Wizarding World.",
                               "https://upload.wikimedia.org/wikipedia/en/d/df/Harry_Potter_and_the_Deathly_Hallows_–_Part_2.jpg",
                               "www.youtube.com/watch?v=ICIJk8DgQ_g")

## Store movies in an array to parse the information from the movies library
movies = [toy_story, avatar, school_of_rock, hunger_games, office_space, harry_potter_dh2]

## Run fresh tomatoes to create the webpage
fresh_tomatoes.open_movies_page(movies)
