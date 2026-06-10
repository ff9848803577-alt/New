menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.60,
        "chips": 3.50,
        "soda": 1.25}

cart = []
total = 0

print("-----MENU-----")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

while True:
    food = input("Select an item (q to quit): ").strip().lower()  
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Item not on menu, try again.")  # Optional: helpful feedback

print("\n-----YOUR ORDER-----")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")