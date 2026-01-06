"""
LOGICAL BUILDING ONE VIDEO COMPLETE CODE
Author: Sambhav
Purpose: Teach logic, not just syntax
"""

# ==================================================
# 1️⃣ INPUT → PROCESS → OUTPUT
# Problem: Add two numbers
# ==================================================

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = a + b
print("Sum:", result)

'''
'''
# ==================================================
# 2️⃣ DECISION MAKING (IF–ELSE)
# Problem: Even or Odd
# ==================================================

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

'''
'''
# ==================================================
# 3️⃣ COMPARISON LOGIC
# Problem: Largest of 3 numbers
# ==================================================

x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

if x >= y and x >= z:
    print("Largest:", x)
elif y >= x and y >= z:
    print("Largest:", y)
else:
    print("Largest:", z)


'''
'''
# ==================================================
# 4️⃣ LOOP THINKING
# Problem: Print numbers from 1 to 10
# ==================================================

print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)



# ==================================================
# 5️⃣ LOOP + PROCESS
# Problem: Sum of first N numbers
# ==================================================

n = int(input("Enter value of n: "))
total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum of first", n, "numbers is:", total)


# ==================================================
# 6️⃣ DRY RUN EXAMPLE (MENTAL EXECUTION)
# ==================================================

sum_value = 0
for i in range(1, 4):
    sum_value = sum_value + i

print("Dry run result:", sum_value)


# ==================================================
# 7️⃣ ASSIGNMENT – LEVEL 2 SOLUTIONS
# ==================================================

# Print numbers from 10 to 1
print("Numbers from 10 to 1:")
for i in range(10, 0, -1):
    print(i)

# Count even numbers between 1 and 20
count = 0
for i in range(1, 21):
    if i % 2 == 0:
        count += 1

print("Even numbers count:", count)

# Factorial of a number
num = int(input("Enter number for factorial: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial:", fact)

# ==================================================
# 8️⃣ PATTERN LOGIC
# ==================================================

rows = 4
for i in range(1, rows + 1):
    print("*" * i)


# ==================================================
# END MESSAGE
# ==================================================

print("\nLogic is built by thinking + practice, not memorizing code.")
