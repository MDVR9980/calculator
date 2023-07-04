def calculator():
    print("Hello! Welcome to the calculator.")

    while True:
        print("Please select an operation:")
        print("1. Plural")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Departure")

        choice = input("Enter your choice (1-5):")

        if choice == '5':
            print("Thanks! Bye.")
            break

        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))

        if choice == '1':
            result = num1 + num2
            print("Answer:", result)
        elif choice == '2':
            result = num1 - num2
            print("Answer:", result)
        elif choice == '3':
            result = num1 * num2
            print("Answer:", result)
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print("Answer:", result)
            else:
                print("Error! Division by zero is not possible.")
        else:
            print("Invalid selection! Please enter an integer between 1 and 5.")

        print("-----------------------")

# Run the program
calculator()
