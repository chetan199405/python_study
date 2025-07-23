#stage 1 project on Calculator

def calculator():
    print("Simple Calculator")
    print("Choose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    # Take input from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
4
    if choice == '1':
        print("Result:", num1 + num2)
    elif choice == '2':
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Result:", num1 * num2)
    elif choice == '4':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero.")
    else:
        print("Invalid input")

# Run the calculator
calculator()
