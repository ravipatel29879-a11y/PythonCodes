# 1.10 BMI Calculator

body_weight = float(input("Enter your weight in kg: "))
body_height = float(input("Enter your height in metres: "))

body_mass_index = body_weight / (body_height ** 2)

if body_mass_index < 18.5:
    result = "Underweight"
elif 18.5 <= body_mass_index <= 24.9:
    result = "Normal"
elif 25 <= body_mass_index <= 29.9:
    result = "Overweight"
else:
    result = "Obese"

print(f"BMI Value: {body_mass_index:.2f}")
print(f"Result: {result}")
