# import os

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return f'Welcome back {request.form["username"]}'
        else:
            error = 'Incorrect Username and Password'

    return render_template('login.html', error=error)


def valid_login(username, password):
    if username == password:
        return True
    else:
        return False


if __name__ == '__main__':
    # host = os.getenv('IP', '0.0.0.0')
    # port = int(os.getenv('PORT', 5000))
    # app.run(host=host, port=port)
    app.run(debug=True)
