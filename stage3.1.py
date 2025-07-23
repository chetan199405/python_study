#Object-Oriented Programming (OOP)

#Classes & Objects
#__init__ method
#self keyword
#Inheritance
#Polymorphism
#Encapsulation

#1. Object-Oriented Programming (OOP) in Python

#OOP helps you organize code by modeling real-world things as objects with attributes (data) and methods (functions).
#Concept	 Meaning
#Class	     Blueprint for creating objects
#Object	     Instance of a class
#Attributes	 Variables inside a class (e.g. self.name)
#Methods	 Functions inside a class
#self	     Refers to the current object instance
#init()	     Constructor method to initialize data when object is created

#Basic Example
class Person: #class Person: → Defines a class named Person
    def __init__(self, name, age): #__init__(self, name, age) → Automatically called when a new object is created
        self.name = name       #self.name = name → Sets the name attribute
        self.age = age

    def greet(self): #greet(self) → A method that prints the greeting
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create objects
p1 = Person("Chetan", 25)
p2 = Person("Amit", 30)

# Call methods
p1.greet()
p2.greet()


#2. Inheritance & Polymorphism in Python
#Inheritance lets a class (child) reuse the code from another class (parent).
#Polymorphism lets you use the same method name in different classes with different behavior.

#Inheritance Example
# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I am an animal")

# Derived class
class Dog(Animal): #class Dog(Animal) → Inherits from Animal
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

# Create objects
d = Dog("Buddy")
c = Cat("Whiskers")

d.speak()   # Buddy says Woof! (speak() is overridden in each subclass)
c.speak()   # Whiskers says Meow!
#This is polymorphism — same method name, different behavior based on object type


#3. Encapsulation in Python

#Encapsulation is the concept of hiding internal data and providing controlled access using methods. It helps in:
#Protecting data from accidental changes
#Keeping the internal implementation hidden

#How It Works in Python:
#Python doesn't have strict access modifiers like Java or C++, but it uses naming conventions:

#Notation	      Meaning
#public	          Normal attribute (self.name) – accessible everywhere
#_protected	      Single underscore (self._name) – should not be accessed directly
#__private	      Double underscore (self.__name) – name-mangled, harder to access

#Example of Encapsulation:

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance #__balance is private – it can’t be accessed directly.
# Usage
acc = BankAccount("Chetan", 1000)
acc.deposit(500)
acc.withdraw(300)

print("Balance:", acc.get_balance())  # Balance: 1200


#example with complete 

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.brand} {self.model} is starting...")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping...")

    def info(self):
        print(f"Car Info: {self.year} {self.brand} {self.model}")

# Create objects
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Tesla", "Model 3", 2022)

# Call methods
car1.start()
car1.info()
car1.stop()

print("---")

car2.start()
car2.info()
car2.stop()
