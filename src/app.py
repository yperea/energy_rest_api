import os
from flask import Flask, jsonify, request

from db import db
from models.customer import CustomerModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('BPADB_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def create_tables():
    db.create_all()

#get /customer/<id>
@app.route('/customer/<int:id>')
def get_customer(id: int):
    customer = CustomerModel.get_by_id(id)

    if customer:
        return customer.json()

    return jsonify ({'message': 'Customer not found'})

#post /customer data: {name :, description:}
@app.route('/customer', methods=['POST'])
def create_customer():

    request_data = request.get_json()
    name = request_data['name']
    description = request_data['description']

    if CustomerModel.get_by_name(name):
        return {'message':
                f"customer with name '{name}' already exists"}, 400

    customer = CustomerModel(name, description)

    try:
        customer.save()
    except Exception:
        return {"message", "Error creating the customer"}, 500

    return customer.json()

#put /customer/<id> data: {name :, description:}
@app.route('/customer/<int:id>', methods=['PUT'])
def update_customer(id: int):

    request_data = request.get_json()
    name = request_data['name']
    description = request_data['description']

    if CustomerModel.get_by_name(name):
        return {'message':
                f"customer with name '{name}' already exists"}, 400

    customer = CustomerModel.get_by_id(id)
    customer.name = name
    customer.description = description

    try:
        customer.save()
    except Exception:
        return {"message", "Error updating the customer"}, 500

    return customer.json()


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
