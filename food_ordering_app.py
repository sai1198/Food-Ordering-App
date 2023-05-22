import random

class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = random.randint(1000, 9999)  
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class Admin:
    def __init__(self):
        self.food_items = []

    def add_food_item(self, name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        self.food_items.append(food_item)
        print("Food item added successfully.")

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                print("Food item edited successfully.")
                return
        print("Food item not found.")

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                print("Food item removed successfully.")
                return
        print("Food item not found.")

    def view_all_food_items(self):
        if self.food_items:
            for food_item in self.food_items:
                print(f"Food ID: {food_item.food_id}")
                print(f"Name: {food_item.name}")
                print(f"Quantity: {food_item.quantity}")
                print(f"Price: {food_item.price}")
                print(f"Discount: {food_item.discount}")
                print(f"Stock: {food_item.stock}")
                print()
        else:
            print("No food items found.")

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []

    def place_new_order(self, food_items):
        if not food_items:
            print("No items selected.")
            return

        selected_items = []
        for index in food_items:
            if 0 <= index < len(admin.food_items):
                selected_items.append(admin.food_items[index])

        if not selected_items:
            print("Invalid item selection.")
            return

        print("Selected Items:")
        total_price = 0
        for item in selected_items:
            total_price += item.price
            print(f"{item.name} ({item.quantity}) [INR {item.price}]")

        order_id = random.randint(10000, 99999)
        self.order_history.append(order_id)
        print("Order placed successfully. Order ID:", order_id)
        print("Total Price: INR", total_price)

    def view_order_history(self):
        if self.order_history:
            print("Order History:")
            for order_id in self.order_history:
                print("Order ID:", order_id)
            print()
        else:
            print("No order history found.")

    def update_profile(self, full_name=None, phone_number=None, email=None, address=None, password=None):
        if full_name:
            self.full_name = full_name
        if phone_number:
            self.phone_number = phone_number
        if email:
            self.email = email
        if address:
            self.address = address
        if password:
            self.password = password

        print("Profile updated successfully.")



admin = Admin()

admin.add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 100)
admin.add_food_item("Vegan Burger", "1 piece", 320, 0, 50)
admin.add_food_item("Truffle Cake", "500gm", 900, 0, 20)

admin.view_all_food_items()

admin.edit_food_item(1001, "Vegan Burger", "2 pieces", 350, 0, 30)
admin.view_all_food_items()

admin.remove_food_item(1002)
admin.view_all_food_items()


user = User("John Doe", "1234567890", "john.doe@example.com", "123, Street Name, City", "password")

user.place_new_order([1, 2])
user.view_order_history()

user.update_profile(full_name="John Smith", address="456, New Street, City")
