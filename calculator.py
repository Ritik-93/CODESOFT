def calculator():
    print("Welcome to the Simple Calculator!")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input! Please enter numeric values.")

    operation = input("Choose an operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is undefined.")
            return
        result = num1 / num2
    else:
        print("Invalid operation. Please choose from +, -, *, /.")
        return

    print(f"The result of {num1} {operation} {num2} is: {result}")

calculator()