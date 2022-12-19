from main import db
class Produto(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    produtos = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name