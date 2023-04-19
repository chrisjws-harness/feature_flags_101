from flask import Flask
from key import key
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
