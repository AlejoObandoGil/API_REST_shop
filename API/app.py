# python 3.7 Flask
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

# Diccionario de clientes 
clients = [
    {
    'cedula': "1127537146",
    'nombre': "Alejandro",
    'apellido': "Obando",
    'email': "john.obando@utp.edu.co",
    'telefono': "3333335",
    'direccion': "cra 28 #65-97"
    },
    {
    'cedula': "1080905060",
    'nombre': "Natalia",
    'apellido': "Rios",
    'email': "natalia.rios@utp.edu.co",
    'telefono': "3355555",
    'direccion': "cra 1 #30-22"
    }
]

# Index
@app.route('/')
def index():

    return "Hello, World!"


# Listar clientes
@app.route('/api/get/clients', methods=['GET'])
def get_clients():

    return jsonify({'clients': clients})


# Buscar cliente
@app.route('/api/get/<client_id>', methods=['GET'])
def get_client(client_id):
    client = [client for client in clients if client['cedula'] == client_id]
    if len(client) == 0:
        abort(404)

    return jsonify({'client': client[0]})


# Error 404
@app.errorhandler(404)
def not_found(error):

    return make_response(jsonify({'error': 'Not found'}), 404)


# Crear cliente
@app.route('/api/post/clients', methods=['POST'])
def create_client():
    print ("Recibido")
    print(request.json)
    if not request.json or not 'nombre' in request.json:
        abort(400)
    client = {
        'cedula': request.json.get('cedula', request.json['cedula']),
        'nombre': request.json.get('nombre', request.json['nombre']),
        'apellido': request.json.get('apellido', request.json['apellido']),
        'email': request.json.get('email', request.json['email']),
        'telefono': request.json.get('telefono', request.json['telefono']),
        'direccion': request.json.get('direccion', request.json['direccion'])
    }
    clients.append(client)

    return jsonify({'client': client}), 201


# Actualizar cliente
@app.route('/api/update/<client_id>', methods=['PUT'])
def update_client(client_id):
    client = [client for client in clients if client['cedula'] == client_id]
    print(request.json)
    print(type(request.json['nombre']))
    if len(client) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'cedula' in request.json and isinstance(request.json['cedula'],str) == False:
        abort(400)        
    if 'nombre' in request.json and isinstance(request.json['nombre'],str) == False:
        abort(400)
    if 'apellido' in request.json and isinstance(request.json['apellido'],str) == False:
        abort(400)
    if 'email' in request.json and isinstance(request.json['email'],str) == False:
        abort(400)
    if 'telefono' in request.json and isinstance(request.json['telefono'],str) == False:
        abort(400)                
    if 'direccion' in request.json and isinstance(request.json['direccion'],str) == False:
        abort(400)

    client[0]['cedula'] = request.json.get('cedula', client[0]['cedula'])        
    client[0]['nombre'] = request.json.get('nombre', client[0]['nombre'])
    client[0]['apellido'] = request.json.get('apellido', client[0]['apellido'])
    client[0]['email'] = request.json.get('email', client[0]['email'])
    client[0]['telefono'] = request.json.get('telefono', client[0]['telefono'])
    client[0]['direccion'] = request.json.get('direccion', client[0]['direccion'])

    return jsonify({'client': client[0]})


# Eliminar cliente
@app.route('/api/delete/clients/<client_id>', methods=['DELETE'])
def delete_client(client_id):
    client = [client for client in clients if client['cedula'] == client_id]
    if len(client) == 0:
        abort(404)
    clients.remove(client[0])

    return jsonify({'result': True})


# main
if __name__ == '__main__':
    #app.run(host='127.0.0.1',debug=True)
    app.run(debug=True)
