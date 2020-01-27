from extensions import mongo
from bson.json_util import dumps
from models.hotel import HotelModel

class HotelDao():
  def findById(id):
    return dumps(mongo.db.hoteis.find_one({ '_id':ObjectId(id)}))

  def findAll():
    return mongo.db.hoteis.find()
  
  def save(obj):
    hotel = obj.toJson()
    return mongo.db.hoteis.insert_one(hotel)

