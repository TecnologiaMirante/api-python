from flask import Flask, request
from flask_restful import Api, Resource, reqparse, jsonify

app = Flask(__name__)
api = Api(app)

ativos = []
exaustores = []
nobreaks = []
switches = []
telemetrias = []
dps_list = []
disjuntores = []
antenas = []
id_antena = 0

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

class Telemetria:
    def __init__(self, tag, modelo, marca, id_criacao):
        self.tag = tag
        self.modelo = modelo
        self.marca = marca
        self.id_criacao = id_criacao

# Listar todas as telemetrias
@app.route('/telemetrias', methods=['GET'])
def get_telemetrias():
    return jsonify({'telemetrias': [t.__dict__ for t in telemetrias]})

# Obter uma telemetria pelo id
@app.route('/telemetrias/<int:id>', methods=['GET'])
def get_telemetria(id):
    telemetria = [t for t in telemetrias if t.id_criacao == id]
    if len(telemetria) == 0:
        return jsonify({'erro': 'Telemetria não encontrada'}), 404
    return jsonify(telemetria[0].__dict__)

# Criar uma nova telemetria
@app.route('/telemetrias', methods=['POST'])
def create_telemetria():
    data = request.json

    nova_telemetria = Telemetria(data['tag'], data['modelo'], data['marca'], data['id_criacao'])

    telemetrias.append(nova_telemetria)

    return jsonify(nova_telemetria.__dict__), 201

# Atualizar uma telemetria existente
@app.route('/telemetrias/<int:id>', methods=['PUT'])
def update_telemetria(id):
    telemetria = [t for t in telemetrias if t.id_criacao == id]
    if len(telemetria) == 0:
        return jsonify({'erro': 'Telemetria não encontrada'}), 404

    data = request.json
    telemetria[0].tag = data.get('tag', telemetria[0].tag)
    telemetria[0].modelo = data.get('modelo', telemetria[0].modelo)
    telemetria[0].marca = data.get('marca', telemetria[0].marca)

    return jsonify(telemetria[0].__dict__)

# Excluir uma telemetria existente
@app.route('/telemetrias/<int:id>', methods=['DELETE'])
def delete_telemetria(id):
    global telemetrias
    telemetrias = [t for t in telemetrias if t.id_criacao != id]
    return '', 204

class DPS:
    def __init__(self, tag, marca, modelo, corrente_maxima, classe, id):
        self.tag = tag
        self.marca = marca
        self.modelo = modelo
        self.corrente_maxima = corrente_maxima
        self.classe = classe
        self.id = id
# Função para criar um novo DPS
def create_dps(tag, marca, modelo, corrente_maxima, classe):
    dps = {'id': len(dps_list) + 1, 'tag': tag, 'marca': marca, 'modelo': modelo, 'corrente_maxima': corrente_maxima, 'classe': classe}
    dps_list.append(dps)
    return dps

# Função para listar todos os DPSs cadastrados
def get_all_dps():
    return dps_list

# Função para buscar um DPS pelo ID
def get_dps_by_id(id):
    for dps in dps_list:
        if dps['id'] == id:
            return dps
    return None

# Função para atualizar os dados de um DPS existente
def update_dps(id, tag=None, marca=None, modelo=None, corrente_maxima=None, classe=None):
    dps = get_dps_by_id(id)
    if dps:
        if tag:
            dps['tag'] = tag
        if marca:
            dps['marca'] = marca
        if modelo:
            dps['modelo'] = modelo
        if corrente_maxima:
            dps['corrente_maxima'] = corrente_maxima
        if classe:
            dps['classe'] = classe
        return dps
    return None

# Função para remover um DPS pelo ID
def delete_dps(id):
    dps = get_dps_by_id(id)
    if dps:
        dps_list.remove(dps)
        return dps
    return None

# Rotas da API
@app.route('/dps', methods=['POST'])
def create():
    tag = request.json['tag']
    marca = request.json['marca']
    modelo = request.json['modelo']
    corrente_maxima = request.json['corrente_maxima']
    classe = request.json['classe']
    dps = create_dps(tag, marca, modelo, corrente_maxima, classe)
    return jsonify(dps)

@app.route('/dps', methods=['GET'])
def read_all():
    dps = get_all_dps()
    return jsonify(dps)

