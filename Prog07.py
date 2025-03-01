# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

all_num = 0

for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    all_num += num

print(f"Sum of all numbers: {all_num}")