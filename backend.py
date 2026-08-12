menu = {
    "Pizza": 200,
    "Burger": 150,
    "Biryani": 250,
    "Pasta": 180,
    "French Fries": 100,
    "Coke": 50
}

def calculate_total(food, quantity):
    return menu[food] * quantity
