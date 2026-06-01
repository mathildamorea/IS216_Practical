# Primitive Data Types

num = 42
price = 3.14
name ="John"
active = True
x = None

print("Integer:", num)
print("Float:", price)
print("String:", name)
print("Boolean:", active)
print("Null:", x)

# List

fruits = ["apple", "banana", "cherry"]

print("\nFirst Fruit:", fruits[0])

fruits.append("date")

print("Updated List:", fruits)

# Dictionary

person = {
    "name": "John",
    "age": 30,
}

print("\nDictionary Example")
print("Name:", person["name"])

# Lab Task: List of 5 Numbers

numbers = [5, 8, 2, 10, 3]

print("\nMaximum:", max(numbers))
print("Minimum:", min(numbers))

# Lab Task: Book Dictionary

book = {
    "title": "Introduction to Programming",
    "author": "Rodney Naro",
    "year": 2026
}

print("\nBook Information")
print(book)

#Lab Task: List of 3 Books
books = [
    {"title": "Book One", "author": "Author One"},
    {"title": "Book Two", "author": "Author Two"},
    {"title": "Book Three", "author": "Author Three"}
]

print("\nBooks")
for item in books:
    print(item)

# Type Checking

print("\nData Types")
print(type(num))
print(type(price))
print(type(name))
print(type(active))
print(type(x))
print(type(fruits))
print(type(person))