"""Blueprint for checking database contents"""
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from flaskr.db import get_db

bp = Blueprint('admin', __name__, url_prefix='/admin')
