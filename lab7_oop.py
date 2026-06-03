# Class and Object

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

dog = Dog("Buddy", 3)
print(dog.bark())

# Inheritance

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def drive(self):
        return f"{self.brand} is driving"

car = Car("Toyota")
print(car.drive())

# Encapsulation

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age

student = Student("John", 20)

print(student.get_name())
print(student.get_age())

#Polymorphism

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Animal Sound"

class Cat(Animal):
    def sound(self):
        return f"{self.name} says Meow"
    
class Bird(Animal):
    def sound(self):
        return f"{self.name} says Tweet"
    
cat = Cat("Kitty")
bird = Bird("Tweety")

print(cat.sound())
print(bird.sound())

# Bank Account Example

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    
account = BankAccount(100)

account.deposit(50)

print("Balance:", account.get_balance())