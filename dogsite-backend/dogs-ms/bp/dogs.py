import json
from flask import Blueprint,Response,jsonify,current_app
import datetime

bp = Blueprint("dogs", __name__)

@bp.route('/dogs')
def dogs():
    js = [ { "name" : "chip", "age" : "5y" } ]
    return Response(json.dumps(js),  mimetype='application/json')

@bp.route('/')
def home():
    current_app.logger.info('Getting api info')
    return jsonify(
    apiVersion="1.0.0",
    lastUpdate=datetime.datetime(2022, 8, 17)
    )