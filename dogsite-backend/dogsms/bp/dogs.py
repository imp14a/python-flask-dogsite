import json
import logging
from flask import Blueprint,Response,jsonify,current_app
from flask_api import status
import datetime
import util.metrics as metric

logger = logging.getLogger(__name__)


bp = Blueprint("dogs", __name__)

@bp.route('/dogs')
def dogs():
    current_app.logger.info('api_request: getting dogs')
    js = [ { "name" : "chip", "age" : "5y" } ]
    return Response(json.dumps(js),  mimetype='application/json')

@bp.route('/dogs_error')
def dogsserror():
    current_app.logger.error('bad_request: dogs error')
    js =  { "error" : "bad request" } 
    metric.exportAndRecordError("http_400");
    return Response(json.dumps(js),  mimetype='application/json',status = status.HTTP_400_BAD_REQUEST)

@bp.route('/')
def home():
    current_app.logger.debug('api_info')
    return jsonify(
    apiVersion="1.1.0",
    lastUpdate=datetime.datetime(2022, 8, 17)
    )