import os
from flask import Flask, redirect, url_for, request, jsonify

# set app methods 
def set_methods(app): 
    login_methods = ["GET", "POST"]
    index_methods = ["GET"]

    # a simple page that says hello
    @app.route('/', methods = login_methods)
    def login():
        if(request.method == 'GET'):    
            data = "hello world"
            return jsonify({'data': data})

    app.add_url_rule('/', endpoint='index') 

# Set app instance 
def set_instance(app): 
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

# Set app configurations
def set_config(app, test_config): 
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

# Create the Flask app 
def create_app(test_config=None):
    
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    set_config(app, test_config)
    set_instance(app) 
    set_methods(app)

    return app