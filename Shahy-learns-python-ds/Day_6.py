 #Tuple in Python
# A tuple is an ordered, immutable collection of elements. It is declared using parentheses ().


# Example 1: Creating a tuple
mytuple = (101, "Alice", 28, "Delhi")
print(mytuple)
print("Name:", mytuple[1])
# Tuple is Immutable

# mytuple[0] = 102  # ❌ This will raise TypeError
#  Tuple with Different Data Types

t = ("Python", 3.8, True, [1, 2])
print(t)
#  Tuple Unpacking

student = ("John", "CSE", 3)
name, branch, year = student
print(name)
print(branch)
print(year)
#  Tuple Methods

numbers = (1, 2, 3, 2, 4, 2)
print("Count of 2:", numbers.count(2))
print("Index of 4:", numbers.index(4))
#  Tuple in a Loop

colors = ("red", "green", "blue")
for color in colors:
    print(color)
#Dictionary in Python
# A dictionary is an unordered collection of key-value pairs. It is mutable and defined using curly braces {}.


# Example 1: Basic Dictionary
emp = {'eid': 100, 'ename': 'Scott', 'job': 'Manager', 'salary': 5000}
print(emp)
#  Accessing and Updating

print("Name:", emp['ename'])
emp['salary'] = 6000
print("Updated Salary:", emp['salary'])
# Adding and Deleting Items

emp['department'] = 'HR'       # Adding new key
del emp['job']                 # Deleting a key
print(emp)
#  Using Dictionary Methods

print("Keys:", emp.keys())
print("Values:", emp.values())
print("Items:", emp.items())
#  Looping through Dictionary

# Keys only
for key in emp:
    print(key, "=>", emp[key])

# Keys and Values
for key, value in emp.items():
    print(f"{key}: {value}")

# Values only
for value in emp.values():
    print(value)
# Dictionary with Nested Data

student = {
    'name': 'Ravi',
    'age': 21,
    'marks': {
        'math': 90,
        'science': 85
    }
}
print(student['marks']['math'])  # Accessing nested value
# Dictionary from List of Tuples

pairs = [("name", "Sara"), ("age", 25)]
d = dict(pairs)
print(d)
