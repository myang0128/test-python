from . import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_open = db.Column(db.Boolean, default=True)
    description = db.Column(db.String(100))

    def __init__(self, is_open, description):
        self.is_open = is_open
        self.description = description

    def to_json(self):
        return {
            'id': self.id,
            'is_open': self.is_open,
            'description': self.description
        }


class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    email = db.Column("email", db.String(50), unique=True, nullable=False)
    password = db.Column("password", db.String(60), nullable=False)
    first_name = db.Column("first_name", db.String(50), nullable=False)
    last_name = db.Column("last_name", db.String(50), nullable=False)

    def to_json(self):
        return {
            "UserID": self.id,
            "Email": self.email,
            "First Name": self.first_name,
            "Last Name": self.last_name
        }
