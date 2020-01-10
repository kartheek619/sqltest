from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost/pre-registration'
db = SQLAlchemy(app)

@app.route('/')
def index():
    from models import User
    user = db.session.query(User).one()
    return user.email

if __name__ == '__main__':
    app.debug = True
    app.run()