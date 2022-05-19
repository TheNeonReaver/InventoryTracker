from trackingapp import db, app


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(length=1024), nullable=False)
    quantity = db.Column(db.Integer(), nullable=False, default=5)
    shipping = db.relationship('Shipment', backref='item')


class Shipment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    item_id = db.Column(db.Integer(), db.ForeignKey('item.id'), nullable=False)


with app.app_context():
    db.create_all()
    db.session.commit()
