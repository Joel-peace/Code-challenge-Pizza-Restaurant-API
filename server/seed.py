
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from server.app import app
from server import db
from server.models import Restaurant, Pizza, RestaurantPizza

def seed_database():
    with app.app_context():
        print("Starting database seed...")

        print("Clearing old data...")
        RestaurantPizza.query.delete()
        Restaurant.query.delete()
        Pizza.query.delete()
        db.session.commit()
        print("Old data cleared.")

        print("Creating restaurants...")
        r1 = Restaurant(name="Pizza Palace", address="123 Main St")
        r2 = Restaurant(name="Italian Corner", address="456 Oak Ave")
        r3 = Restaurant(name="Slice House", address="789 Pine Rd")
        db.session.add_all([r1, r2, r3])
        db.session.commit()
        print("Created restaurants.")

        print("Creating pizzas...")
        p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
        p2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
        p3 = Pizza(name="Vegetarian", ingredients="Tomato, Mozzarella, Veggies")
        db.session.add_all([p1, p2, p3])
        db.session.commit()
        print("Created pizzas.")

        print("Linking restaurants and pizzas...")
        rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
        rp2 = RestaurantPizza(price=12, restaurant_id=r1.id, pizza_id=p2.id)
        rp3 = RestaurantPizza(price=15, restaurant_id=r2.id, pizza_id=p3.id)
        rp4 = RestaurantPizza(price=9, restaurant_id=r3.id, pizza_id=p1.id)
        db.session.add_all([rp1, rp2, rp3, rp4])
        db.session.commit()
        print("Created restaurant-pizza links.")

        print("\nDatabase seeded successfully!")

if __name__ == '__main__':
    seed_database()