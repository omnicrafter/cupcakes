"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret"

connect_db(app)


@app.route('/api/cupcakes')
def get_cupcakes():
    """Get data about all cupcakes,respond with JSON."""

    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]

    return jsonify(cupcakes=cupcakes)


@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake_data(cupcake_id):
    """Get data about a single cupcake, respond with JSON"""

    cupcake = Cupcake.query.get_or_404(cupcake_id).serialize()

    return jsonify(cupcake=cupcake)


@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """Create a cupcake from the request"""
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["size"]
    image = request.json["image"]
    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    response = jsonify(cupcake=new_cupcake.serialize())
    return (response, 201)
