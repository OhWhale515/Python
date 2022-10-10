try:
    value = int(input('Enter an integer: '))
    print('The inverse of', value, 'is', 1/value)
except ValueError:
    print('You did not provide a number, so I will not calculate the inverse')
except ZeroDivisionError:
    print('You provide 0 and division by 0 is not possible, sorry')
