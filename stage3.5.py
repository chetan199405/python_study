#Working with JSON & APIs

#json module
#HTTP requests with requests
#Calling public APIs (weather, GitHub, etc.)


#1. Working with json Module

#The json module in Python lets you work with JSON data easily.
#JSON = JavaScript Object Notation
#A text format for storing data structures:
#{"name": "Alice","age": 25,"is_student": false}

#Common json Functions
#Function	    Description
#json.load()	Read JSON from a file
#json.loads()	Parse JSON string to Python
#json.dump()	Write JSON to a file
#json.dumps()	Convert Python to JSON string

#Example: Python ⇄ JSON
import json

# Python dictionary
data = {
    "name": "Chetan",
    "age": 28,
    "skills": ["Python", "SQL"]
}

# Convert Python → JSON string
json_string = json.dumps(data)
print(json_string)

# Convert JSON string → Python
python_data = json.loads(json_string)
print(python_data['skills'])

#2. HTTP Requests with requests Module
#To communicate with APIs over HTTP, Python uses the requests library.

#Basic HTTP Methods:
#Method	        Purpose
#GET	        Retrieve data
#POST	        Send data (form, JSON)
#PUT	        Update data
#DELETE	        Remove data

#Example: GET Request
import requests

response = requests.get("https://api.github.com")

# Check status
print(response.status_code)  # 200 means OK

# Get JSON response
data = response.json()
print(data)

#Example: POST Request
import requests

url = "https://httpbin.org/post"
payload = {"name": "Chetan", "role": "Developer"}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())

#3. Calling Public APIs

#Example: GitHub User Info API

import requests

username = "octocat"
url = f"https://api.github.com/users/chetan199405"

response = requests.get(url)
data = response.json()

print(f"Name: {data['name']}")
print(f"Public Repos: {data['public_repos']}")
print(f"Location: {data['location']}")


#Summary Table

#Concept	                      Usage
#json.loads() / dumps()	          For converting JSON ↔ Python
#requests.get() / .post()	      Call APIs
#.json()	                      Parse response JSON
#Status codes	                  200 = OK, 404 = Not Found, 500 = Server Error
#Use case	                      Weather, GitHub, Currency APIs, News APIs

