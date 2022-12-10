def show_truth():
    global mysterious_var
    mysterious_var = 'New Surprise!'
    print(mysterious_var)
    
mysterious_var = 'Surprise!'
print(mysterious_var)
show_truth()
print(mysterious_var)

print()

def show_truth():
    global mysterious_var
    mysterious_var = ('New Surprise!')
    print(mysterious_var)
    
mysterious_var = ['Surprise!']
print(mysterious_var)
show_truth()
print(mysterious_var)
