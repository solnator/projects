print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter choice(1/2/3/4): ")
if choice in ("1", "2", "3", "4"):
    num1 = eval(input("Enter the first number: "))
    num2 = eval(input("Enter the second number: "))

    if choice == "1":
        result = num1 + num2
    elif choice == "2":
        result = num1 - num2
    elif choice == "3":
        result = num1 * num2
    elif choice == "4":
        if num2 == 0:
            print("Error! Division by zero.")
        else:
            result = num1 / num2
    print(result)
else:
    print("Invalid input")
