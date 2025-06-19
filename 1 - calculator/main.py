import os

while True:
    num1 = input("Enter first number: ")
    try:
        int(num1)
    except:
        print("Please enter a proper number.")
        exit()

    operator = input("Enter operator (+, -, *, /, ^): ")

    if operator not in ["+", "-", "*", "/", "^"]:
        print("Please enter one of the following operators: (+, -, *, /, ^)")
        os.system("cls")

    num2 = input("Enter second number: ")
    try:
        int(num2)
    except:
        print("Please enter a proper number.")
        exit()
    
    else:

        if operator == "+":
            sums = int(num1) + int(num2)
            print("Result is: " + str(sums))
        elif operator == "-":
            sums = int(num1) - int(num2)
            print("result is: " + str(sums))
        elif operator == "*":
            sums = int(num1) * int(num2)
            print("result is: " + str(sums))
        elif operator == "/":
            sums = int(num1) / int(num2)
            print("result is: " + str(sums))
        elif operator == "^":
            sums = int(num1) ** int(num2)
            print("result is: " + str(sums))

        exit()