"""Contact form handling"""
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from flaskr.db import get_db

bp = Blueprint('contact', __name__, url_prefix='/contact')


@bp.route('/', methods=('GET', 'POST'))
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message_body = request.form['message body']
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
                        (name, email, phone, message_body)
                        )
                db.commit()
            except:
                error = 'Something went wrong!'
            else:
                # TODO make this redirect to a "contact submitted" page
                return redirect(url_for('home'))

        flash(error)

    return render_template('contact.html')
