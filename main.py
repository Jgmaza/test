from models import *
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Blueprint, render_template, request


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


m = Blueprint('main', __name__)


@m.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            eloc = int(request.form['e-loc']) - 1
            evis = int(request.form['e-vis']) - 1
            loc = int(request.form['loc'])
            vis = int(request.form['vis'])
            c = Partido(equipo_local=eloc,
                        equipo_visitante=evis,
                        goles_local=loc,
                        goles_visitante=vis)
            db.session.merge(c)
            db.session.commit()
        except:
            try:
                ciudad = int(request.form['ciudad']) - 1
                division = int(request.form['division']) - 1
                nombre = (request.form['nombre'])
                num = int(request.form['num_jugadores'])
                c = Equipo(nombre=nombre,
                           num_jugadores=num,
                           division=division,
                           ciudad=ciudad)
                db.session.merge(c)
                db.session.commit()
            except:
                try:
                    equipo = int(request.form['equipo']) - 1
                    e = Equipo.query.filter(Equipo.id == equipo).one()
                    e.num_jugadores += 1
                    db.session.merge(e)
                    db.session.commit()
                    nombre = (request.form['nombre'])
                    edad = int(request.form['edad'])
                    sueldo = int(request.form['sueldo'])
                    tr = int(request.form['tr'])
                    ta = int(request.form['ta'])
                    goles = int(request.form['goles'])
                    pj = int(request.form['pj'])
                    c = Jugador(nombre=nombre,
                                id_equipo=equipo,
                                edad=edad,
                                sueldo=sueldo,
                                tr=tr, ta=ta,
                                goles=goles, pj=pj)
                    db.session.merge(c)
                    db.session.commit()
                except:
                    print("F")

    partidos1 = Partido.query.all()
    equipos1 = Equipo.query.all()
    puntoEquipo = []
    for e in equipos1:
        pj = 0
        pg = 0
        pp = 0
        pe = 0
        goles= 0
        for i in partidos1:
            if i.equipo_local == e.id:
                pj += 1
                if i.goles_local > i.goles_visitante:
                    pg += 1
                    goles += i.goles_local
                elif i.goles_local < i.goles_visitante:
                    pp += 1
                else:
                    pe +=1
            elif i.equipo_visitante == e.id:
                pj += 1
                if i.goles_local > i.goles_visitante:
                    pp += 1                   
                elif i.goles_local < i.goles_visitante:
                    pg += 1
                    goles += i.goles_local
                else:
                    pe +=1
            

        puntoEquipo.append({"nombre": e.nombre, "pj": pj,
                           "pg": pg, "pp": pp, "goles":goles,"puntos": 3*pg + pe})
    puntoEquipo = sorted(puntoEquipo, key=lambda x: x["puntos"], reverse=True)

    jugadores1 = Jugador.query.all()

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
    divisiones = Division.query.all()
    return render_template('index.html', puntoEquipo=puntoEquipo, divisiones=divisiones, ciudades=ciudades, equipos=equipos, jugadores=jugadores)


app.register_blueprint(m)

if __name__ == '__main__':
    app.run(debug=True)
