from flask import jsonify,request
from app import app
from models import db,Restaurant, Pizza, RestaurantPizza

@app.route('/restaurants',methods=['GET'])
def rests():
    restaurants = []
    for rest in Restaurant.query.all():
        user_object = {
            'id': rest.id,
            'address':rest.address,
            'name':rest.name
        }

        restaurants.append(user_object)

    return jsonify(restaurants)

@app.route('/pizzas',methods=['GET'])
def pizzas():
    pizzas = []
    for pizza in Pizza.query.all():
        pizza_object = {
            'id': pizza.id,
            'name':pizza.name,
            'ingredients':pizza.ingredients
        }

        pizzas.append(pizza_object)

    return jsonify(pizzas)


@app.route('/new_restaurant', methods=["POST"])
def new_restaurant():
    rest = request.get_json()

    new_rest = Restaurant(
        name = rest['name'],
        address = rest['address']
    )

    db.session.add(new_rest)
    db.session.commit()

    return jsonify({
        "id": new_rest.id,
        "name": new_rest.name,
        "address": new_rest.address
    }), 201


@app.route('/restaurants/<int:id>', methods=['PUT'])
def update_restaurant(id):
    rest = request.get_json()

    existing_rest = Restaurant.query.get(id)
    existing_rest.name = rest['name']
    existing_rest.address = rest['address']

    db.session.commit()

    return jsonify({
        "id": existing_rest.id,
        "name": existing_rest.name,
        "address": existing_rest.address
    }), 200


@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete(id):
    rest = Restaurant.query.get(id)
    db.session.delete(rest)
    db.session.commit()

    return jsonify({
        "id": rest.id,
        "name": rest.name,
        "address": rest.address
    }), 201


