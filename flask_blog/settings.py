import os

SECRET_KEY = '0\x89UX\x99\xc55\x13rZ\xba\xe3\xa7S<u\xd6,\xda\xb2&vI'
DEBUG = True
DB_USERNAME = 'flask_app'
DB_PASSWORD = 'flask_app_pw'
BLOG_DATABASE_NAME = 'blog'
DB_HOST = 'localhost'
DB_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{BLOG_DATABASE_NAME}'
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
