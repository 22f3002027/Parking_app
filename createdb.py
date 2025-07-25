from app import createapp
from database import db
from models.models import User
from models.models import ParkingDetails
app = createapp()

with app.app_context():
    db.create_all()
    print("Database created successfully.")
    theadmin =  User(
        fullname= "Bhavya Singh",
        email="bhavyasingh2602@gmail.com",
        password="aadi2602",
        address="dwarka, delhi",
        pincode="110059",
        role= "Admin"
    )   
    db.session.add(theadmin)
    db.session.commit()
    print("admin created succesfully")
    

