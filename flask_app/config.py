import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

GOOGLE_MAPS_API_KEY = 'AIzaSyDQ9e8isN0Pn1psnrE5mgKSrnfNF6nuXSI' 