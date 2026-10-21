scores = (72, 88, 91, 64, 79)

print(f"Original Tuple: {scores}")
print(f"Indexing (First Element): {scores[0]}")
print(f"Slicing (Middle 3)      : {scores[1:4]}")
print(f"Length                  : {len(scores)}")

# Demonstrating Immutability (TypeError)
print("\nAttempting to modify tuple element:")
try:
    scores[0] = 85
except TypeError as error:
    print(f"  TypeError caught successfully: {error}")

# Modifying via List conversion
temporary_list = list(scores)
temporary_list[0] = 85
scores = tuple(temporary_list)
print(f"Tuple after modification via List conversion: {scores}")
