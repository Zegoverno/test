from ardui_server import db

class Medida(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	valor = db.Column(db.Integer)
