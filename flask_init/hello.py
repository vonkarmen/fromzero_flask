# import os

from flask import Flask, request


app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return f'Hello {request.values["username"]}'
    else:
        return '<form method="post" action="/login"><input type="text" name="username" /><p><button type="submit">Submit</button></form>'


if __name__ == '__main__':
    # host = os.getenv('IP', '0.0.0.0')
    # port = int(os.getenv('PORT', 5000))
    # app.run(host=host, port=port)
    app.run(debug=True)
