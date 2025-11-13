from app.models.base import BaseModel
from app.extensions import db

# table association for amenities and places
place_amenity = db.Table('place_amenity',
    db.Column('place_id', db.String, db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.String, db.ForeignKey('amenities.id'), primary_key=True)
)


class Place(BaseModel):
    __tablename__ = 'places'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    rooms = db.Column(db.Integer, nullable=False)
    surface = db.Column(db.Integer, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    owner_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)
    amenities = db.relationship('Amenity', secondary=place_amenity, lazy='subquery',
                              backref=db.backref('place', lazy=True))
    reviews = db.relationship('Review', backref='place', lazy=True)

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        if amenity not in self.amenities:
            self.amenities.append(amenity)
