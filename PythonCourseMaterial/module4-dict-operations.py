grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'
print (grades)

print()

grades['Anne'] = 'A'
print(grades)

print()

grades.update({'John':'A'})
print(grades)

print()

len(grades)

if 'John' in grades:
    print('John got:', grades['John'])
    
print()

del grades ['John']
print(grades)

print()

grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'

for el in grades:
    print(el)
    
print()

for el in grades.keys():
    print(el)
    
print()

for el in grades.values():
    print(el)
    
print()

for person, grade in grades.items():
    print(person, 'got', grade)