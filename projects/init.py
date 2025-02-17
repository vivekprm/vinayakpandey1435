from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db= SQLAlchemy

def create_app():
    app= Flask(__name__)


    app.config['SECRET_KEY'] = 'vinayak_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///db.sqlite'


    db.init_app(app)


    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_bluerprint)


    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
    create_app()
    

    
