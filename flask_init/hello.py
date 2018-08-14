# import os

from flask import Flask, render_template, request, redirect, url_for, flash, session


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

    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


def valid_login(username, password):
    if username == password:
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
    # host = os.getenv('IP', '0.0.0.0')
    # port = int(os.getenv('PORT', 5000))
    # app.run(host=host, port=port)
    app.secret_key = '0\x89UX\x99\xc55\x13rZ\xba\xe3\xa7S<u\xd6,\xda\xb2&vI'
    app.run(debug=True)
