from flask_blog import db
from datetime import datetime


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    admin = db.Column(db.Integer, db.ForeignKey('author.id'))
    posts = db.relationship('Post', backref='blog', lazy='dynamic')

    def __init__(self, name, admin):
        self.name = name
        self.admin = admin

    def __repr__(self):
        return f'<Blog {self.name}'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    slug = db.Column(db.String(256), unique=True)
    publish_date = db.Column(db.DateTime)
    live = db.Column(db.Boolean)

    category_id = db.Column(db.Integer, db.Foreign('category.id'))

    def __init__(self, blog, author, title, body, category, slug=None, publish_date=None, live=True):
        self.blog_id = blog.id
        self.author_id = author.id
        self.title = title
        self.body = body
        self.category = category
        self.slug = slug
        self.live = live
        self.publish_date = publish_date if publish_date else datetime.utcnow()

    def __repr__(self):
        return f'<post {self.title}>'


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Category {self.name}>'
