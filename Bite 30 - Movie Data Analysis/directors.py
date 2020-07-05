import csv
from collections import defaultdict, namedtuple
import os

MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    director_dict = {}
    with open("movie_metadata.csv", "r", encoding="utf8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if len(row["title_year"]) == 4 and int(row["title_year"]) >= MIN_YEAR:
                if row["director_name"] not in director_dict:
                    director_dict.update({row["director_name"]: [Movie(title=row["movie_title"], year=int(row["title_year"]), score=float(row["imdb_score"]))]})
                else:
                    director_dict[row["director_name"]].append(Movie(title=row["movie_title"], year=int(row["title_year"]), score=float(row["imdb_score"])))
    return director_dict


def calc_mean_score(movies):
    score_holder = 0
    for i in movies:
        score_holder += i.score

    score = round(score_holder/len(movies), 1)
    return score


def get_average_scores(directors):
    scores = []
    for director in directors:
        if len(directors[director]) >= MIN_MOVIES:
            scores.append((director, calc_mean_score(directors[director])))
    scores.sort(reverse=True, key=lambda i: i[1])
    return scores
