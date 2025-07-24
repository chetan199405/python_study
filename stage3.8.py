#Advanced Modules

#datetime, os, sys, collections

#Practice Projects:

#To-Do App using OOP
#JSON-based Contact Book
#API Weather App
#SQLite-based Expense Tracker


#Advanced Python Modules

#1️.datetime – Working with Dates & Times
from datetime import datetime, timedelta

now = datetime.now()
print(now)  # current timestamp

# Formatting
print(now.strftime("%d-%m-%Y %H:%M:%S"))

# Adding days
future = now + timedelta(days=5)
print("5 days later:", future)

#2.os – Operating System Interaction

#import os

print(os.getcwd())       # Current working directory
os.mkdir("test_folder")  # Make a new folder
os.rename("test.txt", "renamed.txt")  # Rename files
print(os.listdir())      # List files in current directory

#3️.sys – System-Specific Parameters
import sys

print(sys.argv)          # Command-line arguments
print(sys.version)       # Python version
sys.exit()               # Exit script early

#4️.collections – Enhanced Data Structures
from collections import Counter, defaultdict, namedtuple

# Counter
c = Counter("aabbccddaa")
print(c)  # Counts frequency of characters

# defaultdict
d = defaultdict(int)
d["apple"] += 1
print(d)

# namedtuple
Point = namedtuple("Point", "x y")
p = Point(10, 20)
print(p.x, p.y)

#5.To-Do App using OOP

class ToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

todo = ToDo()
todo.add_task("Learn Python OOP")
todo.add_task("Build To-Do App")
todo.show_tasks()

#6. JSON-Based Contact Book

import json

contacts = {
    "Chetan": {"phone": "9999999999", "email": "chetan@example.com"}
}

with open("contacts.json", "w") as f:
    json.dump(contacts, f, indent=2)

# Read it back
with open("contacts.json", "r") as f:
    data = json.load(f)
    print(data["Chetan"]["email"])
