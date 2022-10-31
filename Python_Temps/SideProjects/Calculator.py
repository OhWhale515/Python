def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))

def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))

def div(a, b): 
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))

def mod(a, b):
    answer = a % b
    print(str(a) + " % " + str(b) + " = " + str(answer))

def divmod(a, b):
    answer = a // b
    print(str(a) + " // " + str(b) + " = " + str(answer))

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input('input your choice: ')

    if choice == 'A' or choice == "a":
        print("Addition")
        a = int(input("input first number:"))
        b = int(input("input second number:"))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("input first number:"))
        b = int(input("input second number:"))
        sub(a, b)
    elif choice == "C" or choice == "c":
        print("Multiplication")
        a = int(input("input first number:"))
        b = int(input("input second number:"))
        mul(a, b)
    elif choice == "D" or choice == "d":
        print("Division")
        a = int(input("input first number:"))
        b = int(input("input second number:"))
        div(a, b)
    elif choice == "E" or choice == "e":
        print("Peace")
        quit()

