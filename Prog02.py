# Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

equalnum = "Number is EQUAL" if num1 == num2 else "Number is NOT Equal"

print(equalnum)