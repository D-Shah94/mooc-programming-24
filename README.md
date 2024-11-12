
# Python Programming MOOC 2024

Welcome to the **Python Programming MOOC 2024**, which includes both introductory and advanced topics in Python programming. This course is designed to build your skills from the basics to advanced techniques.

## Table of Contents

### Introduction to Programming
1. [Introduction to Programming](#introduction-to-programming)
   - [Getting Started](#getting-started)
   - [Variables and Data Types](#variables-and-data-types)
   - [Basic Input and Output](#basic-input-and-output)
   - [Conditional Statements](#conditional-statements)
   - [Loops](#loops)
   - [Functions](#functions)
2. [Data Structures](#2-data-structures)
   - [Lists](#lists)
   - [Tuples](#tuples)
   - [Dictionaries](#dictionaries)
   - [Sets](#sets)
3. [Advanced Functions and Modules](#3-advanced-functions-and-modules)
   - [Lambda Functions](#lambda-functions)
   - [List Comprehensions](#list-comprehensions)
   - [Modules and Packages](#modules-and-packages)
4. [Object-Oriented Programming](#4-object-oriented-programming)

### Advanced Course in Programming
1. [Functions as Arguments](#1-functions-as-arguments)
2. [Generators](#2-generators)
3. [Functional Programming](#3-functional-programming)
4. [Regular Expressions](#4-regular-expressions)
5. [Introduction to Pygame](#5-introduction-to-pygame)
6. [Animation in Pygame](#6-animation-in-pygame)
7. [Handling Events in Pygame](#7-handling-events-in-pygame)
8. [Advanced Pygame Techniques](#8-advanced-pygame-techniques)
9. [Game Project: Sokoban](#9-game-project-sokoban)
10. [Creating Your Own Game](#10-creating-your-own-game)

---

<br><br> <!-- This adds extra space -->

## 1. Introduction to Programming

### Getting Started

#### Learning Objectives

- Understand what programming is and why it's useful.
- Install Python and set up a development environment.
- Write and run your first Python program.

#### Introduction

Programming is the process of creating instructions that a computer can execute. Python is a high-level programming language known for its readability and simplicity.

#### Your First Python Program

To write a Python program, you can use a simple text editor or an Integrated Development Environment (IDE) like Visual Studio Code.

**Example:**

```python
print("Hello, World!")
```

**Output:**

```
Hello, World!
```

---

### Variables and Data Types

#### Learning Objectives

- Understand variables and how to assign values to them.
- Learn about different data types in Python.
- Perform basic arithmetic operations.

#### Variables

A variable stores a value that can be used and modified throughout your program.

**Syntax:**

```python
variable_name = value
```

**Example:**

```python
age = 25
name = "Alice"
is_student = True
```

#### Data Types

- **Integers (`int`):** Whole numbers (e.g., `10`, `-5`).
- **Floating-point numbers (`float`):** Numbers with decimals (e.g., `3.14`, `-0.001`).
- **Strings (`str`):** Text enclosed in quotes (e.g., `"Hello"`).
- **Booleans (`bool`):** `True` or `False`.

#### Arithmetic Operations

- **Addition:** `+`
- **Subtraction:** `-`
- **Multiplication:** `*`
- **Division:** `/`
- **Exponentiation:** `**`
- **Modulo:** `%`

**Example:**

```python
x = 10
y = 3

print("Sum:", x + y)           # Output: Sum: 13
print("Difference:", x - y)    # Output: Difference: 7
print("Product:", x * y)       # Output: Product: 30
print("Quotient:", x / y)      # Output: Quotient: 3.3333333333333335
print("Power:", x ** y)        # Output: Power: 1000
print("Remainder:", x % y)     # Output: Remainder: 1
```

---

### Basic Input and Output

#### Learning Objectives

- Use the `input()` function to get user input.
- Format strings for output.
- Convert input strings to other data types.

#### Getting User Input

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

**Type Conversion**

User input from `input()` is always a string. To use it as a number, you need to convert it.

**Example:**

```python
age = int(input("Enter your age: "))
print("Next year, you will be", age + 1)
```

---

### Conditional Statements

#### Learning Objectives

- Understand how to use `if`, `elif`, and `else` statements.
- Implement decision-making in your programs.
- Use comparison and logical operators.

#### Conditional Syntax

```python
if condition:
    # code block
elif another_condition:
    # another code block
else:
    # default code block
```

#### Comparison Operators

- **Equal to:** `==`
- **Not equal to:** `!=`
- **Greater than:** `>`
- **Less than:** `<`
- **Greater than or equal to:** `>=`
- **Less than or equal to:** `<=`

#### Logical Operators

- **`and`**
- **`or`**
- **`not`**

**Example:**

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
elif age > 12:
    print("You are a teenager.")
else:
    print("You are a child.")
```

---

### Loops

#### Learning Objectives

- Use `while` loops to repeat code while a condition is true.
- Use `for` loops to iterate over sequences.
- Understand `break` and `continue` statements.

#### While Loops

```python
count = 0
while count < 5:
    print("Count is:", count)
    count += 1
```

#### For Loops

```python
for i in range(5):
    print("Iteration:", i)
```

- `range(n)` generates numbers from `0` to `n-1`.

#### Break and Continue

- **`break`**: Exit the loop immediately.
- **`continue`**: Skip the rest of the code inside the loop for the current iteration.

**Example:**

```python
for num in range(1, 11):
    if num == 5:
        continue
    if num == 8:
        break
    print(num)
```

**Output:**

```
1
2
3
4
6
7
```

---

### Functions

#### Learning Objectives

- Define and call functions.
- Understand parameters and return values.
- Use default parameter values.

#### Defining Functions

```python
def function_name(parameters):
    # code block
    return value
```

#### Example:

```python
def greet(name):
    return "Hello, " + name + "!"

print(greet("Alice"))
```

**Output:**

```
Hello, Alice!
```

#### Default Parameters

```python
def greet(name="Guest"):
    return "Hello, " + name + "!"

print(greet())
print(greet("Bob"))
```

**Output:**

```
Hello, Guest!
Hello, Bob!
```

---
<br><br> <!-- This adds extra space -->

## 2. Data Structures

### Lists

#### Learning Objectives

- Create and manipulate lists.
- Access list elements using indices.
- Use list methods for common operations.

#### Creating Lists

```python
fruits = ["apple", "banana", "cherry"]
```

#### Accessing Elements

```python
print(fruits[0])   # Output: apple
print(fruits[-1])  # Output: cherry
```

#### List Methods

- **`append()`**: Add an item to the end.
- **`insert()`**: Insert an item at a specified index.
- **`remove()`**: Remove an item by value.
- **`pop()`**: Remove an item by index and return it.
- **`sort()`**: Sort the list.

**Example:**

```python
numbers = [3, 1, 4, 1, 5]
numbers.append(9)
numbers.sort()
print(numbers)   # Output: [1, 1, 3, 4, 5, 9]
```

---

### Tuples

#### Learning Objectives

- Understand tuples and how they differ from lists.
- Use tuples to store immutable sequences of data.

#### Creating Tuples

```python
coordinates = (10, 20)
```

#### Accessing Elements

```python
x = coordinates[0]
y = coordinates[1]
```

#### Immutable Nature

Tuples cannot be modified after creation.

---

### Dictionaries

#### Learning Objectives

- Create and use dictionaries for key-value pairs.
- Access, add, and remove items in a dictionary.

#### Creating Dictionaries

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
```

#### Accessing Values

```python
print(person["name"])    # Output: Alice
```

#### Adding and Removing Items

```python
person["email"] = "alice@example.com"
del person["age"]
```

#### Dictionary Methods

- **`keys()`**: Returns a list of keys.
- **`values()`**: Returns a list of values.
- **`items()`**: Returns a list of `(key, value)` tuples.

---

### Sets

#### Learning Objectives

- Understand sets and their properties.
- Perform set operations like union, intersection, and difference.

#### Creating Sets

```python
set_a = {1, 2, 3}
set_b = set([3, 4, 5])
```

#### Set Operations

- **Union:** `set_a | set_b`
- **Intersection:** `set_a & set_b`
- **Difference:** `set_a - set_b`

**Example:**

```python
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a | set_b)  # Output: {1, 2, 3, 4, 5}
print(set_a & set_b)  # Output: {3}
print(set_a - set_b)  # Output: {1, 2}
```

---
<br><br> <!-- This adds extra space -->

## 3. Advanced Functions and Modules

### Lambda Functions

#### Learning Objectives

- Understand anonymous functions using `lambda`.
- Use lambda functions for short, simple functions.

#### Syntax

```python
lambda arguments: expression
```

#### Example:

```python
add = lambda x, y: x + y
print(add(3, 5))   # Output: 8
```

---

### List Comprehensions

#### Learning Objectives

- Create lists using list comprehensions for concise code.
- Understand how to include conditions in list comprehensions.

#### Syntax

```python
[expression for item in iterable if condition]
```

#### Example:

```python
squares = [x ** 2 for x in range(10)]
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
```

---

### Modules and Packages

#### Learning Objectives

- Understand how to use built-in and external modules.
- Learn how to install packages using `pip`.
- Create and import your own modules.

#### Importing Modules

```python
import math
print(math.sqrt(16))   # Output: 4.0
```

#### Installing Packages

Use `pip` to install external packages.

```bash
pip install requests
```

#### Creating Your Own Module

Create a file `mymodule.py`:

```python
def greet(name):
    return "Hello, " + name + "!"
```

Import and use it:

```python
import mymodule

print(mymodule.greet("Alice"))
```

---
<br><br> <!-- This adds extra space -->

## 4. Object-Oriented Programming

### Classes and Objects

#### Learning Objectives

- Define classes and create objects.
- Understand instance variables and methods.
- Use the `__init__` method for initialization.

#### Defining a Class

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + " says woof!")
```

#### Creating Objects

```python
dog1 = Dog("Fido")
dog1.bark()   # Output: Fido says woof!
```

---

### Inheritance

#### Learning Objectives

- Understand how inheritance allows classes to derive from other classes.
- Override methods in derived classes.

#### Example:

```python
class Animal:
    def eat(self):
        print("This animal is eating.")

class Cat(Animal):
    def meow(self):
        print("Meow!")

cat = Cat()
cat.eat()   # Output: This animal is eating.
cat.meow()  # Output: Meow!
```

---

### Polymorphism

#### Learning Objectives

- Understand polymorphism and method overriding.
- Use polymorphism to write flexible code.

#### Example:

```python
class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2

shapes = [Square(4), Circle(3)]

for shape in shapes:
    print("Area:", shape.area())
```

**Output:**

```
Area: 16
Area: 28.2744
```

---

### Encapsulation

#### Learning Objectives

- Understand encapsulation and access modifiers.
- Use getters and setters to control access to attributes.

#### Example:

```python
class Person:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

person = Person("Alice")
print(person.get_name())  # Output: Alice
person.set_name("Bob")
print(person.get_name())  # Output: Bob
```

---

## 5. File Handling

### Reading and Writing Files

#### Learning Objectives

- Open and read files using the `open()` function.
- Write data to files.
- Use context managers to handle files.

#### Reading Files

```python
with open("example.txt", "r") as file:
    contents = file.read()
    print(contents)
```

#### Writing Files

```python
with open("output.txt", "w") as file:
    file.write("This is a test.")
```

---

### Working with CSV Files

#### Learning Objectives

- Use the `csv` module to read and write CSV files.
- Understand how to handle different delimiters.

#### Reading CSV Files

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file, delimiter=",")
    for row in reader:
        print(row)
```

#### Writing CSV Files

```python
import csv

data = [
    ["Name", "Age"],
    ["Alice", 30],
    ["Bob", 25]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

---

### Exception Handling

#### Learning Objectives

- Use `try`, `except`, `else`, and `finally` blocks to handle exceptions.
- Catch specific exceptions.
- Raise exceptions when needed.

#### Basic Exception Handling

```python
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")
```

---

## 6. Modules and Libraries

### Using Built-in Modules

#### Learning Objectives

- Import and use modules from the Python Standard Library.
- Explore functions available in common modules like `math`, `random`, and `datetime`.

#### Example: `math` Module

```python
import math

print(math.factorial(5))   # Output: 120
print(math.gcd(48, 18))    # Output: 6
```

#### Example: `random` Module

```python
import random

print(random.randint(1, 10))   # Random integer between 1 and 10
```

---

### Creating Your Own Modules

#### Learning Objectives

- Organize code into modules for better structure.
- Use `if __name__ == "__main__"` to include test code.

#### Example Module: `string_helper.py`

```python
def change_case(orig_string: str) -> str:
    return orig_string.swapcase()

def split_in_half(orig_string: str):
    mid = len(orig_string) // 2
    return orig_string[:mid], orig_string[mid:]

def remove_special_characters(orig_string: str) -> str:
    import string
    allowed_chars = string.ascii_letters + string.digits + ' '
    return ''.join(c for c in orig_string if c in allowed_chars)

if __name__ == "__main__":
    # Test cases
    print(change_case("Hello World!"))  # Output: hELLO wORLD!
    p1, p2 = split_in_half("HelloWorld")
    print(p1)  # Output: Hello
    print(p2)  # Output: World
    print(remove_special_characters("Hello, World!"))  # Output: Hello World
```

#### Using the Module

```python
import string_helper

print(string_helper.change_case("Hello World!"))
```

**Output:**

```
hELLO wORLD!
```

---

## 7. Advanced Topics

### Randomness

#### Learning Objectives

- Use the `random` module to generate random numbers.
- Understand how to shuffle lists and select random elements.

#### Generating Random Numbers

```python
import random

print(random.randint(1, 6))  # Simulate a die roll
```

#### Shuffling Lists

```python
import random

deck = list(range(1, 53))
random.shuffle(deck)
print(deck)
```

#### Selecting Random Samples

```python
import random

lottery_numbers = random.sample(range(1, 41), 7)
print(sorted(lottery_numbers))
```

---

### Dates and Times

#### Learning Objectives

- Use the `datetime` module to work with dates and times.
- Calculate time differences and format dates.

#### Getting Current Date and Time

```python
from datetime import datetime

now = datetime.now()
print(now)
```

#### Formatting Dates

```python
formatted_date = now.strftime("%d/%m/%Y %H:%M")
print(formatted_date)
```

#### Calculating Time Differences

```python
from datetime import datetime, timedelta

new_year = datetime(now.year + 1, 1, 1)
difference = new_year - now
print("Days until New Year:", difference.days)
```

---

### Data Processing

#### Learning Objectives

- Read and process JSON data using the `json` module.
- Fetch and process data from the internet.
- Work with data retrieved from APIs.

#### Reading JSON Files

```python
import json

with open("data.json", "r") as file:
    data = json.load(file)
```

#### Fetching Data from the Web

```python
import urllib.request
import json

url = "https://api.example.com/data"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
```

#### Example: Processing Course Data

Suppose we have a URL that provides course data in JSON format. We can retrieve and process it as follows:

```python
import urllib.request
import json

def retrieve_courses():
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    active_courses = [
        (course['fullName'], course['name'], course['year'], sum(course['exercises']))
        for course in data if course['enabled']
    ]
    return active_courses
```

---

### Additional Python Features

#### Learning Objectives

- Utilize single-line conditionals and the ternary operator.
- Understand the use of `pass` for empty code blocks.
- Use loops with `else` clauses.
- Work with default parameters and variable-length argument lists.

#### Single-Line Conditionals (Ternary Operator)

```python
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)   # Output: Adult
```

#### Using `pass`

```python
def my_function():
    pass  # Placeholder for future code
```

#### Loops with `else`

```python
for item in iterable:
    if condition:
        break
else:
    print("Loop completed without break")
```

#### Default Parameters

```python
def greet(name="Guest"):
    print("Hello,", name)

greet()          # Output: Hello, Guest
greet("Alice")   # Output: Hello, Alice
```

#### Variable-Length Arguments

```python
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3))   # Output: 6
print(add_numbers(5, 10, 15, 20))   # Output: 50
```
---
**Congratulations on completing the "Introduction to Programming" course!**
<br><br> <!-- This adds extra space -->
---
<br><br> <!-- This adds extra space -->



# Advanced Course in Programming

## 1. Functions as Arguments

### Key Concepts

- **Higher-Order Functions**: Functions that accept other functions as arguments or return them as results.
- **Sorting with Custom Criteria**: Using functions to define custom sorting behavior.
- **Lambda Expressions**: Anonymous functions defined using the `lambda` keyword.
- **Passing Functions as Arguments**: Enhancing function flexibility by passing functions as parameters.

### Functions as Arguments in Sorting

Python's built-in `sort` method and `sorted` function allow for custom sorting criteria using the `key` parameter, which accepts a function. This function determines the value used for sorting each item in the list.

**Example**: Sorting a list of tuples based on the second element (price).

```python
def order_by_price(item):
    return item[1]

products = [("banana", 5.95), ("apple", 3.95), ("orange", 4.50), ("watermelon", 4.95)]
products.sort(key=order_by_price)

for product in products:
    print(product)
```

**Output**:

```
('apple', 3.95)
('orange', 4.5)
('watermelon', 4.95)
('banana', 5.95)
```

In this example, `order_by_price` is passed to `sort` via the `key` parameter. The function extracts the price from each tuple, allowing the list to be sorted by price.

### Defining Functions Within Functions

Functions can be defined inside other functions, which is useful when the helper function is not needed elsewhere.

```python
def sort_by_price(items):
    def order_by_price(item):
        return item[1]
    return sorted(items, key=order_by_price)
```

### Lambda Expressions

Lambda expressions provide a concise way to define anonymous functions. They are especially useful for small functions used as arguments.

**Syntax**:

```python
lambda parameters: expression
```

**Example**: Sorting products by price using a lambda expression.

```python
products.sort(key=lambda item: item[1])
```

**Example**: Sorting strings based on their last character.

```python
strings = ["Mickey", "Mack", "Marvin", "Minnie", "Merl"]
strings.sort(key=lambda word: word[-1])

for word in strings:
    print(word)
```

**Output**:

```
Minnie
Mack
Merl
Marvin
Mickey
```

### Using Functions with Built-in Functions

Lambda expressions can be used with built-in functions like `min`, `max`, and `sorted`.

**Example**: Finding the longest recording.

```python
class Recording:
    def __init__(self, name, performer, year, runtime):
        self.name = name
        self.performer = performer
        self.year = year
        self.runtime = runtime

recordings = [
    Recording("Nevermind", "Nirvana", 1991, 43),
    Recording("Let It Be", "Beatles", 1969, 35),
    Recording("Joshua Tree", "U2", 1986, 50),
]

longest = max(recordings, key=lambda rec: rec.runtime)
print(f"The longest recording: {longest.name} by {longest.performer}, {longest.runtime} min.")
```

**Output**:

```
The longest recording: Joshua Tree by U2, 50 min.
```

### Passing Functions to Custom Functions

You can create functions that accept other functions as parameters to provide customizable behavior.

**Example**: A function that performs an operation on two numbers.

```python
def perform_operation(operation):
    return operation(10, 5)

print(perform_operation(lambda x, y: x + y))  # Output: 15
print(perform_operation(lambda x, y: x * y))  # Output: 50
```

### Practical Applications

**Example**: Filtering lines in a file based on a criterion function.

```python
def copy_lines(source_file, target_file, criterion=lambda x: True):
    with open(source_file) as source, open(target_file, "w") as target:
        for line in source:
            line = line.strip()
            if criterion(line):
                target.write(line + "\n")
```

---
<br><br> <!-- This adds extra space -->

## 2. Generators

### Key Concepts

- **Generators**: Functions that allow you to declare a function that behaves like an iterator.
- **Yield Keyword**: Used to produce a value from a generator and pause its state.
- **Generator Expressions**: Similar to list comprehensions but produce generators.

### Understanding Generators

Generators provide a way to iterate over data without storing the entire dataset in memory. They are especially useful for large datasets or infinite sequences.

**Example**: A simple counter generator.

```python
def counter(max_value):
    number = 0
    while number <= max_value:
        yield number
        number += 1

numbers = counter(5)
for number in numbers:
    print(number)
```

**Output**:

```
0
1
2
3
4
5
```

### The `yield` Keyword

- Acts like a return statement but pauses the function and saves its state.
- When the generator is called again, it resumes from where it left off.

**Example**: Generating even numbers within a range.

```python
def even_numbers(beginning, maximum):
    number = beginning
    while number <= maximum:
        if number % 2 == 0:
            yield number
        number += 1
```

### Infinite Generators

Generators can be designed to produce an infinite sequence of values.

**Example**: Generating prime numbers indefinitely.

```python
def prime_numbers():
    num = 2
    while True:
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            yield num
        num += 1
```

### Generator Expressions

Similar to list comprehensions but with parentheses instead of brackets.

**Syntax**:

```python
(expression for item in iterable if condition)
```

**Example**: Generating squares of numbers.

```python
squares = (x ** 2 for x in range(1, 10))
for square in squares:
    print(square)
```

**Output**:

```
1
4
9
16
25
36
49
64
81
```

### Practical Applications

**Example**: Random word generator.

```python
import random

def word_generator(characters, length, amount):
    for _ in range(amount):
        yield ''.join(random.choice(characters) for _ in range(length))

words = word_generator("abcdefg", 3, 5)
for word in words:
    print(word)
```

---
<br><br> <!-- This adds extra space -->

## 3. Functional Programming

### Key Concepts

- **Functional Programming**: A programming paradigm where programs are constructed by applying and composing functions.
- **Immutability**: Avoiding changing state and mutable data.
- **Higher-Order Functions**: Functions that take other functions as arguments or return them.
- **Pure Functions**: Functions that have no side effects.

### The `map` Function

Applies a function to every item in an iterable.

**Syntax**:

```python
map(function, iterable)
```

**Example**: Converting a list of strings to integers.

```python
str_list = ["1", "2", "3"]
integers = list(map(int, str_list))
print(integers)
```

**Output**:

```
[1, 2, 3]
```

### The `filter` Function

Filters items in an iterable based on a function that returns `True` or `False`.

**Syntax**:

```python
filter(function, iterable)
```

**Example**: Filtering even numbers.

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
```

**Output**:

```
[2, 4]
```

### The `reduce` Function

Applies a rolling computation to sequential pairs of values in a list.

**Syntax**:

```python
from functools import reduce
reduce(function, iterable, initializer)
```

**Example**: Summing a list of numbers.

```python
from functools import reduce

numbers = [1, 2, 3, 4]
total = reduce(lambda acc, x: acc + x, numbers, 0)
print(total)
```

**Output**:

```
10
```

### Combining `map`, `filter`, and `reduce`

Functional programming shines when combining these functions for data processing.

**Example**: Calculating the total credits from passed courses.

```python
from functools import reduce

passed_attempts = filter(lambda attempt: attempt.grade > 0, attempts)
credits = map(lambda attempt: attempt.credits, passed_attempts)
total_credits = reduce(lambda acc, x: acc + x, credits, 0)
```

### Practical Applications

**Example**: Getting a list of student names from course attempts.

```python
def names_of_students(attempts):
    return list(map(lambda attempt: attempt.student_name, attempts))
```

**Example**: Filtering accepted course attempts.

```python
def accepted(attempts):
    return list(filter(lambda attempt: attempt.grade > 0, attempts))
```

---
<br><br> <!-- This adds extra space -->

## 4. Regular Expressions

### Key Concepts

- **Regular Expressions (Regex)**: Sequences of characters that define search patterns.
- **Pattern Matching**: Finding strings that match a specific pattern.
- **Special Characters**: Characters with special meanings in regex (e.g., `^`, `$`, `.`, `*`, `+`).

### Using Regular Expressions in Python

The `re` module provides regex functionality.

**Importing the module**:

```python
import re
```

**Basic Functions**:

- `re.search(pattern, string)`: Searches for the pattern in the string.
- `re.findall(pattern, string)`: Finds all occurrences of the pattern in the string.

**Example**: Finding all numbers in a string.

```python
sentence = "First, 2 !#third 44 five 678xyz962"
numbers = re.findall(r"\d+", sentence)
print(numbers)
```

**Output**:

```
['2', '44', '678', '962']
```

### Regex Syntax Basics

- **Character Classes**:
  - `[abc]`: Matches any one of `a`, `b`, or `c`.
  - `[a-z]`: Matches any lowercase letter.
  - `\d`: Matches any digit (equivalent to `[0-9]`).
- **Quantifiers**:
  - `*`: Matches 0 or more occurrences.
  - `+`: Matches 1 or more occurrences.
  - `{m}`: Matches exactly `m` occurrences.
- **Anchors**:
  - `^`: Matches the start of the string.
  - `$`: Matches the end of the string.
- **Wildcards**:
  - `.`: Matches any single character except newline.

**Example**: Matching a valid time format.

```python
def time_of_day(my_string):
    return bool(re.match(r"^([01]\d|2[0-3]):[0-5]\d:[0-5]\d$", my_string))

print(time_of_day("12:43:01"))  # Output: True
print(time_of_day("33:66:77"))  # Output: False
```

### Practical Examples

**Example**: Checking if a string represents a day of the week abbreviation.

```python
def is_dotw(my_string):
    return bool(re.match(r"^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)$", my_string))
```

**Example**: Validating if all characters in a string are vowels.

```python
def all_vowels(my_string):
    return bool(re.match(r"^[aeiouAEIOU]+$", my_string))
```

### Building a Regex Testing Program

You can create a simple program to test regex patterns against user input.

```python
import re

expression = input("Please type in an expression: ")

while True:
    input_string = input("Please type in a string: ")
    if input_string == "":
        break
    if re.search(expression, input_string):
        print("Found!")
    else:
        print("Not found.")
```

---
<br><br> <!-- This adds extra space -->

## 5. Introduction to Pygame

### Key Concepts

- **Installing Pygame**: Setting up Pygame on your system.
- **Creating a Pygame Window**: Initializing Pygame and displaying a window.
- **Loading and Displaying Images**: Using images in Pygame applications.
- **Event Loop**: Keeping the application running and handling exit events.

### Installing Pygame

To use Pygame, you need to install it using `pip`. Open your command line or terminal and run:

```bash
pip3 install pygame
```

### Creating a Pygame Window

A basic Pygame program initializes the library, creates a window, and enters an event loop.

**Example**: Creating a simple Pygame window.

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
window.fill((0, 0, 0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
```

**Explanation**:

- `pygame.init()`: Initializes all Pygame modules.
- `pygame.display.set_mode((640, 480))`: Creates a window of size 640x480 pixels.
- `window.fill((0, 0, 0))`: Fills the window with black color.
- `pygame.display.flip()`: Updates the entire display.
- **Event Loop**: Listens for events (like closing the window) and handles them.

### Loading and Displaying Images

Pygame allows you to load images and display them in the window.

**Example**: Displaying an image in the window.

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
window.blit(robot, (100, 50))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
```

**Explanation**:

- `pygame.image.load("robot.png")`: Loads an image named `robot.png`.
- `window.blit(robot, (100, 50))`: Draws the image at coordinates (100, 50).
- Images can be drawn multiple times at different positions.

**Note**: Ensure that the image file (`robot.png`) is in the same directory as your script.

### Coordinate System in Pygame

- The coordinate system starts at the top-left corner of the window (0, 0).
- X increases to the right, Y increases downward.
- To center an image, calculate offsets based on image dimensions.

**Example**: Centering an image in the window.

```python
width = robot.get_width()
height = robot.get_height()
window.blit(robot, (320 - width / 2, 240 - height / 2))
```

---
<br><br> <!-- This adds extra space -->

## 6. Animation in Pygame

### Key Concepts

- **Creating Animations**: Updating the position of objects over time.
- **Controlling Frame Rate**: Using `pygame.time.Clock` to regulate animation speed.
- **Bouncing Objects**: Making objects interact with window boundaries.
- **Using Math Functions**: Applying trigonometry for circular motion.

### Moving Objects

To animate an object, update its position in each iteration of the main loop.

**Example**: Moving a robot across the screen.

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")

x = 0
y = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    x += 1
    clock.tick(60)
```

**Explanation**:

- `x += 1`: Moves the robot one pixel to the right each frame.
- `clock.tick(60)`: Caps the frame rate at 60 frames per second.

### Bouncing Off Walls

Reverse the object's direction when it reaches a boundary.

**Example**: Making the robot bounce horizontally.

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    x += velocity
    if velocity > 0 and x + robot.get_width() >= 640:
        velocity = -velocity
    if velocity < 0 and x <= 0:
        velocity = -velocity

    clock.tick(60)
```

### Circular Motion

Use trigonometric functions to move objects in a circle.

**Example**: Rotating the robot around the center.

```python
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")

angle = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    x = 320 + math.cos(angle) * 100 - robot.get_width() / 2
    y = 240 + math.sin(angle) * 100 - robot.get_height() / 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    angle += 0.01
    clock.tick(60)
```

**Explanation**:

- `math.cos(angle)` and `math.sin(angle)` calculate the X and Y offsets.
- Multiplying by 100 sets the radius of the circle.
- Adjusting `angle` changes the rotation over time.

---
<br><br> <!-- This adds extra space -->

## 7. Handling Events in Pygame

### Key Concepts

- **Event Types**: Understanding different event types like keyboard and mouse events.
- **Keyboard Events**: Responding to key presses and releases.
- **Mouse Events**: Handling mouse movements and clicks.
- **Continuous Movement**: Implementing movement while a key is held down.

### Event Loop and Event Types

The event loop retrieves events and allows you to handle them accordingly.

**Example**: Printing all events.

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit()
```

### Handling Keyboard Events

Detect when keys are pressed or released to control objects.

**Example**: Moving the robot with arrow keys.

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")
x = 0
y = 480 - robot.get_height()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
            if event.key == pygame.K_RIGHT:
                x += 10
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
```

**Continuous Movement**:

To move the robot continuously while a key is held down, track the key's state.

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")
x = 0
y = 480 - robot.get_height()

to_right = False
to_left = False
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
        if event.type == pygame.QUIT:
            exit()

    if to_right:
        x += 2
    if to_left:
        x -= 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    clock.tick(60)
```

### Handling Mouse Events

Respond to mouse movements and clicks.

**Example**: Printing mouse click positions.

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Button", event.button, "at", event.pos)
        if event.type == pygame.QUIT:
            exit()
```

**Example**: Placing the robot at the mouse click position.

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0] - robot.get_width() / 2
            y = event.pos[1] - robot.get_height() / 2

            window.fill((0, 0, 0))
            window.blit(robot, (x, y))
            pygame.display.flip()
        if event.type == pygame.QUIT:
            exit()
```

**Example**: Making the robot follow the mouse cursor.

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")

robot_x = 0
robot_y = 0
target_x = 0
target_y = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            target_x = event.pos[0] - robot.get_width() / 2
            target_y = event.pos[1] - robot.get_height() / 2
        if event.type == pygame.QUIT:
            exit()

    if robot_x > target_x:
        robot_x -= 1
    if robot_x < target_x:
        robot_x += 1
    if robot_y > target_y:
        robot_y -= 1
    if robot_y < target_y:
        robot_y += 1

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()
    clock.tick(60)
```

---
<br><br> <!-- This adds extra space -->

## 8. Advanced Pygame Techniques

### Key Concepts

- **Window Title**: Setting the caption of the Pygame window.
- **Drawing Shapes**: Using Pygame functions to draw rectangles, circles, and lines.
- **Displaying Text**: Rendering and displaying text in the window.
- **Combining Techniques**: Creating more complex programs by combining previous concepts.

### Setting the Window Title

Use `pygame.display.set_caption()` to set the window title.

```python
pygame.display.set_caption("My Pygame Window")
```

### Drawing Shapes

Pygame provides functions to draw basic shapes.

**Example**: Drawing a rectangle, circle, and line.

```python
import pygame

pygame.init()
display = pygame.display.set_mode((640, 480))
display.fill((0, 0, 0))

# Draw a green rectangle
pygame.draw.rect(display, (0, 255, 0), (50, 100, 200, 250))
# Draw a red circle
pygame.draw.circle(display, (255, 0, 0), (200, 150), 40)
# Draw a blue line
pygame.draw.line(display, (0, 0, 255), (80, 120), (300, 160), 2)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
```

### Displaying Text

Render text using system fonts or custom fonts.

**Example**: Displaying text on the screen.

```python
import pygame

pygame.init()
display = pygame.display.set_mode((640, 480))
display.fill((0, 0, 0))

# Create a font object
game_font = pygame.font.SysFont("Arial", 24)
# Render text (text, antialias, color)
text = game_font.render("Hello, Pygame!", True, (255, 255, 255))
# Draw the text on the display
display.blit(text, (100, 50))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
```

**Explanation**:

- `pygame.font.SysFont("Arial", 24)`: Creates a font object.
- `font.render("Text", True, color)`: Renders text into an image.
- `display.blit(text, (x, y))`: Draws the text image onto the display.

### Combining Techniques: Example Programs

#### Clock Program

Create a program that displays a clock showing the current system time.

```python
import pygame
import time

pygame.init()
display = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Clock")

font = pygame.font.SysFont("Arial", 72)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    current_time = time.strftime("%H:%M:%S")
    text = font.render(current_time, True, (255, 255, 255))

    display.fill((0, 0, 0))
    display.blit(text, (200, 200))
    pygame.display.flip()

    clock.tick(1)
```

#### Asteroids Game

Create a simple game where the player controls a robot that catches falling asteroids.

```python
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Asteroids")

robot = pygame.image.load("robot.png")
asteroid = pygame.image.load("rock.png")
font = pygame.font.SysFont("Arial", 24)

robot_x = 320 - robot.get_width() / 2
robot_y = 480 - robot.get_height()
asteroid_x = random.randint(0, 640 - asteroid.get_width())
asteroid_y = -asteroid.get_height()
score = 0

clock = pygame.time.Clock()
to_right = False
to_left = False
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

    if not game_over:
        if to_right and robot_x < 640 - robot.get_width():
            robot_x += 5
        if to_left and robot_x > 0:
            robot_x -= 5

        asteroid_y += 5

        if asteroid_y > 480:
            game_over = True

        # Collision detection
        if (robot_x < asteroid_x + asteroid.get_width() and
            robot_x + robot.get_width() > asteroid_x and
            robot_y < asteroid_y + asteroid.get_height() and
            robot_y + robot.get_height() > asteroid_y):
            score += 1
            asteroid_x = random.randint(0, 640 - asteroid.get_width())
            asteroid_y = -asteroid.get_height()

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    window.blit(asteroid, (asteroid_x, asteroid_y))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))
    if game_over:
        game_over_text = font.render("Game Over!", True, (255, 0, 0))
        window.blit(game_over_text, (260, 240))

    pygame.display.flip()
    clock.tick(60)
```

**Explanation**:

- The player controls the robot with left and right arrow keys.
- Asteroids fall from the top of the screen.
- The player gains a point for each asteroid caught.
- The game ends if the player misses an asteroid.

---
<br><br> <!-- This adds extra space -->

## 9. Game Project: Sokoban

### Key Concepts

- **Game Development with Pygame**: Building a complete game using Pygame.
- **Sokoban Game Mechanics**: Understanding the logic behind pushing boxes onto target squares.
- **Game Structure**: Organizing code into classes and methods for better maintainability.
- **Event Handling**: Managing user inputs to control game elements.

### Overview

In this section, we focus on developing a variation of the classic Sokoban game. The objective is to move a robot around a grid to push boxes onto designated target squares using as few moves as possible.

**Game Features**:

- A grid-based map representing the game environment.
- A robot character controlled by the player.
- Boxes that can be pushed by the robot.
- Target squares where boxes need to be placed.
- Move counter to track the number of moves made.
- Ability to start a new game or exit using keyboard inputs.
- Notification when the game is solved.

### Implementing the Game Map

#### Setting Up the Game Class

We define a `Sokoban` class that encapsulates all game functionality.

```python
import pygame

class Sokoban:
    def __init__(self):
        pygame.init()
        self.load_images()
        self.new_game()
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.scale = self.images[0].get_width()
        window_height = self.scale * self.height
        window_width = self.scale * self.width
        self.window = pygame.display.set_mode((window_width, window_height + self.scale))
        pygame.display.set_caption("Sokoban")
        self.game_font = pygame.font.SysFont("Arial", 24)
        self.main_loop()
```

#### Loading Images

We load images representing different game elements and store them in a list for easy access.

```python
def load_images(self):
    self.images = []
    for name in ["floor", "wall", "target", "box", "robot", "done", "target_robot"]:
        self.images.append(pygame.image.load(name + ".png"))
```

#### Creating the Game Grid

We represent the game map as a two-dimensional list called `self.map`.

```python
def new_game(self):
    self.map = [
        # ... (grid data)
    ]
    self.moves = 0  # Initialize move counter
```

#### Drawing the Game Window

We render the game elements on the screen based on the current state of `self.map`.

```python
def draw_window(self):
    self.window.fill((0, 0, 0))
    for y in range(self.height):
        for x in range(self.width):
            square = self.map[y][x]
            self.window.blit(self.images[square], (x * self.scale, y * self.scale))
    # Display move counter
    move_text = self.game_font.render(f"Moves: {self.moves}", True, (255, 0, 0))
    self.window.blit(move_text, (25, self.height * self.scale + 10))
    # Display instructions
    new_game_text = self.game_font.render("F2 = new game", True, (255, 0, 0))
    self.window.blit(new_game_text, (200, self.height * self.scale + 10))
    exit_text = self.game_font.render("Esc = exit game", True, (255, 0, 0))
    self.window.blit(exit_text, (400, self.height * self.scale + 10))
    # Check if game is solved
    if self.game_solved():
        win_text = self.game_font.render("Congratulations, you solved the game!", True, (255, 0, 0))
        text_x = (self.scale * self.width - win_text.get_width()) / 2
        text_y = (self.scale * self.height - win_text.get_height()) / 2
        self.window.blit(win_text, (text_x, text_y))
    pygame.display.flip()
```

### Robot and Boxes Movement Logic

#### Handling Key Events

We update `check_events` to handle arrow key presses and move the robot accordingly.

```python
def check_events(self):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move(0, -1)
            if event.key == pygame.K_RIGHT:
                self.move(0, 1)
            if event.key == pygame.K_UP:
                self.move(-1, 0)
            if event.key == pygame.K_DOWN:
                self.move(1, 0)
            if event.key == pygame.K_F2:
                self.new_game()
            if event.key == pygame.K_ESCAPE:
                exit()
        if event.type == pygame.QUIT:
            exit()
```

#### Finding the Robot

```python
def find_robot(self):
    for y in range(self.height):
        for x in range(self.width):
            if self.map[y][x] in [4, 6]:  # Robot or robot on target
                return (y, x)
```

#### Implementing Movement Logic

```python
def move(self, move_y, move_x):
    if self.game_solved():
        return  # Do not allow movement after winning
    robot_old_y, robot_old_x = self.find_robot()
    robot_new_y = robot_old_y + move_y
    robot_new_x = robot_old_x + move_x

    # Check for wall collision
    if self.map[robot_new_y][robot_new_x] == 1:
        return

    # Check if there's a box to push
    if self.map[robot_new_y][robot_new_x] in [3, 5]:
        box_new_y = robot_new_y + move_y
        box_new_x = robot_new_x + move_x

        # Check if the box can be moved
        if self.map[box_new_y][box_new_x] in [1, 3, 5]:
            return

        # Move the box
        self.map[robot_new_y][robot_new_x] -= 3
        self.map[box_new_y][box_new_x] += 3

    # Move the robot
    self.map[robot_old_y][robot_old_x] -= 4
    self.map[robot_new_y][robot_new_x] += 4
    self.moves += 1  # Increment move counter after a valid move
```

### Finishing the Game

#### Detecting When the Game is Solved

```python
def game_solved(self):
    for y in range(self.height):
        for x in range(self.width):
            if self.map[y][x] in [2, 6]:  # Empty target or robot on target
                return False
    return True  # All targets are covered by boxes
```

#### Displaying a Victory Message

Already included in the `draw_window` method above.

---
<br><br> <!-- This adds extra space -->

## 10. Creating Your Own Game

### Guidelines for Your Game

- **Player Control**: Implement a sprite (e.g., robot) that the player can move.
- **Collectibles/Enemies**: Include items to collect or enemies to avoid.
- **Clear Objective**: Define a clear goal or task for the player.
- **Progress Tracking**: Display a counter or score to show player progress.
- **Code Structure**: Organize your code using classes and functions similar to the Sokoban example.

### Possible Game Ideas

#### Collecting Game

- **Mechanics**:
  - Player moves a robot using arrow keys.
  - Coins or items appear randomly on the screen.
  - Collecting an item increases the score.
  - Enemies move around, and the player must avoid them.
- **Objective**: Collect as many items as possible without colliding with enemies.

#### Rain of Coins

- **Mechanics**:
  - Player controls a robot that moves left and right at the bottom of the screen.
  - Coins fall from the top of the screen.
  - Collecting coins increases the score.
  - Avoid falling enemies or obstacles.
- **Objective**: Achieve the highest score by collecting coins while avoiding dangers.

### Implementing Your Game

- **Initialize Pygame**: Set up the display, fonts, and game clock.
- **Load Resources**: Load images and sounds needed for the game.
- **Game Loop**:
  - **Event Handling**: Process user inputs (keyboard, mouse).
  - **Game Logic**: Update game state (positions, collisions).
  - **Rendering**: Draw all game elements on the screen.
  - **Frame Rate Control**: Use `clock.tick(fps)` to maintain consistent speed.

### Tips for Game Development

- **Start Small**: Begin with basic movement and gradually add features.
- **Use Classes**: Organize game elements (player, enemies, items) into classes.
- **Collision Detection**: Implement logic to handle interactions between objects.
- **User Interface**: Provide clear instructions and feedback to the player.
- **Testing**: Regularly test your game to identify and fix issues early.

### Sharing and Reviewing Games

- **Submitting Your Game**:
  - Ensure all necessary files are included.
  - Provide instructions or comments within the code if needed.
- **Peer Review**:
  - Play games created by others.
  - Provide constructive feedback on gameplay and code quality.
  - Highlight both strengths and areas for improvement.

---

## Additional Notes

### Advantages of Using Functions as Arguments

- **Modularity**: Functions can be reused and combined in different ways.
- **Flexibility**: Functions can be passed around, allowing for dynamic behavior.
- **Readability**: Code can be more concise and expressive.

### Benefits of Generators

- **Memory Efficiency**: Generators yield items one at a time, which is memory efficient for large datasets.
- **Lazy Evaluation**: Values are computed on-the-fly and only when needed.

### Functional Programming Best Practices

- **Immutability**: Avoid changing variables or data structures.
- **Pure Functions**: Functions should not have side effects.
- **Function Composition**: Build complex operations by composing simpler functions.

### Regular Expressions Tips

- **Testing Patterns**: Use tools or online regex testers to validate your patterns.
- **Escaping Special Characters**: Use backslashes to escape characters that have special meaning in regex.
- **Reading Regex**: Break down complex patterns into smaller parts to understand them.

### Best Practices in Pygame Development

- **Game Loop Structure**: Keep the game loop organized with event handling, game logic updates, and rendering steps.
- **Frame Rate Independence**: Use `pygame.time.Clock` to control the frame rate and ensure consistent gameplay speed across different machines.
- **Resource Management**: Load images and sounds once during initialization to avoid performance issues.
- **Modularity**: Organize code into functions and classes for better readability and maintainability.

### Tips for Pygame Programming

- **Coordinate System**: Remember that the Y-axis increases downward.
- **Image Transparency**: Use images with transparent backgrounds (like PNGs) for sprites.
- **Collision Detection**: Use bounding boxes (rectangles) for simple collision detection.
- **Performance**: Limit the amount of computation in the game loop to maintain high frame rates.

---

By mastering these advanced concepts, you'll be able to write Python code that is more efficient, flexible, and powerful. Functions as arguments and lambda expressions enhance the way you manipulate data structures. Generators provide a memory-efficient way to handle large or infinite sequences. Functional programming paradigms like `map`, `filter`, and `reduce` enable you to process data in a clean and declarative manner. Regular expressions equip you with a powerful tool for text processing and pattern matching.

Furthermore, learning Pygame opens up the world of game development. You'll be able to create interactive applications, games, and simulations. The Sokoban game project and the encouragement to create your own game provide practical experience in applying programming concepts to real-world projects.

---
**Congratulations on completing the Advanced Course in Programming!**
<br><br> <!-- This adds extra space -->
---