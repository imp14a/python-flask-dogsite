from flask import Blueprint,render_template,jsonify

bp = Blueprint("pup", __name__)

@bp.route('/pugs')
def pugs():
    return jsonify(
        data=["chip"],
        lastUpdate="today"
    )

@bp.route('/')
def home():
    return "<h1>Hi!</h1>"