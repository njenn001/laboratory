# Prebuilt imports. 
import sqlite3
import click

# Class imports. 
from flask import current_app, g

""" Returns database 

@return db : The database
@rtype : Database
"""
def get_db(): 
    
    if 'db' not in g: 
       
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types = sqlite3.PARSE_DECLTYPES
        )

        g.db.row_factory = sqlite3.Row

        return g.db 

""" Returns database 

@param e :
@type :
"""
def close_db(e = None):

    db = g.pop('db', None)

    if db is not None: 
        db.close()

""" Initialize the database.

@return : None
"""
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


""" Initialize the database.

@return : None
"""
@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

""" Initialize the application. 

@param app : The app
@type app: Flask.app
""" 
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)