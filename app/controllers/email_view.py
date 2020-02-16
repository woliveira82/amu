from flask.views import MethodView
from flask_restful import reqparse

from app.inc import Functions, Response
from app.models import Email
from exception import ResponseException


class EmailView(MethodView):


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', location='json', required=True)
        data = parser.parse_args()

        email = Email(data['email'])
        email.create()
        return Response(email, 201).to_dict()
