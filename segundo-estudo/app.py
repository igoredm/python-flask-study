from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.usuario import User, UserRegister, UserLogin
from extensions import mongo
from flask_jwt_extended import JWTManager

def create_app(config_object='settings'):

  app = Flask(__name__)
  
  app.config.from_object(config_object)

  api = Api(app)
  jwt = JWTManager(app)

  api.add_resource(Hoteis, '/hoteis')
  api.add_resource(Hotel, '/hoteis/<string:id>')
  api.add_resource(User, '/usuarios/<string:id>')
  api.add_resource(UserRegister, '/signup')
  api.add_resource(UserLogin, '/login')

  mongo.init_app(app)

  return app