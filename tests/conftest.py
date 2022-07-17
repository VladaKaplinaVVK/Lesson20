from unittest.mock import MagicMock
import pytest
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre

from dao.movie import MovieDAO
from dao.model.movie import Movie


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    d1 = Director(id=1, name="Vlad")
    d2 = Director(id=1, name="Oleg")
    d3 = Director(id=1, name="Petr")

    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2, d3])
    director_dao.create = MagicMock(return_value=d3)
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    return director_dao


@pytest.fixture()
def genre_dao():
    genre = GenreDAO(None)

    g1 = Genre(id=1, name="Drama")
    g2 = Genre(id=1, name="Thriller")
    g3 = Genre(id=1, name="Comedy")

    genre.get_one = MagicMock(return_value=g1)
    genre.get_all = MagicMock(return_value=[g1, g2, g3])
    genre.create = MagicMock(return_value=g3)
    genre.delete = MagicMock()
    genre.update = MagicMock()
    return genre


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    m1 = Movie(id=1, title="M_1", description="Description_1", year="2002")
    m2 = Movie(id=1, title="M_2", description="Description_2", year="2020")
    m3 = Movie(id=1, title="M_3", description="Description_3", year="2016")

    movie_dao.get_one = MagicMock(return_value=m1)
    movie_dao.get_all = MagicMock(return_value=[m1, m2, m3])
    movie_dao.create = MagicMock(return_value=m3)
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao
