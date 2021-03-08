from flask import Flask,render_template

app = Flask(__name__)



if __name__ == '__main__':
    # Make flask instance run on default port:5000 and host:127.0.0.1
    from api import *

    app.run(debug=True)
