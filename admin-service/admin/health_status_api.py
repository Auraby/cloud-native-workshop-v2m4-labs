from flask_restx import Resource
from admin.health_status import HealthStatus
from admin import api, VERSION
from typing import Dict

health_ns = api.namespace("Health", description='Health check API for application')

