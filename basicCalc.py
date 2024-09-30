# Function to add two numbers
def add(a, b):
    return a + b  # Return the sum of a and b

# Function to subtract two numbers
def subtract(a, b):
    return a - b  # Return the result of a minus b

# Function to multiply two numbers
def multiply(a, b):
    return a * b  # Return the product of a and b

# Function to divide two numbers, with a check to avoid division by zero
def divide(a, b):
    if b == 0:
        return "Error! Division by zero."  # Prevent crashing by returning an error message
    return a / b  # If b isn't zero, return the quotient

# Main function to run the calculator
def calculator():
    print("Simple Calculator")  # Intro message
    print("Select operation: 1.Add 2.Subtract 3.Multiply 4.Divide")  # Menu of options
    choice = input("Enter choice (1/2/3/4): ")  # User picks an operation by entering a number

    # Get two numbers from the user to perform the operation on
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Based on the choice, call the respective function and print the result
    if choice == '1':
        print(f"Result: {add(num1, num2)}")  # Call add() if user selects '1'
    elif choice == '2':
        print(f"Result: {subtract(num1, num2)}")  # Call subtract() if user selects '2'
    elif choice == '3':
        print(f"Result: {multiply(num1, num2)}")  # Call multiply() if user selects '3'
    elif choice == '4':
        print(f"Result: {divide(num1, num2)}")  # Call divide() if user selects '4'
    else:
        print("Invalid input!")  # Handle cases where the user inputs something other than 1-4

# Run the calculator program
calculator()
