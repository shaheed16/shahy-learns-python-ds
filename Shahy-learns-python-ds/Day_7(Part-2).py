# even or odd

num = int(input(""))
if num % 2 == 0:
    print("even")
else:
    print("odd")

# year must be leap year and div by 5 and 3

year = int(input("Enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
    if year % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")
else:
    print("Not a leap year")

# max of 2 numbers

num1 = int(input(""))
num2 = int(input(""))
if num1 > num2:
    print("num1 larger one than num2")
elif num1 < num2:
    print("num1 smaller than num2")
else:
    print("both are equal")

#  positive or negative 

num =int(input(""))
if num > 0:
    print("numer is positive")
elif num < 0:
    print("numer is negtive")
else:
    print("number equal to zero")

# grade checker 

marks = int(input(""))
if marks >= 90:
    print("grade:A")
elif marks >= 80:
    print("grade:B")
elif marks >= 70:
    print("grade:C")
else:
    print("fail")


