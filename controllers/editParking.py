from flask import Flask, render_template, redirect, Response, request, Blueprint
from models.models import *

edit_parking = Blueprint('editParking', __name__)

@edit_parking.route('/admindashboard/editParking', methods=['GET','POST'])

def editParking():
    return render_template("editParking.html")
    