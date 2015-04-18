# variadic arguments
def sum(*arg, **kwargs):
    print(arg)
    print(kwargs)

print(sum(1, 2, 3, 4, 5, 6, coef=-1))

# Позиционни аргументи и keyword аргументи
def something(arg=1):
    print(arg)

something()
something(2)
something(arg=3)
