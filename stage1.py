#Topics:

#1.Python Installation (Anaconda/VS Code/IDLE)--#
#2.Variables, Data Types (int, str, float, bool)--#
#3.Input/Output (input(), print())--#
#4.Operators (Arithmetic, Comparison, Logical)--#
#5.Conditional Statements (if, elif, else)--#
#6.Loops (for, while, break, continue)
#7.Functions (def, return values, arguments)--#

#--Practice Ideas:--#
#--Calculator--#

#Variables & Data Types
name = "Chetan"       # str
age = 25              # int
height = 5.8          # float
is_student = True     # bool

# Print values
print(name, age, height, is_student)

#Input and Output
name = input("Enter your name: ")
print("Hello", name)

#Operators
#Arithmetic:
a = 10
b = 3
print(a + b, a - b, a * b, a / b, a % b, a ** b)

#Comparison:
print(a > b, a == b, a != b)

#Logical:
x = True
y = False
print(x and y, x or y, not x)

#Conditional Statements
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote.")
elif age > 0:
    print("You are underage.")
else:
    print("Invalid age.")

# Loops
#For Loop
for i in range(1):
    print(i)

#while loop
n = 0
while n < 1:
    print(n)
    n += 1

#Functions
def greet(name):
    return "Hello " + name

print(greet("Chetan"))    


#What is Typecasting in Python?
#Typecasting in Python means converting one data type into another.
#For example: converting a string to an integer, a float to an integer, etc.

#Common Types of Typecasting

#1. Implicit Typecasting (Automatic)
#Python automatically converts data types during operations when safe.

x = 5       # int
y = 2.0     # float
z = x + y   # z becomes float (7.0)

print(z)    # Output: 7.0
print(type(z))  # Output: <class 'float'>

#Python implicitly converts int to float to avoid data loss.

#List to Set:
nums = [1, 2, 2, 3]
unique = set(nums)
print(unique)  # Output: {1, 2, 3}

#Float to Int (loss of decimal):
x = 7.8
y = int(x)
print(y)  # Output: 7

#String to Int:
num_str = "100"
num_int = int(num_str)
print(num_int + 50)   # Output: 150

#Int to String:
age = 25
text = "I am " + str(age) + " years old."
print(text)  # Output: I am 25 years old.