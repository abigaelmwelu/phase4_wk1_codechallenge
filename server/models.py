from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates


db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)

   
    pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', cascade='all, delete-orphan')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
        }

    @validates('name')
    def validates_name(self,key, name):
        if len(name) > 50:
            raise ValueError ('Invalid: Name must be less than 50 characters.')
        return name
    
class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # def __repr__(self):
    #     return f''
    
    restaurants = db.relationship('RestaurantPizza', back_populates='pizza', cascade='all, delete-orphan')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients
        }

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'resturants_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    pizza = db.relationship('Pizza', back_populates='restaurants')
    restaurant = db.relationship('Restaurant', back_populates='pizzas')

    def serialize(self):
        return self.pizza.seralize()
    
    @validates('price')
    def validate_price(self,key,  price):
        if not (1 <= price<= 30):
            raise ValueError('price must be between 1 and 30')
        return price
