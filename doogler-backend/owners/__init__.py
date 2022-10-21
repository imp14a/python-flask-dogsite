from flask import Flask

app = Flask(__name__)

@app.route("/error")
def error_page():
    numerator = 0
    denominator = 0
    app.logger.error('An error occurred: page not found')
    print( numerator / denominator ) # <=== This line raise a ZeroDivisionError
    return "Application Error"
    
if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0',
        port=8080
        #port=8443
        #ssl_context='adhoc'
        )