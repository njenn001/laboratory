""" Common Flask server __init__.py. 

Will design different facets of the server and actions 
taken when communicated with. 

"""

""" Prebuilt imports. """
import json
import os
from urllib import request
from flask import * 
 
""" Class imports. """
from backend.server import Server

""" Throws exception. 

@param msg : The message. 
@type msg : str
"""
def throw_exec(msg): 

    if 'index' in msg: 
        os.system('echo index error')
        return render_template('404.html'), 404
    elif 'home' in msg: 
        os.system('echo home error')
        return render_template('404.html'), 404
    elif 'background' in msg: 
        os.system('echo background error')
        return render_template('404.html'), 404
    elif 'dependencies' in msg: 
        os.system('echo dependencies error')
        return render_template('404.html'), 404
    elif 'quickstart' in msg: 
        os.system('echo quickstart error')
        return render_template('404.html'), 404

""" Sets the rules for the server. 

@param app: The Flask application
@type app: app
"""
def set_rules(app):
    app.add_url_rule('/index', endpoint='index')
    app.add_url_rule('/info', endpoint='info')
    app.add_url_rule('/info/background', endpoint='background')
    app.add_url_rule('/info/dependencies', endpoint='dependencies')
    app.add_url_rule('/info/quickstart', endpoint='quickstart')
     

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
    info_methods = ['GET']
    background_methods = ['GET']
    dependencies_methdos = ['GET']
    quickstart_methods = ['GET', 'POST']

    """ Defines the main route of the server.
    "localhost:5000/"
            
    :return render_template() : A template rendering or json response.
    :rtype render_template() : template
    """
    @app.route('/', methods = index_methods)
    def index():
       
        try: 
            """ Check for arguments. """
            if (request.method == 'GET'):  
                os.system('echo web user')
                return render_template('index.html',style=url_for('static', filename='index.css'))
        except Exception as ex: 
            return throw_exec('index') 

    """ Defines the home route. 
    "localhost:5000/info/"

    @return render_template() : 
    @rtype render_template() : template 
    """
    @app.route('/info/', methods = info_methods)
    def info(): 

        try: 
            """ Check for arguments. """
            if (request.method == 'GET'): 
                os.system('echo web user')
                return render_template('info/index.html',style=url_for('static', filename='info/index.css'))
        except Exception as ex: 
            return throw_exec('home')

    """ Defines the background route. 
    "localhost:5000/info/background"

    @return render_template() : 
    @rtype render_template() : template 
    """
    @app.route('/info/background', methods = background_methods)
    def background(): 

        try: 
            """ Check for arguments. """
            if (request.method == 'GET'): 
                os.system('echo web user')
                return render_template('info/background.html',style=url_for('static', filename='info/background.css'))
        except Exception as ex: 
            return throw_exec('background')
        
    """ Defines the dependencies route. 
    "localhost:5000/info/dependencies"

    @return render_template() : 
    @rtype render_template() : template 
    """
    @app.route('/info/background', methods = dependencies_methdos)
    def dependencies(): 

        try: 
            """ Check for arguments. """
            if (request.method == 'GET'): 
                os.system('echo web user')
                return render_template('info/dependencies.html',style=url_for('static', filename='info/dependencies.css'))
        except Exception as ex: 
            return throw_exec('dependencies')
        
    """ Defines the quickstart route. 
    "localhost:5000/info/quickstart"

    @return render_template() : 
    @rtype render_template() : template 
    """
    @app.route('/info/quickstart', methods = quickstart_methods)
    def quickstart(): 

        try: 
            """ Check for arguments. """
            if (request.method == 'GET'): 
                os.system('echo web user')
                return render_template('info/quickstart.html',style=url_for('static', filename='info/quickstart.css'))
        except Exception as ex: 
            return throw_exec('quickstart')
        
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