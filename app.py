import os
from featureflags.client import CfClient
from featureflags.evaluations.auth_target import Target
from flask import Flask, render_template
app = Flask(__name__)

api_key = os.environ.get('ff_key')
cf = CfClient(api_key)


@app.route('/')
def index():
    target = Target(identifier="user1", name="user1")
    new_ui = cf.bool_variation("new_ui", target, False)
    if not new_ui:
        homepage = 'Hello, World!'
    else:
        homepage = render_template('hello.html', name="World")
    return homepage


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
