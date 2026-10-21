number = int(input("Enter a 3-digit number: "))
first_digit = number // 100
second_digit = (number // 10) % 10
third_digit = number % 10
total_digits = first_digit + second_digit + third_digit
product_digits = first_digit * second_digit * third_digit

print(f"Hundreds Digit: {first_digit}")
print(f"Tens Digit: {second_digit}")
print(f"Units Digit: {third_digit}")
print(f"Sum of Digits: {total_digits}")
print(f"Product of Digits: {product_digits}")
