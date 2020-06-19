from flask import Flask
from lib.router import Router

app = Flask(__name__)

Router.run(app)