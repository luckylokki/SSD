from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_secret_key_123'
from app import routes