from flask import Flask
from bp import dogs
import logging

logger = logging.getLogger(__name__)
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '%(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
app.register_blueprint(dogs.bp)

@app.route("/error")
def error_page():
    numerator = 0
    denominator = 0
    app.logger.error('An error occurred: page not found')
    print( numerator / denominator ) # <=== This line raise a ZeroDivisionError
    return "Application Error"