@app.route('/dps/<int:id>', methods=['GET'])
def read(id):
    dps = get_dps_by_id(id)
    if dps:
        return jsonify(dps)
    return jsonify({'error': 'DPS not found'})

@app.route('/dps/<int:id>', methods=['PUT'])
def update(id):
    tag = request.json.get('tag')
    marca = request.json.get('marca')
    modelo = request.json.get('modelo')
    corrente_maxima = request.json.get('corrente_maxima')
    classe = request.json.get('classe')
    dps = update_dps(id, tag, marca, modelo, corrente_maxima, classe)
    if dps:
        return jsonify(dps)
    return jsonify({'error': 'DPS not found'})

@app.route('/dps/<int:id>', methods=['DELETE'])
def delete(id):
    dps = delete_dps(id)
    if dps:
        return jsonify(dps)
    return jsonify({'error': 'DPS not found'})

class Disjuntor:
    def __init__(self, tag, marca, modelo, corrente_maxima, id):
        self.tag = tag
        self.marca = marca
        self.modelo = modelo
        self.corrente_maxima = corrente_maxima
        self.id = id

# Create
@app.route('/disjuntores', methods=['POST'])
def create_disjuntor():
    data = request.get_json()
    tag = data['tag']
    marca = data['marca']
    modelo = data['modelo']
    corrente_maxima = data['corrente_maxima']
    id = len(disjuntores) + 1
    disjuntor = {'tag': tag, 'marca': marca, 'modelo': modelo, 'corrente_maxima': corrente_maxima, 'id': id}
    disjuntores.append(disjuntor)
    return jsonify(disjuntor)

# Read all
@app.route('/disjuntores', methods=['GET'])
def get_all_disjuntores():
    return jsonify(disjuntores)

# Read one
@app.route('/disjuntores/<int:id>', methods=['GET'])
def get_disjuntor(id):
    for disjuntor in disjuntores:
        if disjuntor['id'] == id:
            return jsonify(disjuntor)
    return jsonify({'error': 'Disjuntor não encontrado'})

# Update
@app.route('/disjuntores/<int:id>', methods=['PUT'])
def update_disjuntor(id):
    for disjuntor in disjuntores:
        if disjuntor['id'] == id:
            data = request.get_json()
            disjuntor['tag'] = data['tag']
            disjuntor['marca'] = data['marca']
            disjuntor['modelo'] = data['modelo']
            disjuntor['corrente_maxima'] = data['corrente_maxima']
            return jsonify(disjuntor)
    return jsonify({'error': 'Disjuntor não encontrado'})

# Delete
@app.route('/disjuntores/<int:id>', methods=['DELETE'])
def delete_disjuntor(id):
    for disjuntor in disjuntores:
        if disjuntor['id'] == id:
            disjuntores.remove(disjuntor)
            return jsonify({'message': 'Disjuntor removido com sucesso'})
    return jsonify({'error': 'Disjuntor não encontrado'})


class Parabolica:
    def __init__(self, tag, marca, modelo, diametro, satelite, receptor, id):
        self.tag = tag
        self.marca = marca
        self.modelo = modelo
        self.diametro = diametro
        self.satelite = satelite
        self.receptor = receptor
        self.id = id

class ParabolicaCRUD:
    def __init__(self):
        self.parabolicas = []
        self.next_id = 1

    def criar(self, parabolica):
        parabolica.id = self.next_id
        self.parabolicas.append(parabolica)
        self.next_id += 1

    def listar(self):
        return self.parabolicas

    def buscar_por_id(self, id):
        for parabolica in self.parabolicas:
            if parabolica.id == id:
                return parabolica
        return None

    def atualizar(self, id, novos_dados):
        parabolica = self.buscar_por_id(id)
        if parabolica:
            parabolica.tag = novos_dados.get('tag', parabolica.tag)
            parabolica.marca = novos_dados.get('marca', parabolica.marca)
            parabolica.modelo = novos_dados.get('modelo', parabolica.modelo)
            parabolica.diametro = novos_dados.get('diametro', parabolica.diametro)
            parabolica.satelite = novos_dados.get('satelite', parabolica.satelite)
            parabolica.receptor = novos_dados.get('receptor', parabolica.receptor)
            return True
        return False

    def deletar(self, id):
        parabolica = self.buscar_por_id(id)
        if parabolica:
            self.parabolicas.remove(parabolica)
            return True
        return False
    
