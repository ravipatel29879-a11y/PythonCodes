# 3.7 Modular Calculator

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"

def exponent(x, y):
    return x ** y

def calculator():
    print(" --- Simple Calculator ---")
    print("1. Addition | 2. Subtraction | 3. Multiplication | 4. Division | 5. Power | 6. Exit")
    
    option = input("Choose an option (1-6): ")
    
    if option == '6':
        print("Calculator Closed.")
        return
        
    first_value = float(input("Enter first value: "))
    second_value = float(input("Enter second value: "))
    
    if option == '1':
        print(f"Answer: {addition(first_value, second_value)}")
    elif option == '2':
        print(f"Answer: {subtraction(first_value, second_value)}")
    elif option == '3':
        print(f"Answer: {multiplication(first_value, second_value)}")
    elif option == '4':
        print(f"Answer: {division(first_value, second_value)}")
    elif option == '5':
        print(f"Answer: {exponent(first_value, second_value)}")
    else:
        print("Wrong Option!")

# Example execution
calculator()
