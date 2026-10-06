import random
import string

print("-----------------------------")
print("|     PASSWORD GENERATOR    |")
print("|       WELCOME BACK        |")
print("-----------------------------")

def check_password_strength():
    score = 0

    password = input("Enter password to check: ")

    if any(char.islower() for char in password):
        score += 15

    if any(char.isupper() for char in password):
        score += 20

    if any(char.isdigit() for char in password):
        score += 25

    if any(char in string.punctuation for char in password):
        score += 30

    if len(password) >= 10:
        score += 10

    print(f"\nScore: {score}/100")

    if score >= 80:
        print("Password strength: VERY STRONG")
    elif score >= 60:
        print("Password strength: STRONG")
    elif score >= 40:
        print("Password strength: MEDIUM")
    else:
        print("Password strength: WEAK")

def generate_password():
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
                if lowercase_include not in ["y", "n"]:
                    raise ValueError("Invalid choice")
                
                if uppercase_include not in ["y", "n"]:
                    raise ValueError("Invalid choice")

                if number_include not in ["y", "n"]:
                    raise ValueError("Invalid choice")

                if symbols_include not in ["y", "n"]:
                    raise ValueError("Invalid choice")
                
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

            print("Please, Enter numbers only and select at least one include.")

            user_input = input("How many characters do you want in your password? ")
            lowercase_include = input("Include lowercase letters? (y/n) ")
            uppercase_include = input("Include uppercase letters? (y/n) ")
            number_include = input("Include digits? (y/n) ")
            symbols_include = input("Include symbols? (y/n) ")

            lowercase_include = lowercase_include.lower()
            uppercase_include = uppercase_include.lower()
            number_include = number_include.lower()
            symbols_include = symbols_include.lower()


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


while True:
    print("""
                1. Generate password
                2. Check password strength
                3. Password history
                4. Exit

                """)

    user_input = input("Choose an option: ")

    if user_input in "1":
        generate_password()
    elif user_input in "2":
        check_password_strength()
    elif user_input in "4":
        exit()