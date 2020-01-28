from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from extensions import mongo

def create_app(config_object='settings'):

  app = Flask(__name__)
  
  app.config.from_object(config_object)

  api = Api(app)

  api.add_resource(Hoteis, '/hoteis')
  api.add_resource(Hotel, '/hoteis/<string:id>')

  mongo.init_app(app)

  return app