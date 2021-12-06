from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db= SQLAlchemy()
DB_NAME= "database.db"


def create_app():
    #how you initilize flask, necessary to run
    app= Flask(__name__)
    app.config['SECRET_KEY']= 'nodsnconvsnvpwnvkpsk;cmeqpmdckec'
    #Telling the app where the database is going to be located (website folder in this example)
    app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{DB_NAME}'
    #Initlize the database for the app(letting database know that this app will be using it)
    db.init_app(app)

    from .views import views
    from .auth import auth 

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Ticket

    create_database(app)

    login_manager= LoginManager()
    login_manager.login_view= 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        #telling flask hot to load user by looking for primary key 
        #and checking to see if it matches whatever is passed as argument(id)
        return User.query.get(int(id))
    return app

def create_database(app):
    if not path.exists('webiste/'+ DB_NAME):
        db.create_all(app=app)
        