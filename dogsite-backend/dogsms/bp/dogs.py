import json
import logging
from flask import Blueprint,Response,jsonify
from flask_api import status
import datetime

logger = logging.getLogger(__name__)


bp = Blueprint("dogs", __name__)

@bp.route('/dogs')
def dogs():
    logging.info('api_request: getting dogs')
    js = [ { "name" : "chip", "age" : "5y" } ]
    return Response(json.dumps(js),  mimetype='application/json')

@bp.route('/dogs_error')
def dogsserror():
    logging.error('bad_request: dogs error')
    js =  { "error" : "bad request" } 
    return Response(json.dumps(js),  mimetype='application/json',status = status.HTTP_400_BAD_REQUEST)

@bp.route('/')
def home():
    logging.debug('api_info')
    return jsonify(
    apiVersion="1.1.0",
    lastUpdate=datetime.datetime(2022, 8, 17)
    )