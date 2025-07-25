from flask import Flask, render_template, redirect, Response, request, Blueprint
from models.models import *

sign_up = Blueprint('signup', __name__)

@sign_up.route('/signup', methods=['GET','POST'])
def signup():
    
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        fullname = firstname + " " + lastname
        email = request.form.get('email')
        password = request.form.get('password')
        address = request.form.get('address')
        pincode = request.form.get('pincode')

        doesemailexist = User.query.filter_by(email=email).first()

        if (doesemailexist):
            return render_template('allreadyexist.html')
        else:
            user= User(
                fullname=fullname,
                email=email,
                password=password,
                address=address,
                pincode=pincode,
                role="user"
            )
            db.session.add(user)
            db.session.commit()
            print("User created successfully")
            return redirect("/login")
    return render_template('signup.html')
