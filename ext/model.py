from ext.config import db


def init_app(app):

    class Sales(db.Model):
        id = db.Column(db.Integer, primary_key= True)
        value = db.Column(db.String(50))
        monthyPrice = db.Column(db.String(50))
        setupPrice = db.Column(db.String(50))
        currency = db.Column(db.String(50))

        def to_json(self):
            return {"id": self.id, "value": self.value, "monthyPrice": self.monthyPrice, "setuPrice": self.setupPrince, "currency": self.currency} 
