from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SimpleUser(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False)
    __tablename__ = 'simple_user'

    def __init__(self, email):
        self.email = email

    ##Méthode save
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {'email':self.email, 'id': self.id}

    ##Methode
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()