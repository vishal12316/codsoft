import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
n_letters = int(input("enter no.of characters in password?\n"))
n_numbers = int(input("enter no.of numbers in password?\n"))
n_symbols = int(input("enter no.of symbols in password?\n"))

password_list = []

for _ in range(n_letters):
    password_list.append(random.choice(letters))

for _ in range(n_numbers):
    password_list.append(random.choice(numbers))

for _ in range(n_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ''.join(password_list)
print(password)
