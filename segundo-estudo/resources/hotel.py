from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from dao.hotel import HotelDao

class Hoteis(Resource):
  argumentos = reqparse.RequestParser()
  argumentos.add_argument('nome')
  argumentos.add_argument('estrelas')
  argumentos.add_argument('diaria')
  argumentos.add_argument('cidade')


  def get(self):
    cursor = HotelDao.findAll()
    lista = []

    for c in cursor:
      c['_id'] = str(c['_id'])
      lista.append(c)

    return lista, 200


  def post(self):

    dados = Hotel.argumentos.parse_args()

    obj = HotelModel(**dados)
    hotel = obj.toJson()

    returnObj = HotelDao.save(hotel)

    return "Hotel salvo com id: " + str(returnObj.inserted_id), 201


class Hotel(Resource):
  argumentos = reqparse.RequestParser()
  argumentos.add_argument('nome')
  argumentos.add_argument('estrelas')
  argumentos.add_argument('diaria')
  argumentos.add_argument('cidade')

  def get(self, id):
    try:
      hotel = HotelDao.findById(id)
    except:
      return None, 400

    if hotel:
      hotel['_id'] = str(hotel['_id'])
      return hotel, 200
    return None, 404

  def put(self, id):
    dados = Hotel.argumentos.parse_args()

    novoHotelObj = HotelModel(**dados)
    novoHotel = novoHotelObj.toJson()

    try: 
      hotel = HotelDao.findById(id)
    except:
      return None, 400
    if hotel:
      hotel.update(novoHotel)
      print(hotel)
      HotelDao.update(hotel)
      return novoHotel, 200
    return None, 404

  def delete(self, id):
    try:
      returnObj = HotelDao.delete(id)
    except:
      return None, 400

    if returnObj.deleted_count > 0:
      return None, 204  
    return None, 404