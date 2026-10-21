# 1.18 Fibonacci Series
total_terms = int(input("Enter total terms: "))

first, second = 1, 2
counter = 0

print("Fibonacci Sequence:")
while counter < total_terms:
    print(first, end=" ")
    first, second = second, first + second
    counter += 1

print()
