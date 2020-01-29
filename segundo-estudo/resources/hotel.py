from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from dao.hotel import HotelDao
from flask_jwt_extended import jwt_required


def normalize_path_params(cidade=None,
                          estrelas_min=0,
                          estrelas_max=5.1,
                          diaria_min=0,
                          diaria_max=100000,
                          limit=50,
                          page=0, **dados):
    if cidade:
        return {
            'filters': {
                'estrelas': {"$gt": estrelas_min, "$lt": estrelas_max},
                'diaria': {"$gt": diaria_min, "$lt": diaria_max},
                'cidade': cidade
            },
            'limit': limit,
            'page': page
        }
    return {
        'filters': {
            'estrelas': {"$gt": estrelas_min, "$lt": estrelas_max},
            'diaria': {"$gt": diaria_min, "$lt": diaria_max}
        },
        'limit': limit,
        'page': page
    }


path_params = reqparse.RequestParser()
path_params.add_argument('cidade', type=str)
path_params.add_argument('estrelas_min', type=float)
path_params.add_argument('estrelas_max', type=float)
path_params.add_argument('diaria_min', type=float)
path_params.add_argument('diaria_max', type=float)
path_params.add_argument('limit', type=int)
path_params.add_argument('page', type=int)


class Hoteis(Resource):

    def get(self):

        dados = path_params.parse_args()
        dados_validos = {chave: dados[chave]
                         for chave in dados if dados[chave] is not None}

        if dados_validos:
            dados_normalizados = normalize_path_params(**dados_validos)
            cursor = HotelDao.findByParams(
                dados_normalizados['filters'],
                dados_normalizados['limit'],
                dados_normalizados['page']
            )

        else:
            cursor = HotelDao.findAll()
        # cursor = HotelDao.findByParams(teste)
        lista = []

        for c in cursor:
            c['_id'] = str(c['_id'])
            lista.append(c)

        return lista, 200

    @jwt_required
    def post(self):

        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome', type=str, required=True,
                                help="O campo 'nome' não pode ser deixado em branco")
        argumentos.add_argument('estrelas', type=float, required=True,
                                help="O campo 'estrelas' não pode ser deixado em branco")
        argumentos.add_argument('diaria', type=float, required=True,
                                help="O campo 'diaria' não pode ser deixado em branco")
        argumentos.add_argument('cidade', type=str, required=True,
                                help="O campo 'cidade' não pode ser deixado em branco")

        dados = argumentos.parse_args()

        obj = HotelModel(**dados)
        hotel = obj.toJson()

        returnObj = HotelDao.save(hotel)

        return "Hotel salvo com id: " + str(returnObj.inserted_id), 201


class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True,
                            help="O campo 'nome' não pode ser deixado em branco")
    argumentos.add_argument('estrelas', type=float, required=True,
                            help="O campo 'estrelas' não pode ser deixado em branco")
    argumentos.add_argument('diaria', type=float, required=True,
                            help="O campo 'diaria' não pode ser deixado em branco")
    argumentos.add_argument('cidade', type=str, required=True,
                            help="O campo 'cidade' não pode ser deixado em branco")

    def get(self, id):
        try:
            hotel = HotelDao.findById(id)
        except:
            return None, 404

        if hotel:
            hotel['_id'] = str(hotel['_id'])
            return hotel, 200
        return None, 404

    @jwt_required
    def put(self, id):
        dados = Hotel.argumentos.parse_args()

        novoHotelObj = HotelModel(**dados)
        novoHotel = novoHotelObj.toJson()

        try:
            hotel = HotelDao.findById(id)
        except:
            return None, 404
        if hotel:
            hotel.update(novoHotel)
            print(hotel)
            HotelDao.update(hotel)
            return novoHotel, 200
        return None, 404

    @jwt_required
    def delete(self, id):
        try:
            returnObj = HotelDao.delete(id)
        except:
            return None, 400

        if returnObj.deleted_count > 0:
            return None, 204
        return None, 404
