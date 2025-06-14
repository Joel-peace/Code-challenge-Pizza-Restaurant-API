
from server import db

class Pizza(db.Model):
    __tablename__ = 'pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)
    

    restaurants = db.relationship('RestaurantPizza', backref='pizza')
    
    def __repr__(self):
        return f'<Pizza {self.name}>'