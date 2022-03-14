from main import db


class Division(db.Model):
    __tablename__ = 'division'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)


class Ciudad(db.Model):
    __tablename__ = 'ciudad'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)


class Equipo(db.Model):

    __tablename__ = 'equipo'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    num_jugadores = db.Column(db.Integer, nullable=False)
    ciudad = db.Column(db.Integer, db.ForeignKey('ciudad.id'))
    division = db.Column(db.Integer, db.ForeignKey('division.id'))


class Jugador(db.Model):

    __tablename__ = 'jugador'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    sueldo = db.Column(db.BigInteger, nullable=False)
    tr = db.Column(db.Integer, nullable=False)
    ta = db.Column(db.Integer, nullable=False)
    goles = db.Column(db.Integer, nullable=False)
    pj = db.Column(db.Integer, nullable=False)
    id_equipo = db.Column(db.Integer, db.ForeignKey('equipo.id'))


class Partido(db.Model):

    __tablename__ = 'partido'
    id = db.Column(db.Integer, primary_key=True)
    equipo_local = db.Column(db.Integer, db.ForeignKey('equipo.id'))
    equipo_visitante = db.Column(db.Integer, db.ForeignKey('equipo.id'))
    goles_local = db.Column(db.Integer, nullable=False)
    goles_visitante = db.Column(db.Integer, nullable=False)
