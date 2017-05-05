from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/check_user/envs/prueba.db'
db = SQLAlchemy(app)


class Datos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consumoCpu = db.Column(db.String(80), nullable=False)
    consumoRam = db.Column(db.String(120), nullable=False)
    espacioDisco = db.Column(db.String(120), nullable=False)
    service = db.Column(db.String(120), nullable=False)


    def __init__(self,consumoCpu,consumoRam, espacioDisco, service):
        self.consumoCpu = consumoCpu
        self.consumoRam = consumoRam
        self.espacioDisco = espacioDisco
        self.service = service

    def __repr__(self):
	informacion = self.consumoCpu +" " + self.consumoRam + " " + self.espacioDisco+ " " + self.service

        return '<informacion %r>' % informacion
