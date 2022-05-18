from trackingapp import db, app


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    quantity = db.Column(db.Integer(), nullable=False, default=5)
    shipping = db.Column(db.Integer(), nullable=False, default=0)

    # ^ 0 means not being shipped, 1 means it is being shipped

    def __repr__(self):
        return f'Item {self.name}'


# identifies each item by name instead of id number

with app.app_context():
    db.create_all()
    db.session.commit()
