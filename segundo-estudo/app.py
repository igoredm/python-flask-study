from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from extensions import mongo

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://devuser:devpass@localhost/dev"

api = Api(app)

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<int:id>')

if __name__ == "__main__":
  mongo.init_app(app)
  app.run(debug=True)