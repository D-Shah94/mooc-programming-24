# Write your solution here

frequency = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
groceries_cost = float(input("How much money do you spend on groceries in a week? "))

weekly_cost = groceries_cost + (lunch_price * frequency)

print(f"\nAverage food expenditure:\nDaily: {(weekly_cost) / 7} euros\nWeekly: {weekly_cost} euros")
