#Decorators

#Functions as objects
#Nested functions
#Writing decorators (@decorator_name)

#1. Functions as Objects

#In Python, functions are first-class objects, meaning:
#You can assign them to variables
#Pass them as arguments
#Return them from other functions
#Store them in data structures

def greet():
    return "Hello"

say_hello = greet  # Assigning function to a variable
print(say_hello())  # Output: Hello

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(func):
    message = func("Hi There!")
    print(message)

speak(shout)   # Output: HI THERE!
speak(whisper) # Output: hi there!

# 2. Nested Functions
#A function defined inside another function is called a nested function or inner function.

def outer():
    print("Inside outer function")
    
    def inner():
        print("Inside inner function")
    
    inner()

outer()

#Why use nested functions?
#For encapsulation (helper function hidden from outside)
#Required for closures and decorators

#3. Writing Decorators (Manually and Using @)

#What is a Decorator?
#A decorator is a function that:
#Takes another function as an argument
#Extends or modifies its behavior
#Returns a new function

def decorator_function(original_function):
    def wrapper_function():
        print("Before the original function")
        original_function()
        print("After the original function")
    return wrapper_function

def say_hello():
    print("Hello!")

# Apply the decorator manually
decorated = decorator_function(say_hello)
decorated()

# 3.2 Decorator Using @ Syntax
#Python provides a cleaner syntax using the @decorator_name shortcut.
def decorator_function(original_function):
    def wrapper_function():
        print("Before the original function")
        original_function()
        print("After the original function")
    return wrapper_function

@decorator_function
def say_hello():
    print("Hello!")

say_hello()

#3.3 Decorators with Arguments
#Your decorator needs *args and **kwargs to handle any number of arguments.

def decorator_function(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@decorator_function
def greet(name):
    print(f"Hello, {name}!")

greet("Chetan")

#4. Practical Use Cases of Decorators
#Use Case	                          Example
#Logging	                          Log when a function is called
#Authorization	                      Check if user has permission
#Caching	                          Store results to reuse later
#Timing	                              Measure how long a function takes
#Validation	                          Automatically check inputs


#Example: Timer Decorator

import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Executed in {end - start:.2f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(2)
    print("Done!")

slow_function()

#Summary

#Concept	                              Purpose
#Function as object	                      Assign, pass, return functions
#Nested function	                      Help in decorators and closures
#Decorator (manual)	                      Wrap logic around a function
#Decorator (@)	                          Clean and readable syntax
#*args / **kwargs	                      Generalize decorators for any function