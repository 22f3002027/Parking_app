from flask import Flask, render_template, redirect, Response, request, Blueprint
from models.models import *

new_parking = Blueprint('newParking', __name__)
print("ram")

@new_parking.route('/admindashboard/newParking', methods=['GET','POST'])
def newParking():
    print("sita")
    if request.method == 'POST':
        print("server")
        primeloc = request.form.get('primeloc')
        address = request.form.get('address')
        pincode = request.form.get('pincode')
        price = request.form.get('price')
        maxspots = request.form.get('maxspots')

        
        print(primeloc)
        
        parkingdetails = ParkingDetails(
            primeloc = primeloc,
            address = address,
            pincode = pincode,
            price = price,
            maxspots = maxspots
            )
        print("a")
        db.session.add(parkingdetails)
        db.session.commit()
        print("location added succesfully")
        return redirect('/admindashboard')
    return render_template("newParking.html")
    