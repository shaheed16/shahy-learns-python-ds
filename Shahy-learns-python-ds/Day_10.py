class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def bark(self):
        print("Dog barks: Woof! Woof!")


dog = Dog()
dog.speak()   
dog.bark()    





class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal created")

class Dog(Animal):
    def __init__(self, name, breed):
       
        super().__init__(name)
        self.breed = breed
        print("Dog created")

dog1 = Dog("Buddy", "Labrador")
print(dog1.name)
print(dog1.breed)






class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")

dog = Dog()
dog.speak()




class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        super().speak()   
        print("Dog says: Woof!")

dog = Dog()
dog.speak()





class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

calc = Calculator()
print(calc.add(10, 5))
print(calc.subtract(10, 5))
print(calc.multiply(10, 5))
print(calc.divide(10, 5))




class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle is starting...")

    def stop(self):
        print(f"{self.brand} vehicle has stopped.")

class Car(Vehicle):
    def __init__(self, brand, model):
        
        super().__init__(brand)
        self.model = model

   
    def start(self):
        super().start()  
        print(f"{self.brand} {self.model} engine is running smoothly!")

    
    def honk(self):
        print(f"{self.brand} {self.model} says: Beep! Beep!")


car1 = Car("Toyota", "Corolla")
car1.start()
car1.honk()
car1.stop()


