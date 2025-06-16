from flask import Blueprint, jsonify
from server import db
from server.models import Restaurant

restaurant_bp = Blueprint('restaurants', __name__)

@restaurant_bp.route('', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    
    restaurants_list = []
    for r in restaurants:
        restaurant_dict = {
            "id": r.id,
            "name": r.name,
            "address": r.address
        }
        restaurants_list.append(restaurant_dict)
        
    return jsonify(restaurants_list)

@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)

    if restaurant is None:
        return jsonify({"error": "Restaurant not found"}), 404

    pizzas_list = []
    for rp in restaurant.restaurant_pizzas:
        pizza_dict = {
            "id": rp.pizza.id,
            "name": rp.pizza.name,
            "ingredients": rp.pizza.ingredients
        }
        pizzas_list.append(pizza_dict)

    restaurant_data = {
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": pizzas_list
    }
    return jsonify(restaurant_data)

@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)

    if restaurant is None:
        return jsonify({"error": "Restaurant not found"}),

    db.session.delete(restaurant)
    db.session.commit()

    return '', 204