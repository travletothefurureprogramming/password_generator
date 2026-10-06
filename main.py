import random
import string

print("-----------------------------")
print("|     PASSWORD GENERATOR    |")
print("|       WELCOME BACK        |")
print("-----------------------------")

user_input = input("How many characters do you want in your password? ")
lowercase_include = input("Include lowercase letters? (y/n) ")
uppercase_include = input("Include uppercase letters? (y/n) ")
number_include = input("Include digits? (y/n) ")
symbols_include = input("Include symbols? (y/n) ")

lowercase_include = lowercase_include.lower()
uppercase_include = uppercase_include.lower()
number_include = number_include.lower()
symbols_include = symbols_include.lower()

while True:
    try:
        characters_number = int(user_input)

        if characters_number < 8:
            print("Your number should be at least 8 characters.")

            user_input = input("Please, Enter your number again: ")

        else:
            if lowercase_include == "y":
                lowercase_include = True
            if uppercase_include == "y":
                uppercase_include = True
            if number_include == "y":
                number_include = True
            if symbols_include == "y":
                symbols_include = True
            if lowercase_include == "n":
                lowercase_include = False
            if uppercase_include == "n":
                uppercase_include = False
            if number_include == "n":
                number_include = False
            if symbols_include == "n":
                symbols_include = False
            
            break

    except:

        print("Please, Enter numbers only.")

        user_input = input("How many characters do you want in your password? ")


lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

password = []

if lowercase_include:
    password.append(random.choice(lowercase))

if uppercase_include:
    password.append(random.choice(uppercase))

if number_include:
    password.append(random.choice(digits))

if symbols_include:
    password.append(random.choice(punctuation))

all_characters = ""

if lowercase_include:
    all_characters += lowercase

if uppercase_include:
    all_characters += uppercase

if number_include:
    all_characters += digits

if symbols_include:
    all_characters += punctuation

for _ in range(characters_number - len(password)):
    password.append(random.choice(all_characters))

random.shuffle(password)

password = "".join(password)

print("Strong password:", password)