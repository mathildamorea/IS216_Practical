# If, Else If, Else

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")

# For Loop

print("\nFor Loop")

for i in range(1, 6):
    print(i)

# While Loop

print("\nWhile Loop")

i = 1

while i <= 5:
    print(i)
    i += 1

# Task 1 - Positive, Negative or Zero

number = 7

if number > 0:
    print("\nPositive")
elif number < 0:
    print("\nNegative")
else:
    print("\nZero")

# Task 2 - Multipication Table using nested loops

print("\nMultiplication Table")

for number in range(5, 6):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Task 3 - Prime Number Check

prime_number = 7
is_prime = True

for i in range(2, prime_number):
    if prime_number % i == 0:
        is_prime = False

if is_prime:
    print("\nPrime Number")
else:
    print("\nNot Prime")

# Task 4 - Menu System

print("\nMenu")

choice = 2

if choice == 1:
    print("Add Record")
elif choice == 2:
    print("View Record")
elif choice == 3:
    print("Delete Record")
else:
    print("Invalid Choice")