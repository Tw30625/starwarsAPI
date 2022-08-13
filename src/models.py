from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            
            # do not serialize the password, its a security breach
        }
        
class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    haircolor = db.Column(db.String)
    eyecolor = db.Column(db.String)

    def __repr__(self):
            return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "haircolor": self.haircolor,
            "eyecolor": self.eyecolor,

            # do not serialize the password, its a security breach
        }
        
class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    climate = db.Column(db.String)

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "climate": self.climate,
            

class User(db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(16))
    email = db.Column(db.String, unique=True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    # name = Column(String(250), nullable=False)

    def __repr__(self):
            return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,

class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    character = relationship(Character)
    character_id = db.Column(db.Integer, ForeignKey('character.id'), nullable=True)
    planet = relationship(Planet)
    planet_id = db.Column(db.Integer, ForeignKey('planet.id'), nullable=True)
    user = relationship(User)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))

    def __repr__(self):
            return '<Favorite %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "character": self.character,
            "character_id": self.character_id,
            "planet": self.planet,
            "planet_id": self.planet_id,
            "user": self.user,
            "user_id": self.user_id,

