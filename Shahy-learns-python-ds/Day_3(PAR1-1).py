#  1. Lists in Python – Lists are ordered, mutable collections that can store mixed data types (integers, strings, etc.).
# Creating a List:

lst = [10, 20, 30, 40, 50]
lst2 = [46, "Shaheed", "Shaik", 500085]
print(type(lst)) # Output: <class 'list'>

# Indexing in Lists
# Each element has a unique index starting from 0.

lst = [46, "Shaheed", "Shaik", 500085]
print(lst[0])  # 46
print(lst[2])  # Shaik

#  Accessing invalid index:

print(lst[5]) # IndexError: list index out of range

#  Negative Indexing – Access elements from the end:

print(lst[-1]) # 500085

# 🔹 Slicing Lists – Extract a portion of the list:

nums = [10, 20, 30, 40, 50, 60, 70, 80]

print(nums[0:3])   # [10, 20, 30]
print(nums[4:-3])  # [50]
print(nums[4:])   # [50, 60, 70, 80]
print(nums[:4])   # [10, 20, 30, 40]
print(nums[-3:])   # [60, 70, 80]
print(nums[1:6:2])  # [20, 40, 60] → (with step value of 2)



#  Useful List Operations
#  len() – Returns the number of items in the list:

lst = [10, 20, 30, 40, 50]
print(len(lst)) # Output: 5

#  Membership Test using in:

lst = [10, 20, 30, 40, 50]
if 24 in lst:
 print("Item exists")
else:
 print("Item does not exist")
# Output: Item does not exist

