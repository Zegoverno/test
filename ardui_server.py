from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ardui.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

from serial_ardui import *
from model_ardui import *


@app.route('/')
def index():
	return "hello, pot"


@app.route('/historico', methods=['GET'])
def lista_medidas():
	valores = []
	for i in Medida.query.all():
		print i.valor
		valores.append({'id': i.id, 'valor': i.valor})

	return json.dumps(valores)


@app.route('/pega_valor', methods=['GET'])
def pega_valor():
	a = Medida()
	a.valor = read_pot()
	db.session.add(a)
	db.session.commit()

	return jsonify({'status:': True})


if __name__ == '__main__':
	app.run(debug=True)
