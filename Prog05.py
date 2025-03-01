# Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point

num1 = float(input("First number: "))
num2 = float(input("Second number: "))

quotientnum = round(num1 / num2, 2)

print(quotientnum)