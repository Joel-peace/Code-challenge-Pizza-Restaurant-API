from flask import Blueprint, jsonify
from server import db
from server.models import Restaurant  

restaurant_bp = Blueprint('restaurants', __name__)



@restaurant_bp.route('', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{
        "id": r.id,
        "name": r.name,
        "address": r.address
    } for r in restaurants])

@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    
    
    pizzas = [{
        "id": rp.pizza.id,
        "name": rp.pizza.name,
        "ingredients": rp.pizza.ingredients,
        "price": rp.price
    } for rp in restaurant.pizzas]
    
    return jsonify({
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": pizzas
    })


@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    
 

    db.session.delete(restaurant)
    db.session.commit()
    return '', 204