import flask
app = flask.Flask(__name__)
@app.route('/')
def home():
    return "Welcome to the Package Manager!"