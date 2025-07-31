# Iterating Through Lists
# You can loop through a list in two common ways:

lst = [10, 20, 30, 40, 50]

# Method 1: Using index
for i in range(len(lst)):
 print(lst[i], end=" ")

# Method 2: Using direct elements
for i in lst:
 print(i, end=" ")

#  Both give: 10 20 30 40 50

# List Manipulation & Built-in Methods
# append() – Adds a value at the end:

lst = [1, 2, 3]
lst.append(4)
print(lst) # [1, 2, 3, 4]

#  insert() – Inserts value at a specific index:

lst = [1, 2, 3]
lst.insert(2, 5)
print(lst) # [1, 2, 5, 3]

# extend() – Adds another iterable to the list:

lst1 = [10, 20, 30]
lst2 = [40, 50, 60]
lst1.extend(lst2)
print(lst1) # [10, 20, 30, 40, 50, 60]

# Using '+' operator
lst3 = lst1 + lst2
print(lst3) # [10, 20, 30, 40, 50, 60, 40, 50, 60]

# Removing Elements from a List
# pop() – Removes the last item:

lst = [1, 2, 3]
lst.pop()
print(lst) # [1, 2]

# remove() – Removes a specific value:

lst = [1, 2, 3, 4, 5]
lst.remove(3)
print(lst) # [1, 2, 4, 5]

# del – Deletes by index or entire list:

lst = [1, 2, 3]
del lst[1]
print(lst) # [1, 3]

del lst
print(lst) # NameError: name 'lst' is not defined

# clear() – Empties the list:

lst = [1, 2, 3, 4, 5]
lst.clear()
print(lst) # []

# Updating Lists (Mutability)
# Lists are mutable, meaning their contents can be changed:

lst = [1, 2, 3, 4, 5]
lst[1] = 23
lst[4] = 6
print(lst) # [1, 23, 3, 4, 6]