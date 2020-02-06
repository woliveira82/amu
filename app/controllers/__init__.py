from app import app
from app.controllers.UserView import UserView

view_user = UserView.as_view('user')
app.add_url_rule('/users', view_func=view_user, methods=['GET', 'POST'])
# app.add_url_rule('/users/<int:scenario_id>', view_func=view_user, methods=['GET', 'PUT', 'DELETE'])
