from admin.catalog_manager import CatalogManager
from flask_restx import Resource, reqparse

from admin import VERSION, api


catalog_manager_ns = api.namespace(f'{VERSION}/Scrape', description="To manage catalog items")

class CatalogManagerApi():
    def __init__(self) -> None:
        pass