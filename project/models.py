from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Bassins(db.Model):
    __tablename__ = 'Bassins'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    libelle = db.Column(db.String(100))
    surface = db.Column(db.Float)
    profondeur = db.Column(db.Float)
    volume = db.Column(db.Float)
    type_aliment = db.Column(db.String(1000))
    cycles = db.relationship('Cycles', backref='Bassins', lazy=True)

class Croissance(db.Model):
    __tablename__ = 'Croissance'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    espece = db.Column(db.String(100))
    semaine = db.Column(db.Integer)
    quantite_lb = db.Column(db.Integer)
    pc_aliment = db.Column(db.Float)
    gr_poisson = db.Column(db.Integer)

class Especes(db.Model):
    __tablename__ = 'Especes'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    espece = db.Column(db.String(100))
    libelle = db.Column(db.String(100))

class Mortalite(db.Model):
    __tablename__ = 'Mortalite'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    espece = db.Column(db.String(100))
    taux_initial = db.Column(db.Float)
    taux_hebdomadaire = db.Column(db.Float)

class Cycles(db.Model):
    __tablename__ = 'Cycles'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    lots = db.relationship('Lots', backref='Lots', lazy=True)
    bassin_id = db.Column(db.Integer, db.ForeignKey('Bassins.id'), nullable=False)

class Lots(db.Model):
    __tablename__ = 'Lots'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    cycle_id = db.Column(db.Integer, db.ForeignKey('Cycles.id'), nullable=False)
    espece_id = db.Column(db.Integer, db.ForeignKey('Especes.id'), nullable=False)
    peches = db.relationship('Peches', backref='Lots', lazy=True)
    semis = db.relationship('Semis', backref='Lots', lazy=True)
    statistique = db.relationship('Statistique', backref='Lots', lazy=True)
    termine = db.Column(db.Boolean)
    date_stat = db.Column(db.DateTime)
    date_semis = db.Column(db.DateTime)
    date_peche = db.Column(db.DateTime)
    type_stat = db.Column(db.Integer)
    commentaire = db.Column(db.Text)
    quant_semee = db.Column(db.Integer)
    quant_semeenet = db.Column(db.Integer) 
    quant_mort = db.Column(db.Integer) 
    taux_mortalité = db.Column(db.Integer) 
    quant_pechee = db.Column(db.Integer) # ICI problème 

class Peches(db.Model):
    __tablename__ = 'Peches'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    lot_id = db.Column(db.Integer, db.ForeignKey('Lots.id'), nullable=False)
    date = db.Column(db.DateTime)
    poids = db.Column(db.Float) # ICI PROBLEME QUANTITE/LB etc..
    commentaire = db.Column(db.Text)
    destination = db.Column(db.String(100))

class Semis(db.Model):
    __tablename__ = 'Semis'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    lot_id = db.Column(db.Integer, db.ForeignKey('Lots.id'), nullable=False)
    date = db.Column(db.DateTime)
    quantite = db.Column(db.Integer)
    poids = db.Column(db.Float) # ICI PROBLEME QUANTITE/LB etc..
    commentaire = db.Column(db.Text)
    destination = db.Column(db.String(100))

class Statistique(db.Model):
    __tablename__ = 'Statistique'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    lot_id = db.Column(db.Integer, db.ForeignKey('Lots.id'), nullable=False)
    date = db.Column(db.DateTime)
    quantite = db.Column(db.Integer)
    poids = db.Column(db.Float) # ICI PROBLEME QUANTITE/LB etc..
    commentaire = db.Column(db.Text)
    destination = db.Column(db.String(100))