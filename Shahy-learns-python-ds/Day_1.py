print("shahy")
# Also discussed error: NameError: name 'print' is not defined
print("print(hello)") # Incorrect – should be in quotes

# 2.Variables – Store values like numbers or strings:

i = j = k = 10
i, j, k = 10, 20, 30
print(i, j, k)

string = "Hello World"
print(string, type(string))

boolean = True
print(boolean, type(boolean))

float_num = 10.5
print(float_num, type(float_num))

# 🔄 Swapping Two Variables:

a, b = 10, 20
a, b = b, a
print(a, b)

# 3. Concatenation – Combine strings using '+':

num1 = 10
str1 = '10'
# print("10" + 10) → Error: Cannot add str and int directly
print(num1 + int(str1))    # 20
print(str(num1) + str1)    # '1010'

# 4. String Interpolation – Embed variables in strings:

month = "June"
date = 23

print("Using + : " + month + " " + str(date) + " 2000")
print("Using %%: %s %s 2000" % (month, date))
print("Using .format(): {} {} 2000".format(month, date))
print("Named .format(): {month} {date} 2000".format(month=month, date=date))
print(f"Using f-string: {month} {date} 2000")

# 5. If-Else Statements – Conditional logic:


x = y = 10
z = 20

if x == y or y == z:
 print("True")
else:
 print("False")

# Even or Odd
num = 12
if num % 2 == 0:
 print("Even")
else:
 print("Odd")

