#!/usr/bin/env python3

from models import db, Toy
from flask import Flask
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask_cors import CORS
from flask import Flask, make_response, jsonify, request
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
CORS(app)

db.init_app(app)

@app.route('/toys', methods=['GET', 'POST'])
def all_toys():
    
    if request.method == 'GET':
        toys_list = [toy.to_dict() for toy in Toy.query.all()]

        return toys_list, 200
    
    if request.method == 'POST':
        try:
            new_toy = Toy(
                name = request.get_json().get('name'),
                image = request.get_json().get('image'),
                likes = 0
            )
            print(new_toy)
            
            db.session.add(new_toy)
            db.session.commit()

            return new_toy.to_dict(), 201
        
        except Exception:
            return {"errors": "An error occurred while creating the toy."}, 400

@app.route('/toys/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def toy_by_id(id):
    toy = Toy.query.filter(Toy.id == id).first()

    if toy:
        if request.method == 'GET':
            return toy.to_dict(), 200
        
        if request.method == 'PATCH':
            for attr in request.get_json():
                setattr(toy, attr, request.get_json()[attr])
            
            db.session.add(toy)
            db.session.commit()

            return toy.to_dict(), 202

        if request.method == 'DELETE':
            db.session.delete(toy)
            db.session.commit()

            return {}, 204
    else:
        pass

if __name__ == '__main__':
    app.run(port=5555, debug=True)