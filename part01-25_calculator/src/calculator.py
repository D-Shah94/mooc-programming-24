# Write your solution here
first = int(input("Number 1: "))
second = int(input("Number 2: "))
operation = input("Operation: ")

if operation == "add":
    print(f"{first} + {second} = {first + second}")

if operation == "multiply":
    print(f"{first} * {second} = {first * second}")

if operation == "subtract":
    print(f"{first} - {second} = {first - second}")