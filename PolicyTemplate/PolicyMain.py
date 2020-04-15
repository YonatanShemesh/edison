from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from UserValidation import authenticate, identity
from db import db

from Resources.Policy import Policy, PolicyList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'Fuck knows'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Policy, '/policy/<string:name>')
#api.add_resource(StoreList, '/stores')
#api.add_resource(Item, '/item/<string:name>')
#api.add_resource(ItemList, '/items')
#api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
