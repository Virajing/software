import webbrowser

def power_calculator():
    print("Power Calculator")
    while True:
        try:
            base = float(input("Enter the base number: "))
            exponent = float(input("Enter the exponent: "))
            result = base ** exponent
            print(f"{base} raised to the power of {exponent} is {result}")

            another_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if another_calculation != 'yes':
                break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    print("Exiting Power Calculator...")

def main():
    while True:
        print("1. a")
        print("2. b")
        print("3. c")
        print("4. d")
        print("5. Exit")

        while True:  # Keep asking for input until a valid number is entered
            try:
                basic = int(input("Choose an option and give its number value: "))
                if basic not in [1, 2, 3, 4, 5]:
                    print("Invalid input. Please enter a number between 1 and 5.")
                    continue
                break  # Exit the loop if input is valid
            except ValueError:
                print("Invalid input. Please enter a number.")

        if basic == 1:
            while True:
                print("1. hack")
                print("2. Code")
                print("3. Back")

                while True:
                    try:
                        insideA = int(input("Choose an option and give its number value: "))
                        if insideA not in [1, 2, 3]:
                            print("Invalid input. Please enter 1, 2, or 3.")
                            continue
                        break  # Exit the loop if input is valid
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                if insideA == 1:
                    print("hacking")
                    ip_add = input("Enter an IP address: ")
                    print(f"Hacking {ip_add}")
                    for minute in range(1, 11):
                        print(f"Dependencies pending for {minute} minute{'s' if minute > 1 else ''}.")
                    print("\033[91mAlert: System Failure. Try Again\033[0m")
                elif insideA == 2:
                    print("Code")
                    print("1. python")
                    print("2. java")
                    print("3. c++")
                    print("4. c#")
                    print("5. javascript")
                    print("6. html")
                    print("7. css")
                    print("8. sql")
                    print("9. Back")

                    while True:
                        try:
                            code_lang = int(input("Choose an option and give its number value: "))
                            if code_lang not in range(1, 10):
                                print("Invalid input. Please enter a number between 1 and 9.")
                                continue
                            break  # Exit the loop if input is valid
                        except ValueError:
                            print("Invalid input. Please enter a number.")

                    if code_lang == 9:
                        continue  # Go back to the previous menu
                    else:
                        print(f"Code language: {code_lang}")
                        code = input("Enter a code: ")
                        print(f"{code} is incorrect. Syntax error")
                elif insideA == 3:
                    break  # Go back to the previous menu (basic menu)

        elif basic == 2:
            while True:
                print("1. excel")
                print("2. word")
                print("3. Back")

                while True:
                    try:
                        insideB = int(input("Choose an option and give its number value: "))
                        if insideB not in [1, 2, 3]:
                            print("Invalid input. Please enter 1, 2, or 3.")
                            continue
                        break  # Exit the loop if input is valid
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                if insideB == 1:
                    print("Excel selected.")
                    # Add functionality for Excel if needed
                elif insideB == 2:
                    print("Word selected.")
                    # Add functionality for Word if needed
                elif insideB == 3:
                    break  # Go back to the previous menu (basic menu)

        elif basic == 3:
            while True:
                print("1. calculator")
                print("2. power calculator")
                print("3. Back")

                while True:
                    try:
                        insideC = int(input("Choose an option and give its number value: "))
                        if insideC not in [1, 2, 3]:
                            print("Invalid input. Please enter 1, 2, or 3.")
                            continue
                        break  # Exit the loop if input is valid
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                if insideC == 1:
                    print("Calculator selected.")
                    while True:
                        try:
                            num1 = float(input("Enter first number: "))
                            op = input("Enter operator (+, -, *, /): ")
                            num2 = float(input("Enter second number: "))
                            break  # Exit the loop if input is valid
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                    if op == "+":
                        print(num1 + num2)
                    elif op == "-":
                        print(num1 - num2)
                    elif op == "*":
                        print(num1 * num2)
                    elif op == "/":
                        if num2 == 0:
                            print("Cannot divide by zero.")
                        else:
                            print(num1 / num2)
                    else:
                        print("Invalid operator.")
                elif insideC == 2:
                    power_calculator()
                elif insideC == 3:
                    break  # Go back to the previous menu (basic menu)

        elif basic == 4:
            while True:
                print("1. google")
                print("2. youtube")
                print("3. google docx")
                print("4. Back")

                while True:
                    try:
                        insideD = int(input("Choose an option and give its number value: "))
                        if insideD not in [1, 2, 3, 4]:
                            print("Invalid input. Please enter 1, 2, or 3.")
                            continue
                        break  # Exit the loop if input is valid
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                if insideD == 1:
                    print("Google selected.")
                    webbrowser.open_new_tab("https://www.google.com")
                elif insideD == 2:
                    print("YouTube selected.")
                    webbrowser.open_new_tab("https://www.youtube.com")
                elif insideD == 3:
                    print("Google Docx selected.")
                    webbrowser.open_new_tab("https://docs.google.com")
                elif insideD == 4:
                    break  # Go back to the previous menu (basic menu)

        elif basic == 5:
            print("Exiting...")
            break  # Exit the main loop

if __name__ == "__main__":
    main()
