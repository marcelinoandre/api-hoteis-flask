from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
    {
        "hotel_id": "alpha",
        "nome": "Alpha Hotel",
        "estrelas": 4.3,
        "diaria": 420.35,
        "cidade": "São Paulo",
    },
    {
        "hotel_id": "hollydayin",
        "nome": "Holly Day In",
        "estrelas": 4.8,
        "diaria": 720.35,
        "cidade": "São Paulo",
    },
    {
        "hotel_id": "plazahotel",
        "nome": "Plaza Hotel",
        "estrelas": 4.1,
        "diaria": 415.35,
        "cidade": "Santa Catarina",
    },
    {
        "hotel_id": "copacabanapalace",
        "nome": "Copacabana Palace",
        "estrelas": 4.5,
        "diaria": 620.35,
        "cidade": "Rio de Janeiro",
    },
    {
        "hotel_id": "ibis",
        "nome": "Ibis Hotel",
        "estrelas": 4.0,
        "diaria": 400.35,
        "cidade": "Minas Gerais",
    },
]


class Hoteis(Resource):
    def get(self):
        return {"hoteis": hoteis}


class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome")
    argumentos.add_argument("estrelas")
    argumentos.add_argument("diaria")
    argumentos.add_argument("cidade")

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel["hotel_id"] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {"message": "Hotel not found."}, 404

    def post(self, hotel_id):

        dados = Hotel.argumentos.parse_args()
        hotel_obj = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_obj.json()
        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_obj = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_obj.json()
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel["hotel_id"] != hotel_id]
        return {"messge": "Hotel deleted."}
