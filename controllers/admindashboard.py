from flask import Flask, render_template, redirect, Response, request, Blueprint
from models.models import *

admin_dashboard = Blueprint('admindashboard', __name__)

@admin_dashboard.route('/admindashboard', methods=['GET','POST'])
def admindashboard():

    return render_template('admindashboard.html')