from flask import Flask, render_template, redirect, Response, request, Blueprint
from models.models import *

view_del_spot= Blueprint('viewDelSpot',__name__)

@view_del_spot.route('/admindashboard/viewDelSpot', methods=['GET','POST'])

def viewDelSpot():
    return render_template("viewDelSpot.html")