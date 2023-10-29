from pytodo.extensions.database import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(120), nullable=False)
    checked = db.Column(db.Boolean)