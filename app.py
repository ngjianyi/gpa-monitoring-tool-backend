from flask import Flask

from models.models import db
from routes.student import bp

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # database_url = os.environ.get('DATABASE_URL')
    # if database_url and database_url.startswith("postgres://"):
    #     database_url = database_url.replace("postgres://", "postgresql://", 1)
    #     os.environ['DATABASE_URL'] = database_url

    # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    app.register_blueprint(bp, url_prefix='/api')
    
    return app