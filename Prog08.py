# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

odd_num = 0

for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    if num % 2 != 0:
        odd_num += 1

print(f"No. of odd numbers: {odd_num}")