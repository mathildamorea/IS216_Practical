# Function Example

def add(a, b):
    return a + b

result = add(5, 3)

print("Addition Result:", result)

# Factorial using Recursion

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))

# Reverse a String

def reverse_text(text):
    return text[::-1]

print("Reversed:", reverse_text("hello"))

# Palindrome Check

def is_palindrome(word):
    return word == word[::-1]

print("Palindrome:", is_palindrome("madam"))

# Linear Search

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [1, 2, 3, 4, 5]

print("Linear Search:", linear_search(numbers, 3))

# Bubble Sort

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

print("Bubble Sort:", bubble_sort([5, 3, 8, 1, 2]))

# Binary Search

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_numbers = [1, 2, 3, 4, 5]

print("Binary Search:", binary_search(sorted_numbers, 4))

# Fibonacci Sequence

def fibonacci(n):
    sequence = []
    a = 0
    b = 1

    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
print("Fibonacci Sequence:", fibonacci(10))
