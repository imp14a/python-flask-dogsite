from flask import Flask
from getapug import pug

app = Flask(__name__)
app.register_blueprint(pug.bp)

@app.route("/error")
def error_page():
    numerator = 0
    denominator = 0
    print( numerator / denominator ) # <=== This line raise a ZeroDivisionError
    return "Application Error"