"""Contact form handling"""
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

bp = Blueprint('contact', __name__, url_prefix='/contact')


@bp.route('/form', methods=('GET', 'POST'))
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        messageBody = request.form['message body']
        db = get_db()
        error = None

        if not name:
            error = 'Name is required'
        elif not email:
            error = 'Email is required'

        if error is None:
            try:
                db.execute(
                        "INSERT INTO contactInfo (name, email, phone, messageBody) VALUES (?, ?, ?, ?)",
                        (name, email, phone, messageBody)
                        )
                db.commit()
            except:
                error = 'Something went wrong!'
            else:
                # TODO add to this
                return redirect(url_for(''))
