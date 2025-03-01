# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

for zero_num in range(101):
    if zero_num % 10 != 0:
        print(zero_num)