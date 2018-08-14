# import os

from flask import Flask, render_template, request, redirect, url_for, flash, session
import pymysql

import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            flash('Succesfully logged in')
            session['username'] = request.form.get('username')
            return redirect(url_for('welcome'))
        else:
            error = 'Incorrect Username and Password'
            app.logger.warning(
                f'Incorrect username and password for user {request.form.get("username")}')

    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


def valid_login(username, password):

    # mysql
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_USER = 'flask_app'
    MYSQL_DATABASE_PASSWORD = 'flask_app_pw'
    MYSQL_DATABASE_DB = 'my_flask_app'

    conn = pymysql.connect(
        host=MYSQL_DATABASE_HOST,
        user=MYSQL_DATABASE_USER,
        passwd=MYSQL_DATABASE_PASSWORD,
        db=MYSQL_DATABASE_DB
    )
    cusor = conn.cursor()
    cusor.execute(
        f"SELECT * FROM user WHERE username='{username}' AND password='{password}'")
    data = cusor.fetchone()
    if data:
        return True
    else:
        return False


@app.route('/')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])

    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    # user for cloud9 env
    # host = os.getenv('IP', '0.0.0.0')
    # port = int(os.getenv('PORT', 5000))
    # app.run(host=host, port=port)

    # secrets
    app.secret_key = '0\x89UX\x99\xc55\x13rZ\xba\xe3\xa7S<u\xd6,\xda\xb2&vI'

    # logging
    handler = RotatingFileHandler('error.log', maxBytes=1000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

    app.run(debug=True)
