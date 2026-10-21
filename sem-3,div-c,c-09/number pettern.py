lines = 6

print("Ascending Pattern:")
for row in range(1, lines + 1):
    for num in range(1, row + 1):
        print(num, end=" ")
    print()

print("\nDescending Pattern:")
for row in range(lines, 0, -1):
    for num in range(1, row + 1):
        print(num, end=" ")
    print()
