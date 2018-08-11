# import os

from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'


if __name__ == '__main__':
    # host = os.getenv('IP', '0.0.0.0')
    # port = int(os.getenv('PORT', 5000))
    # app.run(host=host, port=port)
    app.run(debug=True)
