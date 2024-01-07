from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fl0user:WwLKFD1sSgj7@ep-tiny-wave-24232962.us-east-2.aws.neon.fl0.io:5432/PoolDogSv?sslmode=require'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

class Producto(db.Model):
    id_producto = db.Column(db.Integer, primary_key=True)
    descripcion_producto = db.Column(db.String(100))
    id_tipo_producto = db.Column(db.Integer)
    precio = db.Column(db.Float)
    estado = db.Column(db.Boolean)
    fecha_ingreso = db.Column(db.Date)



@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users')
def users():
    return str(User.query.all())


@app.route("/productos")
def productos():
    # Realizamos una consulta a la base de datos

    productos = Producto.query.filter_by(estado=True).all()

    # Devolvemos los productos en formato JSON

    return jsonify([producto.to_dict() for producto in productos])



if __name__ == '__main__':
    app.run()

