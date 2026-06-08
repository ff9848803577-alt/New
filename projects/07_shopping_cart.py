foods = [] # we arent using tuples bcz they are immutable
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit):")
    if food.lower() =="q": # we either can use upper or lower case q to quit using .lower 
        break

    price = float(input(f"Enter a price of a {food}: $"))
    foods.append(food)
    prices.append(price) # append is a list method used to add anything to the list

print("------Your Cart------")

for food  in foods:
    print(food, end="") # end="" using this no new line is added 

for price in prices:
    total += price

print(f"Your total is :{total} $")


