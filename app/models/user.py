from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    hashed_password = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)

    def __init__(self, email, hashed_password, phone_number, first_name, last_name):
        self.email = email
        self.hashed_password = hashed_password
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        user_dict = {
            "user_id": self.user_id,
            "email": self.email,
            "phone number": self.phone_number,
            "first_name": self.first_name,
            "last_name": self.last_name
        }

        return user_dict