from database import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), nullable=False)
    email= db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    pincode = db.Column(db.Integer, nullable=False)
    role=db.Column(db.String(30), nullable=False)
    status = db.Column(db.Integer, default=0)

class ParkingDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    primeloc = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    pincode = db.Column(db.Integer, nullable=False)
    price = db.Column(db.String(50), nullable=False)
    maxspots = db.Column(db.Integer, nullable=False)
    occupied = db.Column(db.Integer, default=0)