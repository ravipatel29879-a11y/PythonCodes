# 1.19 Number Reversal & Palindrome
value = int(input("Enter a value: "))

original_value = value
reverse_value = 0

# Part (a): Reverse using while loop
temporary = abs(value)
while temporary > 0:
    number = temporary % 10
    reverse_value = (reverse_value * 10) + number
    temporary //= 10

if value < 0:
    reverse_value = -reverse_value

print(f"Reversed Value: {reverse_value}")

# Part (b): Check Palindrome
if original_value == reverse_value:
    print(f"{original_value} is a Palindrome.")
else:
    print(f"{original_value} is NOT a Palindrome.")


"""
# 1. Take input from the user
word = input("Enter a word: ")

# 2. Reverse the string using a simple loop
reverse_word = ""
for letter in word:
    reverse_word = letter + reverse_word  # Adds each letter to the front

# 3. Compare original and reversed text
if word == reverse_word:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
"""
