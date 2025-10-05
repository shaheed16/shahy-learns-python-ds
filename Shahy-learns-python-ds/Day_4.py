#  range() – Create lists within a specific range (just like in loops):

lst = list(range(10, 80, 10)) # range(start, stop, step)
print(lst) 
# Output: [10, 20, 30, 40, 50, 60, 70]

# count() – Counts how many times a value appears in the list:

lst = [1, 2, 3, 1, 5, 1, 7, 1, 9, 10]
print(lst.count(1)) 
# Output: 4 → '1' appears four times

# copy() – Creates a shallow copy of the list. The copied list is independent of the

lst = [1, 2, 3, 4, 5]
lst2 = lst.copy()

lst.append(6)
print(lst)  # [1, 2, 3, 4, 5, 6]
print(lst2) # [1, 2, 3, 4, 5]

# Changes to lst don’t affect lst2.

# reverse() – Reverses the list in place:

lst = [1, 2, 3, 4, 5]
lst.reverse()
print(lst) # [5, 4, 3, 2, 1]

# 🔹ort() – Sorts the list in ascending or descending order:

lst = [1, 4, 3, 7, 23, 79, 6765, 4567, 4545, 4, 5]

lst.sort() # Ascending
print(lst) 
# [1, 3, 4, 4, 5, 7, 23, 79, 4545, 4567, 6765]

lst.sort(reverse=True) # Descending
print(lst) 
# [6765, 4567, 4545, 79, 23, 7, 5, 4, 4, 3, 1]