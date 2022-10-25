import os
from flask import Blueprint, Flask
from flask_restx import Api, fields, marshal, reqparse
from typing import Any, Dict
from flask_sqlalchemy import SQLAlchemy

### OS ENV variables ###
PORT = 5000

### DB Settings ###
CATALOGDB_NAME = "catalog"
CATALOGDB_USERNAME = "catalog"
CATALOGDB_PASSWORD = "mysecretpassword"
CATALOGDB_URL = f"postgresql://{CATALOGDB_USERNAME}:{CATALOGDB_PASSWORD}@catalog-database:5432/{CATALOGDB_NAME}"


INVENTORYDB_NAME = "inventory"
INVENTROYDB_USERNAME = "inventory"
INVENTORYDB_PASSWORD = "mysecretpassword"
INVENTORYDB_URL = f"postgresql://{INVENTROYDB_USERNAME}:{INVENTORYDB_PASSWORD}@inventory-database:5432/{INVENTORYDB_NAME}"

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
# app.config['SQLALCHEMY_DATABASE_URI'] = ""
app.config['SQLALCHEMY_BINDS'] = {
        'catalog': CATALOGDB_URL,
        'inventory': INVENTORYDB_URL
}

api.init_app(app_blueprint)