"""Blueprint for checking database contents"""
from flask import (
    Blueprint, render_template
)

from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
def get_contacts():
    db = get_db()

    contacts = db.execute('SELECT id, name, email, phone, messageBody, created FROM contactInfo').fetchall()

    if len(contacts) == 0:
        abort('No contacts yet!')

    return render_template('admin.html', contacts=contacts)
