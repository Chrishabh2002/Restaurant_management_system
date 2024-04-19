class Dish:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def __str__(self):
        return f"{self.name} - ₹{self.price}"

class Menu:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def display_menu(self):
        print("Menu:")
        for dish in self.dishes:
            print(dish)

class Customer:
    def __init__(self, name, table_number):
        self.name = name
        self.table_number = table_number
        self.order = []
        self.feedback = None

    def __str__(self):
        return f"{self.name} (Table: {self.table_number})"

    def add_to_order(self, dish):
        self.order.append(dish)

    def display_order(self):
        print("Order:")
        for dish in self.order:
            print(dish)

    def leave_feedback(self, rating, comment):
        self.feedback = (rating, comment)

    def generate_bill(self):
        total_price = sum(dish.price for dish in self.order)
        print("\nBill Invoice:")
        print(f"Customer: {self.name}")
        print("Order:")
        for dish in self.order:
            print(f"{dish.name}: ₹{dish.price}")
        print(f"Total: ₹{total_price}")

    def display_feedback(self):
        if self.feedback:
            print("\nFeedback:")
            print(f"Rating: {self.feedback[0]}")
            print(f"Comment: {self.feedback[1]}")
        else:
            print("\nNo feedback provided.")

class OnlineOrder:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.order = []

    def add_to_order(self, dish):
        self.order.append(dish)

    def display_order(self):
        print("Online Order:")
        for dish in self.order:
            print(dish)

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu()
        self.customers = []
        self.online_orders = []

    def add_dish_to_menu(self, dish):
        self.menu.add_dish(dish)

    def display_menu(self):
        self.menu.display_menu()

    def add_customer(self, customer):
        self.customers.append(customer)

    def take_order(self, customer_name):
        print("Enter the name of the dish you want to order (type 'done' to finish):")
        while True:
            order_item = input(">> ")
            if order_item.lower() == 'done':
                break
            dish = self.find_dish(order_item)
            if dish:
                customer.add_to_order(dish)
                print(f"{dish.name} added to {customer_name}'s order.")
            else:
                print(f"{order_item} not found in the menu.")

    def find_dish(self, dish_name):
        for dish in self.menu.dishes:
            if dish.name == dish_name:
                return dish
        return None

    def place_online_order(self, customer_name, dish_names):
        order = OnlineOrder(customer_name)
        for dish_name in dish_names:
            dish = self.find_dish(dish_name)
            if dish:
                order.add_to_order(dish)
            else:
                print(f"{dish_name} not found in the menu.")
                return False
        self.online_orders.append(order)
        print(f"Online order placed by {customer_name}.")
        return True

    def display_online_orders(self):
        print("Online Orders:")
        for order in self.online_orders:
            print(f"Customer: {order.customer_name}")
            order.display_order()


dish1 = Dish("Butter Chicken", 300, ["Chicken", "Butter", "Cream", "Tomato"])
dish2 = Dish("Paneer Tikka", 250, ["Paneer", "Yogurt", "Spices", "Capsicum"])
dish3 = Dish("Biryani", 350, ["Basmati Rice", "Chicken", "Spices", "Onion"])
dish4 = Dish("Masala Dosa", 120, ["Rice batter", "Potato", "Onion", "Spices"])
dish5 = Dish("Chole Bhature", 180, ["Chickpeas", "Flour", "Spices", "Tomato"])
dish6 = Dish("Samosa", 30, ["Potato", "Peas", "Spices", "Pastry"])
dish7 = Dish("Palak Paneer", 280, ["Paneer", "Spinach", "Cream", "Spices"])
dish8 = Dish("Pani Puri", 50, ["Semolina", "Potato", "Chickpeas", "Tamarind"])
dish9 = Dish("Rogan Josh", 320, ["Lamb", "Yogurt", "Spices", "Onion"])
dish10 = Dish("Gulab Jamun", 60, ["Milk powder", "Sugar", "Saffron", "Cardamom"])

menu = Menu()
menu.add_dish(dish1)
menu.add_dish(dish2)
menu.add_dish(dish3)
menu.add_dish(dish4)
menu.add_dish(dish5)
menu.add_dish(dish6)
menu.add_dish(dish7)
menu.add_dish(dish8)
menu.add_dish(dish9)
menu.add_dish(dish10)

restaurant = Restaurant("Taste of India")
restaurant.menu = menu

customer_name = input("Please enter your name: ")
table_number = int(input("Please enter your table number: "))
customer = Customer(customer_name, table_number)
restaurant.add_customer(customer)

restaurant.display_menu()
restaurant.take_order(customer_name)

customer.display_order()

# Obtain feedback from the customer
rating = int(input("Please enter your rating (1-5): "))
comment = input("Please enter your feedback comment: ")
customer.leave_feedback(rating, comment)

# Generate bill invoice and display feedback
customer.generate_bill()
customer.display_feedback()

# Thank you note
print("\nThank you for dining with us!")
