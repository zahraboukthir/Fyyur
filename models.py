from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'venues'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    genres=db.Column(db.PickleType())
    website=db.Column(db.String())
    seeking_talent=db.Column(db.Boolean, default=True,nullable=False)
    seeking_description=db.Column(db.String())
    shows = db.relationship('Show', backref=db.backref('venues', lazy=True))
    def __repr__(self):
        return f'<Venue {self.id} {self.name}>'
    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website=db.Column(db.String())
    seeking_venue=db.Column(db.Boolean,default=True, nullable=False)
    seeking_description=db.Column(db.String())
    shows = db.relationship('Show', backref=db.backref('artists', lazy=True))
    def __repr__(self):
        return f'<Artist {self.id} {self.name}>'
    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show (db.Model):
  __tablename__='shows'
  id=db.Column(db.Integer,primary_key=True)
  venues_id = db.Column(db.Integer, db.ForeignKey('venues.id'),nullable=False)
  artists_id = db.Column(db.Integer, db.ForeignKey('artists.id'),nullable=False)
  start_time = db.Column(db.DateTime(timezone=True), nullable=False,default=datetime.now())
  def __repr__(self):
        return f'<Show {self.id} >'