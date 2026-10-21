# (a) ValueError
try:
    number = int("xyz")
except ValueError as error:
    print(f"(a) ValueError caught: {error}")

# (b) ZeroDivisionError
try:
    result = 25 / 0
except ZeroDivisionError as error:
    print(f"(b) ZeroDivisionError caught: {error}")

# (c) FileNotFoundError
try:
    with open("unknown_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as error:
    print(f"(c) FileNotFoundError caught: {error}")

# (d) IndexError
try:
    numbers = [15, 25, 35, 45]
    value = numbers[8]
except IndexError as error:
    print(f"(d) IndexError caught: {error}")