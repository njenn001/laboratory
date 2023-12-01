""" Prebuild imports. """
import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

""" Creates a new blueprint. 

@param __name__ : 
@type __name__ :

@param prefix :
@type prefix : 
"""
bp = Blueprint('auth', __name__, url_prefix='/auth')