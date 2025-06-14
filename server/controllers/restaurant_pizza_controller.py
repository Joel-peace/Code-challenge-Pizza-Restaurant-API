from flask import Blueprint, request, jsonify
from server import db
from server.models import RestaurantPizza  
from sqlalchemy.exc import IntegrityError

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)


@restaurant_pizza_bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    
   
    required_fields = ['price', 'pizza_id', 'restaurant_id']
    if not all(field in data for field in required_fields):
        return jsonify({"errors": ["Missing required fields"]}), 400
    
    try:
     
        rp = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        
        db.session.add(rp)
        db.session.commit()
        
        
        return jsonify({
            "id": rp.id,
            "price": rp.price,
            "pizza": {
                "id": rp.pizza.id,
                "name": rp.pizza.name,
                "ingredients": rp.pizza.ingredients
            },
            "restaurant": {
                "id": rp.restaurant.id,
                "name": rp.restaurant.name,
                "address": rp.restaurant.address
            }
        }), 201
        
    except ValueError as e:
        
        return jsonify({"errors": [str(e)]}), 400
    except IntegrityError:
        
        return jsonify({"errors": ["Invalid pizza or restaurant ID"]}), 400
    except Exception:
     
        return jsonify({"errors": ["An unexpected error occurred"]}), 400