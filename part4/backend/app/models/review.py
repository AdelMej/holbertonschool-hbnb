from app.models.base import BaseModel
from app.extensions import db


class Review(BaseModel):
    __tablename__ = 'reviews'

    title = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=False)
    place_id = db.Column(db.String, db.ForeignKey('places.id'), nullable=False)
