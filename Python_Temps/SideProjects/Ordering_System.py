print('Welcome to Marios Pizza!!')
size = input('What size pizza do you want? S, M, L ')
add_pepperoni = input("Do you want pepperoni? (y/n): ")
extra_cheese = input("Do you want extra cheese? (y/n): ")
bill = 0

if size == 'S':
    bill += 15
    print('A small pizza is $15')
    if add_pepperoni == 'y':
        bill+= 2
    print('Add pepperoni is $2 extra')
    if extra_cheese == 'y':
        bill+= 1
        print('Add extra cheese is $1 extra')
   
elif size == 'M':
    bill += 20
    print('A medium pizza is $20')
    if add_pepperoni == 'y':
        bill+= 3
        print('Add pepperoni is $3 extra')
    if extra_cheese == 'y':
        bill+= 1
        print('Add extra cheese is $1 extra')    
     
else:
    bill += 25
    print('A large pizza is $25')
    if add_pepperoni == 'y':
        bill+= 3
        print('Add pepperoni is $3 extra')
    if extra_cheese == 'y':
        bill+= 1
        print('Add extra cheese is $1 extra')

print(f'Your final bill is: ${bill}')                
