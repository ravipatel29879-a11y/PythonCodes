square_numbers = [num**2 for num in range(1, 16)]

even_numbers = [num for num in range(1, 41) if num % 2 == 0]

text = "Java list comprehension helps create simple and readable programs"
big_words = [item for item in text.split() if len(item) > 4]

odd_cubes = [num**3 for num in range(1, 13) if num % 2 != 0]

print(f"(a) Squares (1-15)     : {square_numbers}")
print(f"(b) Evens (1-40)       : {even_numbers}")
print(f"(c) Words > 4 chars    : {big_words}")
print(f"(d) Odd Cubes (1-12)   : {odd_cubes}")
