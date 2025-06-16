from flask import Blueprint, request, jsonify
from server import db
from server.models import RestaurantPizza, Pizza, Restaurant

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizza_bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if price is None or pizza_id is None or restaurant_id is None:
        error_message = {"errors": ["validation errors"]}
        return jsonify(error_message), 400

    try:
        price = int(price)
        if not (1 <= price <= 30):
            raise ValueError()
    except (ValueError, TypeError):
        error_message = {"errors": ["validation errors"]}
        return jsonify(error_message), 400

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    if pizza is None or restaurant is None:
        error_message = {"errors": ["validation errors"]}
        return jsonify(error_message), 400

    new_restaurant_pizza = RestaurantPizza(
        price=price,
        pizza_id=pizza_id,
        restaurant_id=restaurant_id
    )
    db.session.add(new_restaurant_pizza)
    db.session.commit()

    pizza_data = {
        "id": pizza.id,
        "name": pizza.name,
        "ingredients": pizza.ingredients
    }

    return jsonify(pizza_data), 201