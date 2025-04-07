from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Episode(db.Model, SerializerMixin):
    __tablename__ = "episodes"

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.String, nullable = False)
    number = db.Column(db.Integer)

    appearance = db.relationship("Appearance", back_populates = "episode", cascade = "all, delete-orphan")

    serialize_rules = ("-appearance.episode",) 

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'number': self.number,
            'appearance': [a.to_dict() for a in self.appearance]
        }

    def __repr__(self):
        return f"<Episode {self.number}>"

class Guest(db.Model, SerializerMixin):
    __tablename__ = "guests"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    occupation = db.Column(db.String, nullable = False)

    appearance = db.relationship("Appearance", back_populates = "guest", cascade = "all, delete-orphan")

    serialize_rules = ("-appearance.guest",)

    def __repr__(self):
        return f"<{self.name} : {self.occupation}>"

class Appearance(db.Model, SerializerMixin):
    __tablename__ = "appearances"

    id = db.Column(db.Integer, primary_key = True)
    rating = db.Column(db.Integer, nullable = False)
    episode_id = db.Column(db.Integer, db.ForeignKey("episodes.id"))
    guest_id = db.Column(db.Integer, db.ForeignKey("guests.id"))

    episode = db.relationship("Episode", back_populates = "appearance")
    guest = db.relationship("Guest", back_populates = "appearance")

    serialize_rules = ("-episode.appearance", "-guest.appearance")

    @validates("rating")
    def validates_rating(self,key,value):
        if value < 1 or value > 5:
            raise ValueError("Choose a rating between 1 to 5")
        return value    

    def __repr__(self):
        return f"Episode {self.episode_id} : Rating - {self.rating}"

