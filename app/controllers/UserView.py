from flask.views import MethodView
from app.models import User
from flask_restful import reqparse
from app.inc import Response, Functions
from exception import ResponseException


class UserView(MethodView):


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', location='json', required=True)
        parser.add_argument('password', location='json', required=True)
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('last_name', location='json', required=True)
        data = parser.parse_args()
        data.update({'active': False})
        user = User(**data)
        user.create()
        return Response(user, 201).to_dict()


    def post(self, action):
        if action != 'login':
            raise ResponseException(None, 404)

        parser = reqparse.RequestParser()
        parser.add_argument('email', location='json', required=True)
        parser.add_argument('password', location='json', required=True)
        data = parser.parse_args()

        user = User.login(**data)
        if not user:
            raise ResponseException(None, 401)
        
        return Response(user, 200, 'Mocklogin OK').to_dict()


    def put(self):
        pass


    def delete(self):
        pass
