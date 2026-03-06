import random
import string
symbols = ['_','@']
print("Welcome to the User Name Generator!")
nr_name=input("Enter your Name: ")
nr_name+=random.choice(string.ascii_letters)
nr_name+=random.choice(string.digits)
nr_name+=random.choice(symbols)

print(nr_name)
