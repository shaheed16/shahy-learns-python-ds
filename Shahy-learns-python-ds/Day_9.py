class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


person1 = Person("Alice", 25)
person1.greet()


class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(5, 3))


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"This car is a {self.brand} {self.model}.")

my_car = Car("Toyota", "Corolla")
my_car.info()


class Animal:
    def speak(self):
        print("Some generic sound")

class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")

dog = Dog()
dog.speak()



class Mother:
    def skills(self):
        print("Cooking")

class Father:
    def skills(self):
        print("Driving")

class Child(Mother, Father):
    pass

child = Child()
child.skills()  



class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())



class Shape:
    def area(self):
        print("Area not defined")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

s = Square(4)
print(s.area())


class Dog:
    species = "Canine"  

    def __init__(self, name):
        self.name = name  

dog1 = Dog("Buddy")
dog2 = Dog("Charlie")

print(dog1.name, dog1.species)
print(dog2.name, dog2.species)


class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if value >= 0 and value <= 100:
            self._marks = value
        else:
            print("Invalid marks")

s = Student("John", 85)
print(s.marks)
s.marks = 105  


class Engine:
    def start(self):
        print("Engine starting...")

class Car:
    def __init__(self):
        self.engine = Engine()  

    def start(self):
        self.engine.start()
        print("Car is ready to go!")

my_car = Car()
my_car.start()



class Dog:
  
    species = "Canine"
    
 
    def bark(self):
        print("Woof! Woof!")




my_dog = Dog()  
print(my_dog.species)  
my_dog.bark()         




class Dog:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def info(self):
        print(f"My dog's name is {self.name} and it is {self.age} years old.")

dog1 = Dog("Buddy", 3)
dog1.info()



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I am {self.name}!")

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

person1.greet()
person2.greet()





class Cat:
    def meow(self):
        print("Meow! Meow!")

my_cat = Cat()
my_cat.meow()




def __init__(self, title, author):
    self.title = title
    self.author = author

def info(self):
    print(f"'{self.title}' is written by {self.author}")

book1 = Book("1984", "George Orwell")
book1.info()




class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show(self):
        print(f"{self.name} has grade {self.grade}")

student1 = Student("Alice", "A")
student2 = Student("Bob", "B")

student1.show()
student2.show()



class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

my_laptop = Laptop("Dell", 800)
print(my_laptop.price)


my_laptop.price = 750
print(my_laptop.price)




class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, other_person):
        print(f"Hi {other_person.name}, I am {self.name}!")

p1 = Person("Alice")
p2 = Person("Bob")

p1.greet(p2)





class Car:
    def __init__(self, brand):
        self.brand = brand
        self.wheels = 4  

my_car = Car("Toyota")
print(f"{my_car.brand} has {my_car.wheels} wheels")




class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(10, 5))



class Light:
    def __init__(self):
        self.is_on = False

    def switch_on(self):
        self.is_on = True
        print("Light is ON")

    def switch_off(self):
        self.is_on = False
        print("Light is OFF")

light = Light()
light.switch_on()
light.switch_off()




class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def display(self):
        print(f"Count: {self.count}")

c = Counter()
c.increment()
c.increment()
c.display()





class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}")
        else:
            print("Insufficient balance")

account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print("Balance:", account.balance)


