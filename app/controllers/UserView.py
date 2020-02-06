from flask.views import MethodView
from app.models import User
from flask_restful import reqparse
from app.inc import Response, Functions
from exception import ResponseException


class UserView(MethodView):


    def get(self):
        pass


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', location='json', required=True)
        parser.add_argument('password', location='json', required=True)
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('last_name', location='json', required=True)
        data = parser.parse_args()
        print('in post view')
        data.update({'active': False})
        user = User(**data)
        user.create()
        return Response(user, 201).to_dict()


    def put(self):
        pass


    def delete(self):
        pass
