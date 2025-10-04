"""A function is a block of reusable code that performs a specific task.
Functions help make programs more modular, readable, and reusable. """

# Example 1: Defining and Calling a Function
def greet():
    print("shahy")

# Calling the function
greet()

# Example 2: Function with Parameters
def greet(name):
    print("Hello,", name)

greet("shahy")
greet("shaheed")

# Example 3: Function with Return Value
def add(a, b):
    return a + b

result = add(100, 200)
print("Sum =", result)

# Example 4: Function with Default Parameter
def greet(name="shaheed"):
    print("Hello,", name)

greet("shahy")
greet()   # Uses default value

# Example 5: Function with Multiple Return Values
def calc(a, b):
    return a+b, a-b, a*b, a/b

add, sub, mul, div = calc(20, 5)
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)

# Example 6: Function with Variable Arguments (args)
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3))
print(total(5, 10, 15, 20))

# Example 7: Function with Keyword Arguments (kwargs)
def student_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

student_info(name="John", age=21, branch="CSE")

# Example 8: Lambda (Anonymous Function)
square = lambda x: x*x
print("Square of 5:", square(5))

add = lambda a, b: a+b
print("Sum:", add(10, 15))

# Example 9: Function Inside a Function (Nested Function)
def outer():
    print("Outer function")

    def inner():
        print("Inner function")
    inner()

outer()

# Example 10: Recursive Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial of 5:", factorial(5))
