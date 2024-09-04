import os
from flask import Flask
from config import Config
from models import  db, bcrypt
from flask_migrate import Migrate
#from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

#db = SQLAlchemy()
#migrate = Migrate()
#bcrypt = Bcrypt()
#jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    bcrypt.init_app(app)
    migrate = Migrate(app,db)
    jwt = JWTManager(app)
    
    

    from routes.user_routes import user_bp
    from routes.contact_routes import contact_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(contact_bp)

    return app

# Uncomment and use this block to run the app directly
# if __name__ == "__main__":
#     app = create_app()
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)
