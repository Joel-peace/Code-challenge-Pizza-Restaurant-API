from flask import Blueprint, jsonify
from server.models import Pizza

pizza_bp = Blueprint('pizzas', __name__)

@pizza_bp.route('', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()

    pizzas_data = []
    for pizza in pizzas:
        pizza_info = {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        }
        pizzas_data.append(pizza_info)

    return jsonify(pizzas_data)