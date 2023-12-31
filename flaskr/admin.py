"""Blueprint for checking database contents"""
from flask import (
    Blueprint, flash, render_template
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
def get_contacts():
    contacts = ['test']
    db = get_db()

    rows = db.execute('SELECT id, name, email, phone, messageBody, created FROM contactInfo').fetchall()
    if rows is None:
        abort(404, 'No contacts to retrieve')
    for row in rows:
        contacts.append(row)
    return render_template('admin.html')
