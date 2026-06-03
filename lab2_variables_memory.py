name = "Alice"
age = 25
price = 19.99
active = True

print("String:", name)
print("Integer:", age)
print("Float:", price)
print("Boolean:", active)

# Python contstants are written in CAPITALS by convention.
# Python does not prevent modification.

PI = 3.14159

print("Constant PI:", PI)

PI = 3.14

print("Modified PI:", PI)
print("Python does not generate an error when constants are modified")

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

# Global Scope

message = "I am Global"

def test_scope():

    # Local Scope

    local_message = "I am Local"

    print(message)
    print(local_message)

test_scope()

print(message)

# print(local_message)
# This would cause an error because local_message
# only exists inside the function.

# Python does not have var, let, const.
# Scope is demonstrated using global and local variables.