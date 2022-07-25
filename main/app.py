from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

ma = Marshmallow(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product

class ProductUserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductUser

@app.route('/api/products')
def index():
    products = Product.query.all()
    products_schema = ProductSchema(many=True)
    return jsonify(products_schema.dump(products))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)