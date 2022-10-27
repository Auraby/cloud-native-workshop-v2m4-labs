from flask_restx import Resource
from admin.health_status import HealthStatus
from admin import api, VERSION
from admin.settings.status_code import RESPONSE_SUCCEED, BAD_REQUEST
from typing import Dict

health_ns = api.namespace("Health", description='Health check API for application')


@health_ns.route('')
class HealthStatusApi(HealthStatus,Resource):
    """API to check application health"""

    def __init__(self,api) -> None:
        super().__init__()
        self.api = api

    @health_ns.response(RESPONSE_SUCCEED,"Connection to db established")
    def get(self):
        """GET request to check container health"""
        health_ns.logger.info("Received health check request")
        return self.check_connections()

    def check_connections(self) -> Dict[str,str]:
        """JSON response to allow Openshift to test health status of container"""
        status_code = 200
        status = "OK"

        # Insert the check for the method here
        catalogdb_error = self.check_catalogdb()
        if catalogdb_error:
            status = catalogdb_error
            status_code = BAD_REQUEST

        inventorydb_error = self.check_inventorydb()
        if inventorydb_error:
            status = inventorydb_error
            status_code = BAD_REQUEST

        return {"message": status}, status_code