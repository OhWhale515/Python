def add(*args):
    sum = 0
    # print(type(args))
    for n in args:
        sum += n
    return sum
  

# print(add(3, 5, 6, 2, 1, 7, 4, 3,))

def calculate(**kwargs):
    print(kwargs)

    print(kwargs["add"])


calculate(add=3, multiply=5)