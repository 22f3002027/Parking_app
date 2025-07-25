from flask import Flask, render_template, redirect, Response, request, Blueprint
from models.models import *

log_in = Blueprint('login', __name__)

@log_in.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print("a")

        user = User.query.filter_by(email=email).first()
         
        if (password==user.password and user.role == "user"):
            print('user login successful')
            return redirect('/userdashboard')
        elif (password==user.password and user.role == "Admin"):
            print('admin login successful')
            return redirect('/admindashboard')
        else:
            print('login failed')
            return redirect('/login')
    return render_template('login.html')
