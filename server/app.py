
from flask import Flask
from flask_migrate import Migrate
from server.config import Config
from server import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
 
    db.init_app(app)

    migrate = Migrate(app, db)
    

    with app.app_context():
        from server.models import Restaurant, Pizza, RestaurantPizza
    

    from server.controllers.restaurant_controller import restaurant_bp
    from server.controllers.pizza_controller import pizza_bp
    from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp
    
    app.register_blueprint(restaurant_bp, url_prefix='/restaurants')
    app.register_blueprint(pizza_bp, url_prefix='/pizzas')
    app.register_blueprint(restaurant_pizza_bp, url_prefix='/restaurant_pizzas')
    
    @app.route('/')
    def index():
        return "Pizza Restaurant API"
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5555, debug=True)