from extensions import mongo
from bson.objectid import ObjectId
from models.hotel import HotelModel

class HotelDao():

  def findById(id):
    return mongo.db.hoteis.find_one({ '_id':ObjectId(id)})

  def findAll():
    return mongo.db.hoteis.find()

  def save(hotel):
    return mongo.db.hoteis.insert_one(hotel)

  def update(hotel):
    mongo.db.hoteis.update_one({'_id': hotel['_id']}, {"$set": hotel})
    
  def delete(id):
    return mongo.db.hoteis.delete_one({'_id': ObjectId(id)})