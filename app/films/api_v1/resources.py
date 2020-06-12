from flask import Blueprint
from flask_restful import Api, Resource

from .schemas import FilmSchema
from ..models import Film

film_schema = FilmSchema()

films_bp = Blueprint('films_v1', __name__)


class FilmListResource(Resource):

    def get(self):
        films = Film.get_all()
        result = film_schema.dump(films, many=True)
        return result


class FilmResource(Resource):

    def get(self, id):
        film = Film.get_by_id(id)
        result = self.film_schema.dump(film)
        return result


api = Api(films_bp)

api.add_resource(FilmListResource, 'api/v1/films/',
                 endpoint='film_list_resource')
api.add_resource(FilmResource, 'api/v1/films/<int:id>',
                 endpoint="film_resource")
