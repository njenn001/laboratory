""" Common Flask server __init__.py. 

Will design different facets of the server and actions 
taken when communicated with. 

"""

""" Prebuilt imports. """
import json
import os
from urllib import request
from flask import * 
import sqlite3

""" Class imports. """
from backend.server import Server
from . import db
from . import auth

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
    elif 'ap' in msg: 
        os.system('echo ap error')
        return render_template('404.html'), 404
    elif 'server' in msg: 
        os.system('echo server error')
        return render_template('404.html'), 404
    elif 'clients' in msg: 
        os.system('echo clients error')
        return render_template('404.html'), 404
    elif 'comms' in msg: 
        os.system('echo comms error')
        return render_template('404.html'), 404

""" Sets the rules for the server. 

@param app: The Flask application
@type app: app
"""
def set_rules(app):

    # Index endpoint
    app.add_url_rule('/index', endpoint='index')
    
    # Information endpoints
    app.add_url_rule('/info', endpoint='info')
    app.add_url_rule('/info/background', endpoint='background')
    app.add_url_rule('/info/dependencies', endpoint='dependencies')
    app.add_url_rule('/info/quickstart', endpoint='quickstart')
    app.add_url_rule('/info/ap', endpoint='ap')
    app.add_url_rule('/info/server', endpoint='server')
    app.add_url_rule('/info/clients', endpoint='clients')
    app.add_url_rule('/info/comms', endpoint='comms')

    # Client endpoints
    app.add_url_rule('/sincity/auth', endpoint='sincity')
    app.add_url_rule('/sincity/play', endpoint='sincityplay')
    
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

    # Index method
    index_methods = ['GET']
    
    # Information methods
    info_methods = ['GET']
    background_methods = ['GET']
    dependencies_methdos = ['GET']
    quickstart_methods = ['GET', 'POST']
    ap_methods=['GET']
    server_methods=['GET']
    clients_methods=['GET']
    comms_methods=['GET']

    # Client methods
    sincity_methods=['GET', 'POST']
    sincity_play_methods=['GET', 'POST']

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
                
    """ Defines the ap route. 
    "localhost:5000/info/ap"

    @return render_template() : 
    @rtype render_template() : template 
    """
    @app.route('/info/ap', methods = ap_methods)
    def ap():
        try: 
            """ Check for arguments. """
            if (request.method == 'GET'): 
                os.system('echo web user')
                return render_template('info/ap.html',style=url_for('static', filename='info/ap.css'))
        except Exception as ex: 
            return throw_exec('ap')
                
    """ Defines the server route. 
    "localhost:5000/info/server"

    @return render_template() : 
    @rtype render_template() : template 
    """
    @app.route('/info/server', methods = server_methods)
    def server(): 

        try: 
            """ Check for arguments. """
            if (request.method == 'GET'): 
                os.system('echo web user')
                return render_template('info/server.html',style=url_for('static', filename='info/server.css'))
        except Exception as ex: 
            return throw_exec('server')
                
    """ Defines the client route. 
    "localhost:5000/info/client"

    @return render_template() : 
    @rtype render_template() : template 
    """
    @app.route('/info/clients', methods = clients_methods)
    def clients(): 

        try: 
            """ Check for arguments. """
            if (request.method == 'GET'): 
                os.system('echo web user')
                return render_template('info/clients.html',style=url_for('static', filename='info/clients.css'))
        except Exception as ex: 
            return throw_exec('clients')
            
    """ Defines the comms route. 
    "localhost:5000/info/comms"

    @return render_template() : 
    @rtype render_template() : template 
    """
    @app.route('/info/comms', methods = comms_methods)
    def comms(): 

        try: 
            """ Check for arguments. """
            if (request.method == 'GET'): 
                os.system('echo web user')
                return render_template('info/comms.html',style=url_for('static', filename='info/comms.css'))
        except Exception as ex: 
            return throw_exec('comms')    
    
    """ Defines the sincity route. 
    "localhost:5000/sincity/auth"

    @return render_template() : 
    @rtype render_template() : template 
    """
    @app.route('/sincity/auth', methods = sincity_methods)
    def sincity(): 


        try: 
            connect = sqlite3.connect(r'./instance/flaskr.sqlite')
            cursor = connect.cursor()
            cursor.execute('SELECT * FROM USER')

            data = cursor.fetchall() 

            """ Check for arguments. """
            if (request.method == 'POST'): 
                u = request.form['username']
                p = request.form['password']
                
                for user in data:
                    if u in user: 
                        
                        if user[2] == p:
                            return render_template('/sincity/play.html',style=url_for('static', filename='sincity/play.css'), result=u) 
                        else: 
                            return render_template('/sincity/auth.html',style=url_for('static', filename='sincity/auth.css'), result=['Incorrect Password.']) 
                    else: 
                        return render_template('/sincity/auth.html',style=url_for('static', filename='sincity/auth.css'), result=['User does not exist.']) 

            if (request.method == 'GET'): 
                os.system('echo web user 1')
                return render_template('/sincity/auth.html',style=url_for('static', filename='sincity/auth.css'))
        except Exception as ex: 
            return throw_exec('auth')    
    
    """ Defines the sincity route. 
    "localhost:5000/sincity/play"

    @return render_template() : 
    @rtype render_template() : template 
    """
    @app.route('/sincity/play', methods = sincity_play_methods)
    def sincity_play(): 

        try: 
            """ Check for arguments. """
            if (request.method == 'GET'): 
                os.system('echo web user')
                return render_template('/sincity/play.html',style=url_for('static', filename='sincity/auth.css'))
        except Exception as ex: 
            return throw_exec('play')    
    
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

    """ Database and Blueprints. """
    db.init_app(app)
    app.register_blueprint(auth.bp)

    """ Returns the configure application. """
    return app