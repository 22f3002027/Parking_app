from app import createapp
from database import db
app = createapp()

with app.app_context():
    db.create_all()
    print("Database created successfully.")