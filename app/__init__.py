from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)

db = SQLAlchemy()
migrate = Migrate()
marshmallow = Marshmallow()

def create_app():
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dbase.db"

    from .controller import controller

    app.register_blueprint(controller)

    from .fetch_news import fetch_news

    app.cli.add_command(fetch_news)

    db.init_app(app)
    migrate.init_app(app,db)
    marshmallow.init_app(app)

    from .model import Article

    return app
