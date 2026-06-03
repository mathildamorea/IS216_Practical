# Lab 8 - Framework & Functional Programming

# ------------------------------------------------
# 1. Hello World Framework Example (Django)
#-------------------------------------------------

# Example Django Hello World

# from django.http import HttpResponse
#
# def hello(request):
#       return HttpResponse("Hello, Django")

print("Hello, Django")


# ------------------------------------------------
# 2. Functional Programming Examples
# ------------------------------------------------

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

def add(a, b):
    return a + b

print("Pure Function Multiply:", multiply(5, 3))
print("Pure Function Add:", add(5, 3))

# Higher-Order Function

def calculate(function, x, y):
    return function(x, y)

print("Higher-Order Function:", calculate(add, 5, 3))

# Imperative Style

squares = []

for num in nums:
    squares.append(num * num)

print("Imperative:", squares)

# Functional Style

functional_squares = list(map(lambda num: num * num, nums))

print("Functional:", functional_squares)