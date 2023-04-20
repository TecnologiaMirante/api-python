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

    def put(self, ativo_id):
        parser = reqparse.RequestParser()
        parser.add_argument("tag", type=str, required=True)
        parser.add_argument("modelo", type=str, required=True)
        parser.add_argument("marca", type=str, required=True)
        parser.add_argument("potencia", type=int, required=True)
        parser.add_argument("tensao", type=int, required=True)
        args = parser.parse_args()

        for ativo in ativos:
            if ativo["id"] == ativo_id:
                ativo["tag"] = args["tag"]
                ativo["modelo"] = args["modelo"]
                ativo["marca"] = args["marca"]
                ativo["potencia"] = args["potencia"]
                ativo["tensao"] = args["tensao"]
                return ativo, 200
        ativo = {
            "id": ativo_id,
            "tag": args["tag"],
            "modelo": args["modelo"],
            "marca": args["marca"],
            "potencia": args["potencia"],
            "tensao": args["tensao"]
        }
        ativos.append(ativo)
        return ativo, 201

    def delete(self, ativo_id):
        global ativos
        ativos = [ativo for ativo in ativos if ativo["id"] != ativo_id]
        return '', 204
class Ativo(Resource):
    def get(self, ativo_id):
        for ativo in ativos:
            if ativo["id"] == ativo_id:
                return ativo, 200
        return "Ativo not found", 404
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

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("tag", type=str, required=True)
        parser.add_argument("modelo", type=str, required=True)
        parser.add_argument("marca", type=str, required=True)
        args = parser.parse_args()

        for exaustor in exaustores:
            if exaustor["id"] == id:
                exaustor["tag"] = args["tag"]
                exaustor["modelo"] = args["modelo"]
                exaustor["marca"] = args["marca"]
                return exaustor, 200
        exaustor = {
            "id": len(exaustores) + 1,
            "tag": args["tag"],
            "modelo": args["modelo"],
            "marca": args["marca"]
        }
        exaustores.append(exaustor)
        return exaustor, 201

    def delete(self, id):
        global exaustores
        exaustores = [exaustor for exaustor in exaustores if exaustor["id"] != id]
        return '', 204
class Nobreak(Resource):
    def get(self, nobreak_id=None):
        if nobreak_id:
            nobreak = next((nobreak for nobreak in nobreaks if nobreak["id"] == nobreak_id), None)
            if nobreak:
                return nobreak, 200
            return {"message": f"Nobreak com id {nobreak_id} não encontrado."}, 404
        return nobreaks, 200

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

    def put(self, nobreak_id):
        nobreak = next((nobreak for nobreak in nobreaks if nobreak["id"] == nobreak_id), None)
        if nobreak:
            parser = reqparse.RequestParser()
            parser.add_argument("tag", type=str)
            parser.add_argument("modelo", type=str)
            parser.add_argument("marca", type=str)
            parser.add_argument("tensaoEntrada", type=int)
            parser.add_argument("tensaoSaida", type=int)
            args = parser.parse_args()

            if args["tag"]:
                nobreak["tag"] = args["tag"]
            if args["modelo"]:
                nobreak["modelo"] = args["modelo"]
            if args["marca"]:
                nobreak["marca"] = args["marca"]
            if args["tensaoEntrada"]:
                nobreak["tensaoEntrada"] = args["tensaoEntrada"]
            if args["tensaoSaida"]:
                nobreak["tensaoSaida"] = args["tensaoSaida"]
            
            return nobreak, 200
        return {"message": f"Nobreak com id {nobreak_id} não encontrado."}, 404

    def delete(self, nobreak_id):
        global nobreaks
        nobreaks = [nobreak for nobreak in nobreaks if nobreak["id"] != nobreak_id]
        return {"message": f"Nobreak com id {nobreak_id} deletado com sucesso."}, 200
class Switches(Resource):
    def get(self, id=None):
        if id:
            for switch in switches:
                if switch["id"] == id:
                    return switch
            return {"message": "Switch not found"}, 404
        else:
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

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("tag", type=str)
        parser.add_argument("modelo", type=str)
        parser.add_argument("marca", type=str)
        parser.add_argument("qtdPortas", type=int)
        args = parser.parse_args()

        for switch in switches:
            if switch["id"] == id:
                if args["tag"]:
                    switch["tag"] = args["tag"]
                if args["modelo"]:
                    switch["modelo"] = args["modelo"]
                if args["marca"]:
                    switch["marca"] = args["marca"]
                if args["qtdPortas"]:
                    switch["qtdPortas"] = args["qtdPortas"]
                return switch, 200
        return {"message": "Switch not found"}, 404

    def delete(self, id):
        for i, switch in enumerate(switches):
            if switch["id"] == id:
                switches.pop(i)
                return {"message": "Switch deleted successfully"}, 200
        return {"message": "Switch not found"}, 404
#routes     
api.add_resource(Ativos, "/ativos")
api.add_resource(Ativo, "/ativos/<int:ativo_id>")

api.add_resource(Exaustores, "/exaustores/<int:id>")
api.add_resource(Nobreak, "/nobreaks", "/nobreaks/<int:nobreak_id>")
api.add_resource(Switches, "/switches", "/switches/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)

# GET /exaustores: retorna uma lista de todos os exaustores
# POST /exaustores: adiciona um novo exaustor
# PUT /exaustores/<int:id>: atualiza o exaustor com o ID especificado
# DELETE /exaustores/<int:id>: exclui o exaustor com o ID especificado