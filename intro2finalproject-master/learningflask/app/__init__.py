from flask import Flask
from config import Config
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()
app = Flask(__name__)
app.config.from_object(Config)
csrf.init_app(app)
from app import routes
