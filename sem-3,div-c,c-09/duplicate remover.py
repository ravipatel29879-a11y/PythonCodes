numbers1 = [15, 25, 35, 25, 45, 15, 55, 35, 65]
numbers2 = [35, 45, 75, 85]

print(f"List 1: {numbers1}")
print(f"List 2: {numbers2}")

# (a) Remove duplicates using set
unique_numbers = list(set(numbers1))
print(f"\n(a) Duplicates Removed (List 1): {unique_numbers}")

# (b) Elements in List 1 but not List 2
different_numbers = list(set(numbers1) - set(numbers2))
print(f"(b) In List 1 but not List 2   : {different_numbers}")

# (c) Count occurrences of each number in List 1
frequency = {number: numbers1.count(number) for number in set(numbers1)}
print("(c) Element Occurrences (List 1):")
for number, frequency_count in sorted(frequency.items()):
    print(f"    Element {number:2d} -> Appears {frequency_count} time(s)")
