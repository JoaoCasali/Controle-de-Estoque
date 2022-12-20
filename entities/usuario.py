from config import db

class Usuario(db.Model):
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NOM_PES = db.Column(db.Varchar(200), nullable=False)
    SENHA = db.Column(db.Varchar(200), nullable=False)
    DTA_NAS = db.Column(db.Varchar(200), nullable=False)