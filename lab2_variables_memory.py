name = "Alice"
age = 25
price = 19.99
active = True

print("String:", name)
print("Integer:", age)
print("Float:", price)
print("Boolean:", active)

# Constant

PI = 3.14159
print("Constant PI:", PI)

# Python allows constants to be changed, but it is not recommended
PI = 3.14
print("Modified PI:", PI)

#value type example

x = 5
y = x
y = 10

print("x =", x)
print("y =", y)

# Reference type example

person1 = {"age": 25}
person2 = person1

person2["age"] = 30

print("person1 =", person1)
print("person2 =", person2)
           