class Receptor:
    def __init__(self, tag, marca, modelo, channel, frequency, symbol_rate, transmitter, parabolic, id):
        self.tag = tag
        self.marca = marca
        self.modelo = modelo
        self.channel = channel
        self.frequency = frequency
        self.symbol_rate = symbol_rate
        self.transmitter = transmitter
        self.parabolic = parabolic
        self.id = id

class ReceptorDAO:
    def __init__(self):
        self.receptores = []
        self.next_id = 1

    def listar(self):
        return self.receptores

    def buscar_por_id(self, id):
        for receptor in self.receptores:
            if receptor.id == id:
                return receptor
        return None

    def cadastrar(self, receptor):
        receptor.id = self.next_id
        self.receptores.append(receptor)
        self.next_id += 1

    def atualizar(self, id, receptor_novo):
        receptor_antigo = self.buscar_por_id(id)
        if receptor_antigo:
            receptor_antigo.tag = receptor_novo.tag
            receptor_antigo.marca = receptor_novo.marca
            receptor_antigo.modelo = receptor_novo.modelo
            receptor_antigo.channel = receptor_novo.channel
            receptor_antigo.frequency = receptor_novo.frequency
            receptor_antigo.symbol_rate = receptor_novo.symbol_rate
            receptor_antigo.transmitter = receptor_novo.transmitter
            receptor_antigo.parabolic = receptor_novo.parabolic
            return True
        return False

    def remover(self, id):
        receptor = self.buscar_por_id(id)
        if receptor:
            self.receptores.remove(receptor)
            return True
        return False


class Transmissor:
    def __init__(self, tag, marca, modelo, programmed_power, canal_fisico, canal_virtual, receptor, antena, id):
        self.tag = tag
        self.marca = marca
        self.modelo = modelo
        self.programmed_power = programmed_power
        self.canal_fisico = canal_fisico
        self.canal_virtual = canal_virtual
        self.receptor = receptor
        self.antena = antena
        self.id = id
        self.transmissores = []

    def cadastrar_transmissor(self, transmissor):
        self.transmissores.append(transmissor)

    def buscar_transmissor(self, id):
        for transmissor in self.transmissores:
            if transmissor.id == id:
                return transmissor
        return None

    def listar_transmissores(self):
        return self.transmissores

    def atualizar_transmissor(self, id, dados):
        for transmissor in self.transmissores:
            if transmissor.id == id:
                transmissor.tag = dados.get('tag', transmissor.tag)
                transmissor.marca = dados.get('marca', transmissor.marca)
                transmissor.modelo = dados.get('modelo', transmissor.modelo)
                transmissor.programmed_power = dados.get('programmed_power', transmissor.programmed_power)
                transmissor.canal_fisico = dados.get('canal_fisico', transmissor.canal_fisico)
                transmissor.canal_virtual = dados.get('canal_virtual', transmissor.canal_virtual)
                transmissor.receptor = dados.get('receptor', transmissor.receptor)
                transmissor.antena = dados.get('antena', transmissor.antena)
                return True
        return False

    def deletar_transmissor(self, id):
        for transmissor in self.transmissores:
            if transmissor.id == id:
                self.transmissores.remove(transmissor)
                return True
        return False

class Combinador:
    def __init__(self, tag, marca, modelo, id):
        self.tag = tag
        self.marca = marca
        self.modelo = modelo
        self.id = id
        self.combinadores = []

    def cadastrar(self, tag, marca, modelo, id):
        combinador = Combinador(tag, marca, modelo, id)
        self.combinadores.append(combinador)
        return combinador

    def listar(self):
        return self.combinadores

    def buscar(self, id):
        for combinador in self.combinadores:
            if combinador.id == id:
                return combinador
        return None

    def atualizar(self, id, tag=None, marca=None, modelo=None):
        combinador = self.buscar(id)
        if combinador:
            combinador.tag = tag if tag is not None else combinador.tag
            combinador.marca = marca if marca is not None else combinador.marca
            combinador.modelo = modelo if modelo is not None else combinador.modelo
            return combinador
        return None

    def deletar(self, id):
        combinador = self.buscar(id)
        if combinador:
            self.combinadores.remove(combinador)
            return True
        return False

class Cabo:
    def __init__(self, tag, marca, modelo, tipo, tamanho, id):
        self.tag = tag
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.tamanho = tamanho
        self.id = id
        
