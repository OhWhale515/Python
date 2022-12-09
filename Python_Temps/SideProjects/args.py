def add(*args):
    sum = 0
    # print(type(args))
    for n in args:
        sum += n
    return sum
  

print(add(3, 5, 6))