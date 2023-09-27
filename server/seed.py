from app import app, db, Restaurant, Pizza, RestaurantPizza

def create_sample_data():
    with app.app_context():
        Restaurant.query.delete()
        db.create_all()

        restaurant1 = Restaurant(name="munch", address="123 westlands St")
        restaurant2 = Restaurant(name="pizza inn ", address="456 ngong road St")

   
        pizza1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
        pizza2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")


        db.session.add(restaurant1)
        db.session.add(restaurant2)
        db.session.add(pizza1)
        db.session.add(pizza2)


        restaurant_pizza1 = RestaurantPizza(price=10.99, pizza=pizza1, restaurant=restaurant1)
        restaurant_pizza2 = RestaurantPizza(price=12.99, pizza=pizza2, restaurant=restaurant2)


        db.session.add(restaurant_pizza1)
        db.session.add(restaurant_pizza2)

        db.session.commit()

        print("added to the database.")

if __name__ == "__main__":
    create_sample_data()
