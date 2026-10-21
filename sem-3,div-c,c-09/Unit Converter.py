distance = float(input("Enter distance in kilometres: "))
meters = distance * 1000
centimeters = distance * 100000
miles = distance * 0.621371
feet_value = distance * 3280.84

print(f"Metres: {meters:.2f} m")
print(f"Centimetres: {centimeters:.2f} cm")
print(f"Miles: {miles:.4f} mi")
print(f"Feet: {feet_value:.2f} ft")
