from config import db


class Estoque(db.Model):
    __tablename__ = "estoque"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PRO_ID = db.Column(db.Integer, db.ForeignKey('produtos.ID'))
    QTD_PRO = db.Column(db.String(200), nullable=False)
    USU_ID = db.Column(db.Integer, db.ForeignKey('usuarios.ID'))

    def __repr__(self):
        return '<Name %r>' % self.name
