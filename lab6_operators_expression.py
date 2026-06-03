print("Arithmetic Operators")
print("Addition:", 5 + 3)
print("Subtraction:", 5 - 3)
print("Multiplication:", 5 * 3)
print("Division:", 15 / 3)
print("Modulus:", 15 % 4)

# Comparison Operators

print("\nComparison Operators")
print("Equal:", 5 == 5)
print("Not Equal:", 5 != 3)
print("Greater Than:", 5 > 3)
print("Less Than:", 3 < 5)

# Logical Operators

print("\nLogical Operators")
a = True
b = False

print("AND:", a and b)
print("OR:", a or b)
print("NOT:", not a)

# String Operations

print("\nString Operations")
name = "John"

str1 = "Hello" + " " + "World"
str2 = f"Hello {name}"

print(str1)
print(str2)

# Lab Task 1: Simple Calculator

print("\nSimple Calculator")
num1 = 10
num2 = 5

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

# Lab Task 2: Even or Odd using Modulus

print("\nEven or Odd")
number = 8

if number % 2 == 0:
    print("Even")

# Lab Task 3: Password Validation using Logical Operators

print("\nPassword Validation")
password = "Python123"

if len(password) >= 8 and any(char.isdigit()for char in password):
    print("Valid Password")
else:
    print("Invalid Password")