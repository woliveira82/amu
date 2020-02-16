from app import app
from .email_view import EmailView
from .UserView import UserView

view_email = EmailView.as_view('email')
app.add_url_rule('/email', view_func=view_email, methods=['POST'])


view_user = UserView.as_view('user')
app.add_url_rule('/users', view_func=view_user, methods=['POST'])
app.add_url_rule('/users/<action>', view_func=view_user, methods=['POST'])
app.add_url_rule('/users/<int:id>/password', view_func=view_user, methods=['PUT'])
app.add_url_rule('/users/<int:id>', view_func=view_user, methods=['DELETE'])
