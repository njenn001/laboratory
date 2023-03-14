""" Common Flask server __init__.py. 

Will design different facets of the server and actions 
taken when communicated with. 

"""

""" Imports. """
import os
from urllib import request
from flask import * 
 
from obj.user import User

""" Sets the rules for the server. 

@param app: The Flask application
@type app: app
"""
def set_rules(app):
    app.add_url_rule('/index', endpoint='index')
    app.add_url_rule('/background', endpoint='background') 

""" Sets the error handlers on the server. 

@param app: The Flask application
@type app: app
"""
def set_errors(app): 

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

""" Sets the server methods. 

@param app: The Flask application
@type app: app
"""
def set_methods(app): 

    index_methods = ['GET']
    background_methods = ["GET"]

    """ Defines the basic index route.
            
    :returns: A template rendering
    :rtype: template
    """
    @app.route('/', methods = index_methods)
    def index():
       
        return render_template('index.html',style=url_for('static', filename='index.css'))

    """ Defines the background route.
            
    :returns: A template rendering
    :rtype: template
    """
    @app.route('/background', methods = background_methods)
    def background():
        content_type = request.headers.get('Content-Type')
        
""" Sets the app instance. 

@param app: The Flask application
@type app: app
"""
def set_instance(app): 

    """ Ensure the instance folder exists. """
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

""" Sets the server methods. 

@param app: The Flask application
@type app: app

@param test_config: Configuration file. 
@type test_config: str
"""
def set_config(app, test_config): 

    if test_config is None:

        """ Load the static config. """
        app.config.from_pyfile('config.py', silent=True)

    else:

        """ Load an test the passed config. """
        app.config.from_mapping(test_config)

""" Creates the Flask application. 

@param test_config: Configuration file.
@type test_config: str
"""
def create_app(test_config=None):
    
    """ Create and configure the app. """
    app = Flask(__name__, instance_relative_config=True, static_url_path='/static')
    
    """ Further configurations. """
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    """ Runs different setups. """
    set_config(app, test_config)
    set_instance(app) 
    set_methods(app)
    set_rules(app)
    set_errors(app)

    """ Returns the configure application. """
    return app