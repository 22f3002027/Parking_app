from flask import Flask, render_template, redirect, Response, request, Blueprint
from models.models import *

signup = Blueprint('signup', __name__)

@signup.route('/signup', methods=['GET','POST'])
def signup():
    print("Signup page accessed")
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        fullname = firstname + " " + lastname
        email = requesr.form.get('email')
        password = request.form.get('password')
        address = request.form.get('address')
        pincode = request.form.get('pincode')

        doesemailexist = User.query.filter_by(email=email).first()

        if (doesemailexist):
            render_template('areadyexists.html')
        else:
            user= User(
                fullname=fullname,
                email=email,
                password=password,
                address=address,
                pincode=pincode
            )
            db.session.add(user)
            db.session.commit()
            print("User created successfully")
            return rediret("/login")
    return render_template('signup.html')
