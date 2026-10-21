# 1.21 Armstrong Number Finder

# Part (a): Check single number
value = int(input("Enter a value: "))
digit_count = len(str(value))
temporary = value
power_total = 0

while temporary > 0:
    current_digit = temporary % 10
    power_total += current_digit ** digit_count
    temporary //= 10

if value == power_total:
    print(f"{value} is an Armstrong number.")
else:
    print(f"{value} is NOT an Armstrong number.")

# Part (b): Armstrong numbers between 1 and 999
print("\nArmstrong numbers between 1 and 999:")

for number in range(1, 1000):
    count_digits = len(str(number))
    temp_number = number
    total_sum = 0

    while temp_number > 0:
        digit_value = temp_number % 10
        total_sum += digit_value ** count_digits
        temp_number //= 10

    if number == total_sum:
        print(number, end=" ")

print()
