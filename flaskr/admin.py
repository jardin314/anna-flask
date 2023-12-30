"""Blueprint for checking database contents"""
from flask import (
    Blueprint, flash, render_template
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
def get_contacts():
    contacts = []
    db = get_db()
    error = None

    try:
        rows = db.execute('SELECT id, name, email, phone, messageBody, created FROM contactInfo').fetchOne()
        flash(rows)
        if rows is None:
            abort(404, 'No contacts to retrieve')
        for row in rows:
            contacts.append({'id': row[0],
                             'name': row[1],
                             'email': row[2],
                             'phone': row[3],
                             'messageBody': row[4],
                             'created': row[5]})
    except Exception:
        error = 'Something went wrong'

    if error is not None:
        flash(error)

    return render_template('admin.html')
