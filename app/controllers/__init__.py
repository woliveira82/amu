from app import app
from app.controllers.UserView import UserView

view_user = UserView.as_view('user')
app.add_url_rule('/users/<action>', view_func=view_user, methods=['POST'])
app.add_url_rule('/users/<int:id>/password', view_func=view_user, methods=['PUT'])
app.add_url_rule('/users/<int:id>', view_func=view_user, methods=['DELETE'])
