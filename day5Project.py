import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


letters_count = int(input("how many letters do you want?"))
numbers_count = int(input("how many numbers do you want?"))
symbols_count = int(input("how many symbols do you want?"))

password = ""

for char in range(1, letters_count):
    password+= random.choice(letters)

for char in range(1, numbers_count):
    password+= random.choice(numbers)

for char in range(1, symbols_count):
    password += random.choice(symbols)

print(f"this is my password: {password}")
