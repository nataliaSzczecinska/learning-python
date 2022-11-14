import random
import datetime

class Movie():
    def __init__(self, title, year, movie_type):
        self.title = title
        self.year = year
        self.movie_type = movie_type
        
        #variables
        self._number_of_plays = 0

    @property
    def number_of_plays(self):
        return self._number_of_plays

    @number_of_plays.setter
    def number_of_plays(self, value):
        self._number_of_plays = value

    def play(self):
        self._number_of_plays += 1

    def __str__(self):
        return f"{self.title} ({self.year})"

class Serie(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season:02d}E{self.episode:02d}"

def get_movies(list_of_movies):
    list_of_elements = []
    for item in list_of_movies:
        if isinstance(item, Movie) and not isinstance(item, Serie):
            list_of_elements.append(item)
    return list_of_elements

def get_series(list_of_movies):
    list_of_elements = []
    for item in list_of_movies:
        if isinstance(item, Serie):
            list_of_elements.append(item)
    return list_of_elements

def search(title, list_of_movies):
    list_of_titles = []
    for item in list_of_movies:
        if (title == item.title):
            list_of_titles.append(item)
    return list_of_titles

def generate_views(list_of_movies):
    item = random.choice(list_of_movies)
    item.number_of_plays = random.randint(1, 100)

def generate_views_n_times(list_of_movies, times):
    for i in range(times):
        generate_views(list_of_movies)

def top_titles(list_of_movies, amount):
    sorted_by_number_of_plays = sorted(list_of_movies, key = lambda item: item.number_of_plays, reverse = True)
    if amount >= 0 and amount <= len(sorted_by_number_of_plays):
        return sorted_by_number_of_plays[:amount]
    else:
        raise ValueError(f"{amount} is not correct")

def top_titles_by_type(list_of_movies, amount, content_type):
    list_of_type = []
    if issubclass(content_type, Movie) and not issubclass(content_type, Serie):
        list_of_type = get_movies(list_of_movies)
    elif issubclass(content_type, Serie):
        list_of_type = get_series(list_of_movies)
    sorted_by_number_of_plays = sorted(list_of_type, key = lambda item: item.number_of_plays, reverse = True)
    if amount >= 0 and amount <= len(sorted_by_number_of_plays):
        return sorted_by_number_of_plays[:amount]
    else:
        raise ValueError(f"{amount} is not correct")

def add_series(list_of_movies, title, year, season, movie_type, number_of_episodes):
    for i in range(1, number_of_episodes + 1):
        list_of_movies.append(Serie(title = title, year = year, season = season, episode = i, movie_type = movie_type))


movie_01 = Movie(title = "Harry Potter and the Philospher's Stone", year = 2001, movie_type = ["fantasy"])
movie_02 = Movie(title = "Harry Potter and the Chamber of Sectects", year = 2002, movie_type = ["fantasy"])
movie_03 = Movie(title = "Harry Potter and the Prisoner of Azkaban", year = 2004, movie_type = ["fantasy"])
movie_04 = Movie(title = "Iron Man", year = 2008, movie_type = ["sience fiction", "action"])
movie_05 = Movie(title = "Iron Man 2", year = 2010, movie_type = ["sience fiction", "action"])
movie_06 = Movie(title = "Iron Man 3", year = 2013, movie_type = ["sience fiction", "action"])

movies_list = [movie_01, movie_02, movie_03, movie_04, movie_05, movie_06]

add_series(movies_list, "Doctor Hause", 2004, 1, ["drama", "medical series"], 22)
add_series(movies_list, "Doctor Hause", 2005, 2, ["drama", "medical series"], 24)
add_series(movies_list, "Doctor Hause", 2006, 3, ["drama", "medical series"], 24)
add_series(movies_list, "Doctor Hause", 2007, 4, ["drama", "medical series"], 16)

print("The Movies Library")
for item in movies_list:
    print(item)

generate_views_n_times(movies_list, 10)
today = datetime.datetime.now().strftime("%d.%m.%Y")
print("-" * 20)
print(f"Most popular movies {today} is:")
top_titles = top_titles(movies_list, 3)
for item in top_titles:
    print(f"{item} is played {item.number_of_plays} times")

"""
for movie in movies_list:
    print(movie)


list_of_movies = get_movies(movies_list)
list_of_series = get_series(movies_list)


print("Only movies")
for movie in list_of_movies:
    print(movie)

print("Only series")
for movie in list_of_series:
    print(movie)

movies_by_title = sorted(list_of_movies, key=lambda item: item.title)
series_by_title = sorted(list_of_series, key=lambda item: item.title)

print("Only movies - sorted")
for movie in movies_by_title:
    print(movie)

print("Only series - sorted")
for movie in series_by_title:
    print(movie)

print("Titles with \'Harry Potter and the Philospher's Stone\'")
harry_potter_and_the_philosphers_stone = search("Harry Potter and the Philospher's Stone", movies_list)
for item in harry_potter_and_the_philosphers_stone:
    print(item)

print("Titles with \'Friends\'")
friends = search("Friends", movies_list)
for item in friends:
    print(item)

print("Generate Views 10 times")
print(len(movies_list))
generate_views_n_times(movies_list, 10)
for item in movies_list:
    print(item)
    print(f"It is played {item.number_of_plays} times")

print("*" * 10)
print("Top 3 movies or series")
top_3 = top_titles(movies_list, 3)
for item in top_3:
    print(item)
    print(f"It is played {item.number_of_plays} times")


print("*" * 10)
print("Top 2 movies")
top_3 = top_titles_by_type(movies_list, 2, Movie)
for item in top_3:
    print(item)
    print(f"It is played {item.number_of_plays} times")
"""