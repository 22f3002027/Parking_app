from flask import Flask 
from database import db
from controllers.signup import sign_up
from controllers.login import log_in
from controllers.admindashboard import admin_dashboard
from controllers.newParking import new_parking
from controllers.editParking import edit_parking

app = None

def createapp():
    app = Flask(__name__)
    app.debug= True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parking.db'
    db.init_app(app)
    app.app_context().push()
    app.register_blueprint(sign_up)
    app.register_blueprint(log_in)
    app.register_blueprint(admin_dashboard)
    app.register_blueprint(new_parking)
    app.register_blueprint(edit_parking)
    return app

app = createapp()
if __name__ == '__main__':
    app.run(debug=True)
