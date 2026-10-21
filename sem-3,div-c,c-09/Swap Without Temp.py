x = int(input("Enter first number (x): "))
y = int(input("Enter second number (y): "))
print(f"\nOriginal Values: x = {x}, y = {y}")

# Method 1: Tuple Swap
x, y = y, x
print(f"After Tuple Swap: x = {x}, y = {y}")

# Method 2: Arithmetic Swap
x = x + y
y = x - y
x = x - y
print(f"After Arithmetic Swap (back to original): x = {x}, y = {y}")
