num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

operation = input("Choose any operation; +,-,/,*: ")

if operation == "+" :
    output = num1 + num2
if operation == "-" :
    output = num1 - num2
if operation == "*" :
    output = num1 * num2
if operation == "/" :
    output = num1 / num2

print(output)

print("The End")