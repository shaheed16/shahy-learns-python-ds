#1.input() – Takes user input from the keyboard:
num = int(input("Enter any number: "))
print(num)
print(type(num))

if num % 2 == 0:
 print("Even")
else:
 print("Odd")
#2.if…elif…else – Checks multiple conditions in sequence:
percentage = int(input("Enter student's percentage: "))

if percentage >= 90:
 print("A")
elif percentage >= 80:
 print("B")
elif percentage >= 70:
 print("C")
elif percentage >= 50:
 print("D")
elif percentage >= 35:
 print("E")
else:
 print("Fail")

#3.for loop – Repeats code for each item in a range:
# Run loop based on user input
num = int(input("Enter a number to repeat: "))
for i in range(num):
 print(i)

# With step value
for i in range(1, num + 1, 2):
 print(i)

# Reverse loop
for i in range(num, 0, -1):
 print(i)
#4.while loop – Repeats code while a condition is true:
num = int(input("Enter a number: "))
while num <= 10:
 print(num)
 num += 1

#5.break & continue – Control the flow inside loops:
#break – Exit the loop when a condition is met:

num = int(input("Enter a number to search: "))
for i in range(10):
    if i == num:
        print("Number found")
        break
else:
        print("Number not found")



# continue – Skip current iteration and move to the next:
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1

