import random
import string

print("-----------------------------")
print("|     PASSWORD GENERATOR    |")
print("|       WELCOME BACK        |")
print("-----------------------------")

user_input = input("How many characters do you want in your password? ")

while True:
    try:
        characters_number = int(user_input)

        if characters_number < 8:
            print("Your number should be at least 8 characters.")

            user_input = input("Please, Enter your number again: ")

        else:

            break

    except:

        print("Please, Enter numbers only.")

        user_input = input("How many characters do you want in your password? ")


lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

password = [
    random.choice(lowercase),
    random.choice(uppercase),
    random.choice(digits),
    random.choice(punctuation)
]

all_characters = lowercase + uppercase + digits + punctuation

for _ in range(characters_number - 4):
    password.append(random.choice(all_characters))

random.shuffle(password)

password = "".join(password)
print("Strong password: ", password)