"""__init__ for this flask blog"""

from flask import Flask

app = Flask(__name__)

# Load config settings from app/settings.py
app.config.from_object("app.config")

from app import routes

type(routes)
