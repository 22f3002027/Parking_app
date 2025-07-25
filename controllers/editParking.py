from flask import Flask, render_template, redirect, Response, request, Blueprint
from models.models import *

edit_parking = Blueprint('editParking', __name__)


@edit_parking.route('/admindashboard/editParking/<int:id>', methods=['GET','POST'])
def editparking(id):
    print("sita")
    parkingdetails = ParkingDetails.query.get_or_404(id)
    if not parkingdetails:
        print("tag")
    print("ghar")    
    if request.method== 'POST':
        parkingdetails.primeloc = request.form.get('primeloc')
        parkingdetails.address = request.form.get('address')
        parkingdetails.pincode = request.form.get('pincode')
        parkingdetails.price = request.form.get('price')
        parkingdetails.maxspots = request.form.get('maxspots')
        
        
        db.session.commit()
        return redirect('/admindashboard')

    return render_template('editParking.html',parkingdetails=parkingdetails)