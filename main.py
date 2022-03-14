from models import *
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,Blueprint, render_template, request


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


m = Blueprint('main', __name__)


@m.route('/')
def index():
    if request.method == 'POST':
        print("a")
    jugadores1 = Jugador.query.all()
    equipos1 = Equipo.query.all()
    equipos = []
    jugadores = []
    for e in equipos1:
        equipos.append({"id": e.id, "nombre": e.nombre, "num_jugadores": e.num_jugadores,
                        "ciudad": Ciudad.query.filter(Ciudad.id == e.ciudad).one().nombre,
                        "division": Division.query.filter(Division.id == e.division).one().nombre})
    for e in jugadores1:
        jugadores.append({"id": e.id, "nombre": e.nombre,
                          "equipo": Equipo.query.filter(Equipo.id == e.id_equipo).one().nombre,
                          "edad": e.edad, "sueldo": e.sueldo, "tr": e.tr, "ta": e.ta,
                          "goles": e.goles, "pj": e.pj})
    ciudades = Ciudad.query.all()
    return render_template('index.html', ciudades=ciudades, equipos=equipos, jugadores=jugadores)


app.register_blueprint(m)

if __name__ == '__main__':
    app.run(debug=True)
