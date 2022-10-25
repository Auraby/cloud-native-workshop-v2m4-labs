from admin.catalog_manager import CatalogManager
from flask_restx import Resource, reqparse

from admin import VERSION, api


catalog_manager_ns = api.namespace(f'{VERSION}/Catalog Manager', description="To manage catalog items")

@catalog_manager_ns.route('')
class CatalogManagerApi(CatalogManager,Resource):
    def __init__(self,api) -> None:
        super().__init__()
        self.api = api

    def get(self):
        return {"message": "OK"}, 200

    @catalog_manager_ns.response(200, 'Successfully added to database')
    def post(self):
        return {"message": "OK"}, 200