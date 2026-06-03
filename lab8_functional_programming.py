# Functional Programming Examples

nums = [1, 2, 3, 4, 5]

# Map

doubled = list(map(lambda x: x * 2, nums))
print("Map:", doubled)

# Filter

evens = list(filter(lambda x: x % 2 == 0, nums))
print("Filter:", evens)

# Reduce

from functools import reduce

total = reduce(lambda x, y: x + y, nums)
print("Reduce:", total)

# Pure Function

def multiply(a, b):
    return a * b

print("Pure Function:", multiply(5, 3))

# Higher-Order Function

def add(a, b):
    return a + b

def calculate(function, x, y):
    return function(x, y)

print("Higher-Order Function:", calculate(add, 5, 3))