from flask import Blueprint

user = Blueprint('api', __name__)


@user.route('/', methods=['POST'])
def test():
    pass
