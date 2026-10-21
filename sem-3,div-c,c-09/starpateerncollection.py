lines = 6

print("(a) Right-angled Triangle:")
for row in range(1, lines + 1):
    for col in range(row):
        print("*", end="")
    print()

print("\n(b) Inverted Triangle:")
for row in range(lines, 0, -1):
    for col in range(row):
        print("*", end="")
    print()

print("\n(c) Diamond Pattern:")
# Upper part
for row in range(1, lines + 1):
    for col in range(lines - row):
        print(" ", end="")
    for star in range(2 * row - 1):
        print("*", end="")
    print()

# Lower part
for row in range(lines - 1, 0, -1):
    for col in range(lines - row):
        print(" ", end="")
    for star in range(2 * row - 1):
        print("*", end="")
    print()
