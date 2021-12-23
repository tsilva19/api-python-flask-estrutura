from flask import Flask
from flask_cors import CORS

from src.adapter.input.controller.alunos import Alunos
from src.errors_handlers import Api

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Alunos, "/alunos")
