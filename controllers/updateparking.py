from flask import Flask, render_template, redirect, Response, request, Blueprint
from models.models import *

update_parking = Blueprint('updateparking',__name__)

@update_parking.route('/admindashboard/updateparking', method=['GET','POST'])

def updateparking():
    if request.method == 'POST':
        primeloc = request.form.get('primeloc')
        address = request.form.get('address')
        pincode = request.foem.get('pincode')
        price = request.get.form('price')
        maxspots = request.form.get('maxspots')

        db.commit()
        return redirect('/admindashboard')

    return render_template('editParking.html')