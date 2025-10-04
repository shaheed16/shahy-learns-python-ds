myset = {10, 20, 30, 40, 50, 50, 10, 70}
print(myset)
# Output: {50, 20, 70, 40, 10, 30}

# Removing Duplicates from a List Using Set:

lst = [10, 20, 30, 40, 50, 50, 10, 70]
myset = set(lst)
print(myset)  # Set with unique values

lst = list(myset)
print(lst)    # Converted back to list
# Output: [70, 40, 10, 50, 20, 30]

# Important Note: Sets do not support indexing or item assignment.

set1 = {1, "Shahy", 12.06}
print(set1[2])
# Output: TypeError: 'set' object is not subscriptable

''' Where Sets Are Used in Computer Science: ✅ Databases – Set operations in SQL ✅ Algorithms – Searching, graph theory ✅ Programming – Python set methods for fast lookups
 For a good refresher on set theory concepts: 📎 Basic Set Theory Concepts'''

# Set Operations in Python:

a = {1, 2, 3, 4}
b = {2, 3, 4}

print(a.union(b))               # {1, 2, 3, 4}
print(a.intersection(b))        # {2, 3, 4}
print(a.difference(b))          # {1}
print(b.difference(a))          # set()
print(a.symmetric_difference(b))# {1}
print(a.issubset(b))            # False
print(a.issuperset(b))          # True
print(a.isdisjoint(b))          # False

# Common Set Methods to Know:
add(), remove(), discard(), pop(), clear(), copy()
union(), intersection(), difference(), symmetric_difference()
update(), intersection_update(), difference_update(), symmetric_difference_update()
issubset(), issuperset(), isdisjoint()

