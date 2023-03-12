import os
from urllib import request
from flask import * 
 
from obj.user import User

# Set rules (directories) to server
def set_rules(app):
    app.add_url_rule('/index', endpoint='index')
    app.add_url_rule('/background', endpoint='background') 

# Set error handlers 
def set_errors(app): 

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

# set app methods 
def set_methods(app): 

    index_methods = ['GET']
    background_methods = ["GET"]

    # Get simple index page 
    @app.route('/', methods = index_methods)
    def index():
       
        return render_template('index.html',style=url_for('static', filename='index.css'))

    # REWRITE
    # Background headquarters 
    @app.route('/background', methods = background_methods)
    def background():
        content_type = request.headers.get('Content-Type')
        
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
    app = Flask(__name__, instance_relative_config=True, static_url_path='/static')
    
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    set_config(app, test_config)
    set_instance(app) 
    set_methods(app)
    set_rules(app)
    set_errors(app)

    return app