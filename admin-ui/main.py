from flask import Flask
from create import create

app = Flask(__name__)

app.register_blueprint(create,url_prefix='/')


if __name__ == '__main__':
    app.run(debug=True)