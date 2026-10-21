group1 = {num for num in range(1, 21) if num % 2 == 0}   # Even numbers 1-20
group2 = {num for num in range(1, 21) if num % 4 == 0}   # Multiples of 4 up to 20

print(f"Set 1 (Evens 1-20)        : {group1}")
print(f"Set 2 (Multiples of 4)     : {group2}")
print("-" * 50)
print(f"Union (Set1 | Set2)        : {group1 | group2}")
print(f"Intersection (Set1 & Set2) : {group1 & group2}")
print(f"Difference (Set1 - Set2)   : {group1 - group2}")
print(f"Difference (Set2 - Set1)   : {group2 - group1}")
print(f"Symmetric Difference       : {group1 ^ group2}")
