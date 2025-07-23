#Topics:

#1.Data Structures: Lists, Tuples, Sets, Dictionaries
#2.String Manipulation
#3.List Comprehension
#4.Exception Handling (try, except, finally)
#5.File Handling (open, read, write)
#6.Modules & Packages (import, math, random, custom modules)
#7.Lambda Functions, map(), filter(), reduce()
#8.Built-in Functions & help() documentation

#Practice Projects:
#Password Generator

# 1. Data Structures in Python
#A. Lists
#Ordered, changeable (mutable), allows duplicates

fruits = ["apple", "banana", "cherry"]
print(fruits[0])         # apple
fruits.append("orange")  # add to end
fruits.remove("banana")  # remove item
print(fruits)

#B. Tuples
#Ordered, unchangeable (immutable), allows duplicates
coordinates = (10, 20)
print(coordinates[0])    # 10
# coordinates[0] = 100   # ❌ Error: Tuples are immutable

#C. Sets
#Unordered, no duplicates
colors = {"red", "green", "blue", "green"}
print(colors)            # {'red', 'green', 'blue'}
colors.add("yellow")
colors.remove("blue")

#D. Dictionaries
#Key-value pairs, unordered (Python 3.6+ maintains insertion order)
student = {
    "name": "Alice",
    "age": 22,
    "grade": "A"
}
print(student["name"])         # Alice
student["grade"] = "A+"
student["email"] = "alice@example.com"
print(student["grade"])

#Try creating a dictionary that holds info about your favorite movie:
movie = {
    "title": "Inception",
    "year": 2010,
    "genre": "Sci-Fi"
}
print(movie)


#2. String Manipulation in Python
#Common String Operations

text = " Hello, Python World! "

print(text.lower())         # lowercase
print(text.upper())         # uppercase
print(text.strip())         # remove leading/trailing spaces
print(text.replace("Python", "Coding"))  # replace word
print(text.split())         # split into list
print("Length:", len(text)) # length

#Accessing Characters
word = "Python"
print(word[0])      # P
print(word[-1])     # n
print(word[1:4])    # yth

#String Formatting
name = "Chetan"
age = 25

# Using f-string
print(f"My name is {name} and I am {age} years old.")

# Useful String Methods
print("python".capitalize())  # Python
print("123".isdigit())        # True
print("abc".isalpha())        # True
print("abc123".isalnum())     # True
print("Hello".startswith("H"))  # True
print("world".endswith("d"))    # True

# 3. List Comprehension in Python

# Example 1: Square numbers from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Example 2: Get even numbers from 1 to 10
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

#4. Exception Handling in Python
#Exception handling lets you catch and manage errors in your program instead of letting it crash.

try:
    file = open("test.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution completed.")

#exception handling error 
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")


#5. File Handling in Python

#Modes:
#"r" – Read (default)
#"w" – Write (overwrites)
#"a" – Append
#"x" – Create (fails if file exists)

#Example 1: Write to a file
with open("demo.txt", "w") as file:
    file.write("Hello, this is a test file.")
#Example 2: Read from a file
with open("demo.txt", "r") as file:
    content = file.read()
    print("File Content:", content)

# 6. Modules & Packages

#Python has built-in modules (like math, random) and you can also create your own.
import math
print(math.sqrt(16))         # 4.0
print(math.factorial(5))     # 120

#pick up random number
import random
print(random.randint(1, 10))     # Random number between 1 and 10
print(random.choice(["A", "B", "C"]))  # Random choice from list

#7. Lambda, map(), filter(), reduce()
#Lambda (Anonymous Function)
square = lambda x: x ** 2
print(square(5))  # 25

# map() – Apply a function to all items
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)  # [1, 4, 9, 16]

#filter() – Filter items using a condition
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6]

#reduce() – Reduce a list to a single value
from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # 24

#8. Built-in Functions & help()
#Some Useful Built-in Functions
print(len("Python"))        # 6
print(type(123))            # <class 'int'>
print(max([1, 3, 2]))       # 3
print(min([1, 3, 2]))       # 1
print(sum([10, 20, 30]))    # 60

#Using help() to Get Info
help(str)           # Shows help on string methods
help(math.sqrt)     # Shows help on math.sqrt

