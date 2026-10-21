number = int(input("Enter a non-negative integer: "))
result = 1

if number < 0:
    print("Factorial does not exist for negative numbers.")
else:
    for count in range(1, number + 1):
        result *= count
    print(f"{number}! = {result}")
