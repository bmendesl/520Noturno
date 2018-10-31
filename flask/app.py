#pip3 install flask

from flask import Flask, jsonify
from pymongo import MongoClient
import requests 

con = MongoClient()
db = con['aulamongo']

app = Flask(__name__)

@app.route('/')
def index():
    mensagem = {'mensagem': "minha primeira pagina"}
    return jsonify(mensagem)

@app.route('/usuarios')
def usuarios():
    usuarios = []
    for x in db.usuarios.find():
        usuarios.append(x)
    return jsonify(usuarios)
    #return jsonify([x for x in db.usuarios.find()])

@app.route('/cep/<busca>')
def clonaapi(busca):
    date = requests.get('https://viacep.com.br/ws/{}/json/'.format(busca))
    return jsonify(date.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
