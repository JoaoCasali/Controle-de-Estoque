from main import db
class Produto(db.Model):
    
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    DSC_PRO = db.Column(db.String(200), nullable=False)
    MRC_DSC = db.Column(db.String(200), nullable=False)
    UNI_MED = db.Column(db.String(50), nullable=False)
    PRC_BRT = db.Column(db.Float, nullable=False)
    #USU_ID = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name