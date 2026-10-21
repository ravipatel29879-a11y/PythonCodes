def find_factorial(number):
    result = 1
    for count in range(1, number + 1):
        result *= count
    return result

# Printing table headers with left-alignment
# :<10
# : mean format start
#  < mean left alignment
#  10 mean 10 spaces

print(f"{'Value':<10} | {'Result':<15}")
print("-" * 28)

# Displaying factorials for numbers 1 to 8
for count in range(1, 9):
    print(f"{count:<10} | {find_factorial(count):<15}")
