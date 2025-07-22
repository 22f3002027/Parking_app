from flask import Flask 
from database import db
from controllers.signup import signup


app = None

def createapp():
    app = Flask(__name__)
    app.debug= True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parking.db'
    db.init_app(app)
    app.app_context().push()
    app.register_blueprint(signup)
    return app

app = createapp()
if __name__ == '__main__':
    app.run(debug=True)
