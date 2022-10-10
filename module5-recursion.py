def get_factorial(number):
    factorial = 1
    for x in range(1, number + 1):
        factorial *= x
    return factorial
print(get_factorial(6))

print()

def get_factorial_recursive(number):
    return number * get_factorial_recursive(number - 1)
    
