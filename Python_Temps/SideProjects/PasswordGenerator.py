import string 
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()*+,-./")

def generate_password():
    password_length = int(input("How long you want the password to be? "))

    random.shuffle(characters)

    password = []
    
    for x in range(0, password_length):
        password.append(random.choice(characters))

    random.shuffle(password)


    password ="".join(password)

    print(password)

option = input("Do you wanna generate a new  password? (Yes/No)")

if option == "Yes":
    generate_password()
elif option == "No":
    print("Ya done")
    quit()
else:
    print("Invalid input man, its either Yes or No...Dang ")
    quit()