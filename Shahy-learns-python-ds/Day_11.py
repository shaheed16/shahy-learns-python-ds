# =========================================
# 1. Private and Protected Attributes
# =========================================
print("=== Private and Protected Attributes ===")

class Student:
    def __init__(self, name, grade):
        self.__name = name      # private attribute
        self.__grade = grade
    
    def display(self):
        print(f"Name: {self.__name}, Grade: {self.__grade}")

s1 = Student("Alice", "A")
s1.display()
# print(s1.__name)  # ❌ Uncommenting this will cause an error

class Employee:
    def __init__(self, name, salary):
        self._salary = salary  # protected attribute
        self.name = name

    def show(self):
        print(f"{self.name}'s salary is {self._salary}")

class Manager(Employee):
    def update_salary(self, amount):
        self._salary += amount  # accessing protected member

m = Manager("John", 50000)
m.update_salary(5000)
m.show()

# =========================================
# 2. Getters & Setters
# =========================================
print("\n=== Getters & Setters ===")

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount!")

b1 = BankAccount(1000)
print(b1.get_balance())
b1.set_balance(1500)
print(b1.get_balance())
b1.set_balance(-200)

class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            print("Age must be positive")

p = Person(25)
print(p.age)
p.age = 30
print(p.age)
p.age = -5

# =========================================
# 3. Method Overriding
# =========================================
print("\n=== Method Overriding ===")

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

a = Animal()
a.speak()
d = Dog()
d.speak()

class Vehicle:
    def start(self):
        print("Starting vehicle...")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car is ready to drive")

c = Car()
c.start()

# =========================================
# 4. Polymorphism with Common Method Names
# =========================================
print("\n=== Polymorphism ===")

# Example 7 – Different classes
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

for animal in [Cat(), Dog()]:
    animal.sound()

# Example 8 – Polymorphism via inheritance
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Area = πr²")

class Rectangle(Shape):
    def area(self):
        print("Area = l × w")

for s in [Circle(), Rectangle()]:
    s.area()

# Example 9 – Method arguments
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))
print(calc.add(2, 3, 4))

# Example 10 – Duck typing
class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def let_it_fly(thing):
    thing.fly()

for obj in [Bird(), Airplane()]:
    let_it_fly(obj)
