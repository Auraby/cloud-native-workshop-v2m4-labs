from flask_cors import CORS
from admin import app, app_blueprint, api, PORT
import logging

from admin.health_status_api import health_ns
from admin.catalog_manager_api import catalog_manager_ns

api.add_namespace(health_ns)
api.add_namespace(catalog_manager_ns)

CORS(app)
app.register_blueprint(app_blueprint)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

if __name__ == '__main__':
    app.run(port=PORT, debug=True)