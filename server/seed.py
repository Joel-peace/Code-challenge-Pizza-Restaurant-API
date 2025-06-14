# server/seed.py
import os
import sys

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from server.app import create_app
from server import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    # Clear existing data
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()
    db.session.commit()

    # Create restaurants
    r1 = Restaurant(name="Pizza Palace", address="123 Main St")
    r2 = Restaurant(name="Italian Corner", address="456 Oak Ave")
    r3 = Restaurant(name="Slice House", address="789 Pine Rd")
    
    # Create pizzas
    p1 = Pizza(name="Margherita", ingredients="Tomato sauce, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato sauce, Mozzarella, Pepperoni")
    p3 = Pizza(name="Vegetarian", ingredients="Tomato sauce, Mozzarella, Vegetables")
    
    # Add to session
    db.session.add_all([r1, r2, r3, p1, p2, p3])
    db.session.commit()
    
    # Create restaurant pizzas
    rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=12, restaurant_id=r1.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=15, restaurant_id=r2.id, pizza_id=p3.id)
    rp4 = RestaurantPizza(price=9, restaurant_id=r3.id, pizza_id=p1.id)
    
    db.session.add_all([rp1, rp2, rp3, rp4])
    db.session.commit()
    
    print("Database seeded successfully!")
    print(f"Created: {Restaurant.query.count()} restaurants")
    print(f"Created: {Pizza.query.count()} pizzas")
    print(f"Created: {RestaurantPizza.query.count()} restaurant pizzas")