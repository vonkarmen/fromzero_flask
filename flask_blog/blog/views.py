from flask_blog import app, db
from flask import render_template, redirect, flash, url_for
from blog.form import SetupForm
from author.models import Author
from blog.models import Blog
from author.decorators import login_required


@app.route('/')
@app.route('/index')
def index():
    blogs = Blog.query.count()
    if blogs == 0:
        return redirect(url_for('setup'))

    return '<h2>Hello World</h2>'


@app.route('/admin')
@login_required
def admin():
    return render_template('blog/admin.html')


@app.route('/setup', methods=['POST', 'GET'])
def setup():
    form = SetupForm()
    error = ''
    if form.validate_on_submit():
        author = Author(
            form.fullname.data,
            form.email.data,
            form.username.data,
            form.password.data,
            True
        )
        db.session.add(author)
        db.session.flush()
        if author.id:
            blog = Blog(
                form.name.data,
                author.id
            )
            db.session.add(blog)
            db.session.flush()
        else:
            db.session.rollback()
            error = "Error creating user"
            print(error)

        if author.id and blog.id:
            db.session.commit()
            flash('Blog created')
            return redirect(url_for('admin'))
        else:
            db.session.rollback()
            error = "Error creating blog"
            print(error)

    return render_template('blog/setup.html', form=form, error=error)
