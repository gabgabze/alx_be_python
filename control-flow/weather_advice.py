"""weather= input("What's the weather like today? (sunny/rainy/cold):" )

if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")

elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")

elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")

else:
    print("Sorry, I don't have recommendations for this weather.")"""


class Product:

    def __init__(self, name, price, quantity = 30):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity


std = Product("Molly", 18, 3)
print(std.total_value())
print(std.__str__())