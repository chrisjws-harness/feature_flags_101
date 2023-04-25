import os
from featureflags.client import CfClient
from featureflags.evaluations.auth_target import Target
from flask import Flask, render_template, request
app = Flask(__name__)

api_key = os.environ.get('ff_key')
cf = CfClient(api_key)


@app.route('/')
def index():
    if bool(request.headers.get("whoami")):
        print(request.headers.get("whoami"))
        target = Target(
            name=request.headers.get("whoami"),
            identifier=request.headers.get("whoami").lower().replace(" ", "_")
        )
    else:
        print("default user!")
        target = Target(identifier="user1", name="user1")
    print(target)
    new_ui = cf.bool_variation("new_ui", target, False)
    greeting = cf.string_variation("different_greetings", target, "")
    personalization = cf.bool_variation("personalization", target, False)
    params = {"name": "World"}
    if greeting != "":
        params['greeting'] = greeting
    if personalization:
        params['name'] = request.headers.get("whoami")
    if not new_ui:
        homepage = 'Hello, World!'
    else:
        homepage = render_template('hello.html', **params)
    return homepage


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
