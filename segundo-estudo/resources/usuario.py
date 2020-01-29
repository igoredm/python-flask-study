from flask_restful import Resource, reqparse
from flask import jsonify
from models.usuario import UserModel
from dao.usuario import UserDao
from flask_jwt_extended import (
    create_access_token, create_refresh_token, jwt_required,
    get_raw_jwt, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies
)
from werkzeug.security import safe_str_cmp

argumentos = reqparse.RequestParser()
argumentos.add_argument('login', type=str, required=True,
                        help="O campo 'login' não pode ser deixado em branco")
argumentos.add_argument('senha', type=str, required=True,
                        help="O campo 'senha' não pode ser deixado em branco")


class UserRegister(Resource):

    def post(self):

        dados = argumentos.parse_args()

        if UserDao.findByLogin(dados['login']):
            return {"message": "O nome de usuário já existe, tente fazer login"}, 400

        obj = UserModel(**dados)
        usuario = obj.toJson()

        returnObj = UserDao.save(usuario)

        return "Usuario salvo com id: " + str(returnObj.inserted_id), 201


class UserLogin(Resource):

    @classmethod
    def post(cls):
        dados = argumentos.parse_args()

        user = UserDao.findByLogin(dados['login'])

        if user and safe_str_cmp(user['senha'], dados['senha']):
            accessToken = create_access_token(identity=str(user['_id']))

            resp = jsonify({'login': True})
            set_access_cookies(resp, accessToken)
            print(resp)

            return resp
        return {'message': 'Usuário ou senha inválidos'}, 401


class UserLogout(Resource):
    @jwt_required
    def post(self):
        resp = jsonify({'logout': True})
        unset_jwt_cookies(resp)
        return resp


class User(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True,
                            help="O campo 'nome' não pode ser deixado em branco")
    argumentos.add_argument('estrelas', type=float, required=True,
                            help="O campo 'estrelas' não pode ser deixado em branco")
    argumentos.add_argument('diaria', type=float, required=True,
                            help="O campo 'diaria' não pode ser deixado em branco")
    argumentos.add_argument('cidade', type=str, required=True,
                            help="O campo 'cidade' não pode ser deixado em branco")

    @jwt_required
    def get(self, id):
        try:
            usuario = UserDao.findById(id)
        except:
            return None, 404

        if usuario:
            usuario['_id'] = str(usuario['_id'])
            return usuario, 200
        return None, 404

    # def put(self, id):
    #   dados = Hotel.argumentos.parse_args()

    #   novoHotelObj = HotelModel(**dados)
    #   novoHotel = novoHotelObj.toJson()

    #   try:
    #     hotel = HotelDao.findById(id)
    #   except:
    #     return None, 404
    #   if hotel:
    #     hotel.update(novoHotel)
    #     print(hotel)
    #     HotelDao.update(hotel)
    #     return novoHotel, 200
    #   return None, 404

    @jwt_required
    def delete(self, id):
        try:
            returnObj = UserDao.delete(id)
        except:
            return None, 400

        if returnObj.deleted_count > 0:
            return None, 204
        return None, 404
