"""
total price = 0
get number of items
while number of items < 0:
    display Invalid number of items!
    get number of items
for i in range (0, number of items):
    get price of item
    total price = total price + price of item
if total price > 100:
    total price = total price - (total price * 0.1)
print total price
"""
total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(0, number_of_items):
    price_of_items = float(input("Price of item: "))
    total_price = total_price + price_of_items
if total_price > 100:
    total_price = total_price - (total_price * 0.1)
print(f"Total price for {number_of_items} items is ${total_price:.2f}")