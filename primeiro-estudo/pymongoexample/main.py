from flask import Blueprint
from bson.json_util import dumps
from .user import User
from bson.objectid import ObjectId
from flask import jsonify, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from .extensions import mongo 

main = Blueprint('main', __name__)

@main.route('/')
def findAll():
    user_collection = mongo.db.users
    users = user_collection.find()
    data = dumps(users)
    response = make_response(data)
    response.mimetype = 'application/json'
    return response

@main.route('/<id>', methods=['GET'])
def findById(id):
    user_collection = mongo.db.users
    try: 
      users = user_collection.find_one({ '_id':ObjectId(id)})
    except:
      return bad_request()
    data = dumps(users)
    response = make_response(data)
    response.mimetype = 'application/json'
    return response


@main.route('/add', methods=['POST'])
def add_user():
  user = User()

  _json = request.json
  _name = _json['name']
  _email = _json['email']
  _pass = _json['pwd']

  if _name and _email and _pass and request.method == 'POST':
    _hashed_pass = generate_password_hash(_pass)

    user_collection = mongo.db.users
    id = user_collection.insert({'name':_name, 'email':_email,'pwd':_hashed_pass})

    response = jsonify("User added PORRA, ID: " + str(id))

    response.status_code = 200

    return response
  
  else:
    return bad_request()

@main.route('/<id>', methods=['PUT'])
def updateUser(id):
  _id = id
  _json = request.json
  _name = _json['name']
  _email = _json['email']
  _pass = _json['pwd']

  if _name and _email and _pass and request.method == 'PUT':
    _hashed_pass = generate_password_hash(_pass)

    user_collection = mongo.db.users
    user_collection.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'name':_name, 'email':_email,'pwd':_hashed_pass}})

    response = jsonify("User edited PORRA, ID: " + str(id))

    response.status_code = 200

    return response

@main.route('/<id>', methods=['DELETE'])
def deleteById(id):
    user_collection = mongo.db.users
    user_collection.delete_one({ '_id':ObjectId(id)})

    response = jsonify("User deleted PORRA")

    response.status_code = 204
    return response

@main.route('/test')
def test():
  userTest = User()
  userTest.setName("ola")
  return userTest.getName()

@main.errorhandler(400)
def bad_request(error=None):
  message = {
    'status': 400,
    'message':'Faz o bag direito BURRO'
  }

  resp = jsonify(message)
  resp.status_code = 400

  return resp