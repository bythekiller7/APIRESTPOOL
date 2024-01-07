from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fl0user:WwLKFD1sSgj7@ep-tiny-wave-24232962.us-east-2.aws.neon.fl0.io:5432/PoolDogSv?sslmode=require'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users')
def users():
    return str(User.query.all())

if __name__ == '__main__':
    app.run()

