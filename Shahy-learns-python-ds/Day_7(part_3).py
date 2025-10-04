# 1. Print numbers from 1 to 10 (for loop)
for i in range(1, 11):
    print(i)


# Topic: Basic for loop.

# 2. Print even and odd numbers separately (for loop + condition)
for i in range(1, 21):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")


# Topic: Conditional check inside a loop.

# 3. Sum of first N natural numbers (while loop)
n = int(input("Enter N: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print("Sum =", total)


🧠 Topic: while loop.

# 4. Factorial of a number (for loop)
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial =", fact)


# Topic: Loop with multiplication.

# Reverse a number (while loop)
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed number:", rev)


# Topic: Looping through digits.

# 6. Use of break and continue
for i in range(1, 10):
    if i == 5:
        continue   # skip 5
    if i == 8:
        break      # stop at 8
    print(i)


# Topic: Loop control statements.

# 7. Multiplication table (for loop)
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")


# Topic: Loop with formatted output.

# 8. Pattern printing (nested loop)
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()


# Topic: Nested loops.


# 9. Fibonacci series (for loop)
n = int(input("Enter number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# Topic: Loop-based series generation.

# 10. Check if a number is prime (for-else loop)
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(num, "is not prime")
            break
    else:
        print(num, "is prime")
else:
    print("Not a prime number")


# Topic: Using for-else in loops.