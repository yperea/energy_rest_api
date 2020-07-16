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



if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
