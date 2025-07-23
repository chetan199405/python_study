#stage 2 project on password generator

import random #Used for random selection — in this case, to pick random characters for the password.
import string #It provides convenient character sets: letters, digits, punctuation, etc.
 
def generate_password(length=12): #It accepts a parameter length, defaulting to 12, which means the password will have 12 characters unless specified otherwise.
    characters = string.ascii_letters + string.digits + string.punctuation #Creates a pool of characters from which the password will be generated.(string.ascii_letters → all uppercase and lowercase letters (A–Z, a–z), string.digits → '0' to '9', string.punctuation → symbols like !@#$%^&*()_+ etc.)
    password = ''.join(random.choice(characters) for _ in range(length)) #Generates the actual password.(random.choice(characters) → picks one random character from the pool.,This is done in a loop (for _ in range(length)) which runs length times (e.g., 12 times).,''.join(...) → joins all selected characters into a single string.)
    return password #Returns the final generated password from the function.

print("Generated Password:", generate_password()) #Calls the function and prints the password.
