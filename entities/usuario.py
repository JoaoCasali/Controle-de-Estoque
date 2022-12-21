from config import db


class Usuarios(db.Model):
    __tablename__ = "usuarios"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NOM_PES = db.Column(db.String(200), nullable=False)
    SENHA = db.Column(db.String(200), nullable=False)
    DTA_NAS = db.Column(db.String(200), nullable=False)
