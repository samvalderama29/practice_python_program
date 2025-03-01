# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

biggernum = f"{num1} is Bigger" if num1 > num2 else f"{num2} is Bigger"

print(biggernum)