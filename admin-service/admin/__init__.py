import os
from flask import Blueprint, Flask
from flask_restx import Api, fields, marshal, reqparse
from typing import Any, Dict

### OS ENV variables ###


### Application Setup ####

VERSION = 'V1'

app_blueprint = Blueprint(VERSION, __name__)
api = Api(version='1.0', title='Coolstore Admin Service', 
        description='Service to add new items to the coolstore catalog and manage them',
        validate=False)

app = Flask(__name__)
app.config['RESTPLUS_SWAGGER_UI_DOC_EXPANSION'] = 'list'
app.config['RESTPLUS_VALIDATE'] = True
app.config['RESTPLUS_MASK_SWAGGER'] = False
app.config['ERROR_404_HELP'] = False
app.config['ERROR_INCLUDE_MESSAGE'] = False
api.init_app(app_blueprint)