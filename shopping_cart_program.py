#shopping cart program

foods = []
prices = []
total = 0

while True:
  food = input("what food u like to buy or q(to quit?")
  if food.lower() == "q":
    print("you quit")
    break
  else:
    price = float(input(f"Enter the price of a {food} rs"))
    foods.append(food)
    prices.append(price)

print("-----YOUR CART-----")

for food in foods:
    print(food)

for price in prices:
   total += price
   
   
print(f"your total price is Rs {price}")
