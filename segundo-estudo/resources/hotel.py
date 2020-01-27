from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from dao.hotel import HotelDao

class Hoteis(Resource):
  def get(self):
    print(HotelDao.findAll())
    return { 'Hoteis': [] }, 200


class Hotel(Resource):
  argumentos = reqparse.RequestParser()
  argumentos.add_argument('nome')
  argumentos.add_argument('estrelas')
  argumentos.add_argument('diaria')
  argumentos.add_argument('cidade')

  def findHotel(id):
    for hotel in hoteis:
      if hotel['id'] == id: return hotel
    return None


  def get(self, id):
    hotel = Hotel.findHotel(id)
    if hotel:
      return hotel
    return {'message': 'Hotel não encontrado.'}, 404

  def post(self, id):

    dados = Hotel.argumentos.parse_args()

    novoHotelObj = HotelModel(id, **dados)
    # novoHotel = novoHotelObj.toJson()

    # hoteis.append(novoHotel)

    id = HotelDao.save(novoHotelObj)


    return "Hotel salvo com id: " + str(id), 201

  def put(self, id):
    dados = Hotel.argumentos.parse_args()

    novoHotelObj = HotelModel(id, **dados)
    novoHotel = novoHotelObj.toJson()

    hotel = Hotel.findHotel(id)
    if hotel:
      hotel.update(novoHotel)
      return novoHotel, 200
    
    hoteis.append(novoHotel)
    return novoHotel, 201

  def delete(self, id):
    global hoteis
    hoteis = [hotel for hotel in hoteis if hotel['id'] != id]
    return None ,204

hoteis = [
  {
    'id': 1,
    'nome': 'Alpha Hotel',
    'estrelas': 4.3,
    'diaria': 380.34,
    'cidade': 'Jundiaí'
  },
  {
    'id': 2,
    'nome': 'Bravo Hotel',
    'estrelas': 4.4,
    'diaria': 420.52,
    'cidade': 'São Paulo'
  },
  {
    'id': 3,
    'nome': 'Hotel Charlie',
    'estrelas': 3.9,
    'diaria': 310.20,
    'cidade': 'Araraquara'
  }
]