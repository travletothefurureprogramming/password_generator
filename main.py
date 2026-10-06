import random
import string

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

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


random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))

result = []

for x in range(part1):
    result.append(s1[x])
    result.append(s2[x])

for x in range(part2):
    result.append(s1[x])
    result.append(s2[x])

random.shuffle(result)

password = "".join(result)
print("Strong password: ", password)