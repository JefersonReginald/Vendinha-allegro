from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Sale {self.item}, Quantity: {self.quantity}, Price: {self.price}>'
