previous_reading = float(input("Enter previous meter reading: "))
current_reading = float(input("Enter current meter reading: "))
consumed_units = current_reading - previous_reading
fixed_charge = 120.0
electric_rate = 6.00
total_bill = (consumed_units * electric_rate) + fixed_charge

print(f"Units Consumed: {consumed_units:.2f}")
print(f"Total Electric Bill: ₹{total_bill:.2f}")