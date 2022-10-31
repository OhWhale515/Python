def get_number():
    for i in range(1, 4):
        yield i

print(get_number())

generator = get_number()
print(next(generator))
print(next(generator))
print(next(generator))

print()

for x in get_number():
    print(x)
    
print()

numbers = list(get_number())
print(numbers)