from market import db


# creat database with w parameters: 1.id 2.name 3.price
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'
