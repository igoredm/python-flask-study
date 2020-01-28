from extensions import mongo
from bson.objectid import ObjectId

class UserDao():

  def findById(id):
    return mongo.db.usuarios.find_one({ '_id':ObjectId(id)}, {'login':1})

  def findByLogin(login):
    return mongo.db.usuarios.find_one({ 'login':login})

  def save(usuario):
    return mongo.db.usuarios.insert_one(usuario)

  def update(usuario):
    mongo.db.usuarios.update_one({'_id': usuario['_id']}, {"$set": usuario})
    
  def delete(id):
    return mongo.db.usuarios.delete_one({'_id': ObjectId(id)})