DEFAULT_TEMP = 8  # Personalisation

class Environment:
    def __init__(self, starting_temp=DEFAULT_TEMP):
        self.__temperature = starting_temp

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, new_value):
        if 18 <= new_value <= 32:
            self.__temperature = new_value
            print(f"[APPROVED] Temperature set to {new_value}°C")
        else:
            print(f"[DENIED] {new_value}°C out of range (18-32°C)")

environment = Environment()
print(f"Initial Temperature: {environment.temperature}°C\n")

# 3 valid, 2 invalid
temperature_list = [25, 14, 30, 36, 21]

for temp_value in temperature_list:
    environment.temperature = temp_value

print(f"\nFinal Temperature: {environment.temperature}°C")