class CaboDAO:
    def __init__(self):
        self.cabos = []
        self.id_counter = 1
        
    def listar(self):
        return self.cabos
    
    def buscar_por_id(self, id):
        for cabo in self.cabos:
            if cabo.id == id:
                return cabo
        return None
    
    def criar(self, cabo):
        cabo.id = self.id_counter
        self.cabos.append(cabo)
        self.id_counter += 1
    
    def atualizar(self, id, novo_cabo):
        for i in range(len(self.cabos)):
            if self.cabos[i].id == id:
                novo_cabo.id = id
                self.cabos[i] = novo_cabo
                return True
        return False
    
    def deletar(self, id):
        for i in range(len(self.cabos)):
            if self.cabos[i].id == id:
                self.cabos.pop(i)
                return True
        return False

class Torre:
    def __init__(self, tag, marca, modelo, tipo, altura, aterramento, id):
        self.tag = tag
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.altura = altura
        self.aterramento = aterramento
        self.id = id

class TorreCRUD:
    def __init__(self):
        self.torres = []
        self.next_id = 1
    
    # Create operation
    def create(self, torre):
        torre.id = self.next_id
        self.torres.append(torre)
        self.next_id += 1
        return torre
    
    # Read operations
    def read_all(self):
        return self.torres
    
    def read_by_id(self, id):
        for torre in self.torres:
            if torre.id == id:
                return torre
        return None
    
    # Update operation
    def update(self, torre):
        for i in range(len(self.torres)):
            if self.torres[i].id == torre.id:
                self.torres[i] = torre
                return torre
        return None
    
    # Delete operation
    def delete(self, id):
        for i in range(len(self.torres)):
            if self.torres[i].id == id:
                return self.torres.pop(i)
        return None

# Classe Antena
class Antena:
    def __init__(self, tag, marca, modelo, tipo, altura, aterramento, id):
        self.tag = tag
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.altura = altura
        self.aterramento = aterramento
        self.id = id


# Rotas da API

# Criar antena
@app.route('/antenas', methods=['POST'])
def criar_antena():
    global id_antena
    data = request.get_json()
    antena = Antena(tag=data['tag'], marca=data['marca'], modelo=data['modelo'], tipo=data['tipo'],
                    altura=data['altura'], aterramento=data['aterramento'], id=id_antena)
    antenas.append(antena)
    id_antena += 1
    return jsonify({'mensagem': 'Antena criada com sucesso.'})


# Listar antenas
@app.route('/antenas', methods=['GET'])
def listar_antenas():
    lista_antenas = []
    for antena in antenas:
        lista_antenas.append({'id': antena.id, 'tag': antena.tag, 'marca': antena.marca, 'modelo': antena.modelo,
                              'tipo': antena.tipo, 'altura': antena.altura, 'aterramento': antena.aterramento})
    return jsonify(lista_antenas)


# Buscar antena pelo ID
@app.route('/antenas/<int:id>', methods=['GET'])
def buscar_antena(id):
    for antena in antenas:
        if antena.id == id:
            return jsonify({'id': antena.id, 'tag': antena.tag, 'marca': antena.marca, 'modelo': antena.modelo,
                            'tipo': antena.tipo, 'altura': antena.altura, 'aterramento': antena.aterramento})
    return jsonify({'mensagem': 'Antena não encontrada.'})


# Atualizar antena pelo ID
@app.route('/antenas/<int:id>', methods=['PUT'])
def atualizar_antena(id):
    for antena in antenas:
        if antena.id == id:
            data = request.get_json()
            antena.tag = data['tag']
            antena.marca = data['marca']
            antena.modelo = data['modelo']
            antena.tipo = data['tipo']
            antena.altura = data['altura']
            antena.aterramento = data['aterramento']
            return jsonify({'mensagem': 'Antena atualizada com sucesso.'})
    return jsonify({'mensagem': 'Antena não encontrada.'})


# Excluir antena pelo ID
@app.route('/antenas/<int:id>', methods=['DELETE'])
def excluir_antena(id):
    for antena in antenas:
        if antena.id == id:
            antenas.remove(antena)
            return jsonify({'mensagem': 'Antena excluída com sucesso.'})
    return jsonify({'mensagem': 'Antena não encontrada.'})
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