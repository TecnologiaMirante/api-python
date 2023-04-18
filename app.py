from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

ativos = []
exaustores = []
nobreaks = []
switches = []

class Ativos(Resource):
    def get(self):
        return ativos

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("tag", type=str, required=True)
        parser.add_argument("modelo", type=str, required=True)
        parser.add_argument("marca", type=str, required=True)
        parser.add_argument("potencia", type=int, required=True)
        parser.add_argument("tensao", type=int, required=True)
        args = parser.parse_args()

        ativo = {
            "id": len(ativos) + 1,
            "tag": args["tag"],
            "modelo": args["modelo"],
            "marca": args["marca"],
            "potencia": args["potencia"],
            "tensao": args["tensao"]
        }
        ativos.append(ativo)
        return ativo, 201

class Exaustores(Resource):
    def get(self):
        return exaustores

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("tag", type=str, required=True)
        parser.add_argument("modelo", type=str, required=True)
        parser.add_argument("marca", type=str, required=True)
        args = parser.parse_args()

        exaustor = {
            "id": len(exaustores) + 1,
            "tag": args["tag"],
            "modelo": args["modelo"],
            "marca": args["marca"]
        }
        exaustores.append(exaustor)
        return exaustor, 201

class Nobreaks(Resource):
    def get(self):
        return nobreaks

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("tag", type=str, required=True)
        parser.add_argument("modelo", type=str, required=True)
        parser.add_argument("marca", type=str, required=True)
        parser.add_argument("tensaoEntrada", type=int, required=True)
        parser.add_argument("tensaoSaida", type=int, required=True)
        args = parser.parse_args()

        nobreak = {
            "id": len(nobreaks) + 1,
            "tag": args["tag"],
            "modelo": args["modelo"],
            "marca": args["marca"],
            "tensaoEntrada": args["tensaoEntrada"],
            "tensaoSaida": args["tensaoSaida"]
        }
        nobreaks.append(nobreak)
        return nobreak, 201

class Switches(Resource):
    def get(self):
        return switches

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("tag", type=str, required=True)
        parser.add_argument("modelo", type=str, required=True)
        parser.add_argument("marca", type=str, required=True)
        parser.add_argument("qtdPortas", type=int, required=True)
        args = parser.parse_args()

        switch = {
            "id": len(switches) + 1,
            "tag": args["tag"],
            "modelo": args["modelo"],
            "marca": args["marca"],
            "qtdPortas": args["qtdPortas"]
        }
        switches.append(switch)
        return switch, 201
    
api.add_resource(Ativos, "/ativos")
api.add_resource(Exaustores, "/exaustores")
api.add_resource(Nobreaks, "/nobreaks")
api.add_resource(Switches, "/switches")

if __name__ == "__main__":
    app.run(debug=True)
