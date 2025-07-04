
from flask import Flask
from flask_migrate import Migrate

from server.config import Config
from server import db

from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(restaurant_bp, url_prefix='/restaurants')
app.register_blueprint(pizza_bp, url_prefix='/pizzas')
app.register_blueprint(restaurant_pizza_bp, url_prefix='/restaurant_pizzas')

@app.route('/')
def index():
    return "<h1>Welcome to the Pizza Restaurant API!</h1>"

if __name__ == '__main__':
    app.run(port=5555, debug=True)