limit = int(input("Enter limit: "))

total_numbers = 0
total_squares = 0
total_cubes = 0

for num in range(1, limit + 1):
    total_numbers += num
    total_squares += num**2
    total_cubes += num**3

print(f"Sum of first {limit} natural numbers: {total_numbers}")
print(f"Sum of squares of first {limit} natural numbers: {total_squares}")
print(f"Sum of cubes of first {limit} natural numbers: {total_cubes}")
