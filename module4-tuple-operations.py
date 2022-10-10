user_data = ('John', 'American', 1964)
print(len(user_data))

print

user_data = ('John', 'American', 1964)
if 'American' in user_data:
    print('This person comes from the US!')
    
print()

user_data = ('John', 'American', 1964)
for element in user_data:
    print(element)
    
print()

user_data = ('John', 'American', 1964) + ('teacher', 'male')
print(user_data)

print()

numbers = (0, 1) * 10
print(numbers)

print()

male_name = ['Adam', 'Jerry', 'Mark']
berlin_temps = [13.0, 17.5, 12.0]
user_data = ('John', 'American', 1964)
first = 5
second = 7
first, second = second, first