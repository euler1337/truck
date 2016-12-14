#!/usr/bin/env python
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

#@app.route("/")
#def main():
#    return render_template('index.html')



#if __name__ == "__main__":
#    app.run(debug=True)