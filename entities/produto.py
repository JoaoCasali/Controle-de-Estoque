from config import db


class Produtos(db.Model):
    __tablename__ = "produtos"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    DSC_PRO = db.Column(db.String(200), nullable=False)
    MRC_DSC = db.Column(db.String(200), nullable=False)
    UNI_MED = db.Column(db.String(50), nullable=False)
    PRC_BRT = db.Column(db.Float, nullable=False)
    USU_ID = db.Column(db.Integer, db.ForeignKey('usuario.id'))

    def __repr__(self):
        return '<Name %r>' % self.name
