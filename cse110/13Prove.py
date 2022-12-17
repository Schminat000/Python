# Gives the calculator the mph to use.
wind_speed = 0
while wind_speed != 60:
    if wind_speed <= 60:
        wind_speed += 5

# Calculates the wind chill based on given temperature and mph. T = Temp ; V = Wind mph
def wind_chill_calculator(T,V):
    return float(35.74 + (0.6215*(T)) - (35.75 * (V**0.16)) + (0.4275 * (T) * (V**0.16)))

# Switches C to F if necessary before the calculations. T = Temp ; C = Celsius
def celsius_to_f(T,C):
    if C.upper() == "C":
        return T * (9/5) + 32
    elif C.upper() == "F":
        return T

# Gets the user's inputs.
user_temperature = float(input("What is the temperature? "))
user_fahrenheit_or_celsius = input("Fahrenheit or Celsius (F/C)? ")

# Stores them into variables
temperature = celsius_to_f(user_temperature,user_fahrenheit_or_celsius)
wind_chill = wind_chill_calculator(celsius_to_f(user_temperature,user_fahrenheit_or_celsius),wind_speed)

# Prints the loop until all mphs are printed.
for wind_mph in range(5,65,5):
    print(f"At temperature {temperature}F, and the wind speed is {wind_mph}mph, the windchill is: {wind_chill:.2f}F")

# wind_chill = 35.74 + (0.6215*(user_temperature)) - (35.75 * (5**0.16)) + (0.4275 * (user_temperature) * (5**0.16))
# print(f"At temperature {user_temperature}F, and the wind speed is 5 mph, the windchill is: {wind_chill:.2f}F")

# wind_chill = 35.74 + (0.6215*(user_temperature)) - (35.75 * (10**0.16)) + (0.4275 * (user_temperature) * (10**0.16))
# print(f"At temperature {user_temperature}F, and the wind speed is 10 mph, the windchill is: {wind_chill:.2f}F")

# wind_chill = 35.74 + (0.6215*(user_temperature)) - (35.75 * (15**0.16)) + (0.4275 * (user_temperature) * (15**0.16))
# print(f"At temperature {user_temperature}F, and the wind speed is 15 mph, the windchill is: {wind_chill:.2f}F")

# wind_chill = 35.74 + (0.6215*(user_temperature)) - (35.75 * (20**0.16)) + (0.4275 * (user_temperature) * (20**0.16))
# print(f"At temperature {user_temperature}F, and the wind speed is 20 mph, the windchill is: {wind_chill:.2f}F")

# wind_chill = 35.74 + (0.6215*(user_temperature)) - (35.75 * (25**0.16)) + (0.4275 * (user_temperature) * (25**0.16))
# print(f"At temperature {user_temperature}F, and the wind speed is 25 mph, the windchill is: {wind_chill:.2f}F")

# wind_chill = 35.74 + (0.6215*(user_temperature)) - (35.75 * (30**0.16)) + (0.4275 * (user_temperature) * (30**0.16))
# print(f"At temperature {user_temperature}F, and the wind speed is 30 mph, the windchill is: {wind_chill:.2f}F")

# wind_chill = 35.74 + (0.6215*(user_temperature)) - (35.75 * (35**0.16)) + (0.4275 * (user_temperature) * (35**0.16))
# print(f"At temperature {user_temperature}F, and the wind speed is 35 mph, the windchill is: {wind_chill:.2f}F")

# wind_chill = 35.74 + (0.6215*(user_temperature)) - (35.75 * (40**0.16)) + (0.4275 * (user_temperature) * (40**0.16))
# print(f"At temperature {user_temperature}F, and the wind speed is 40 mph, the windchill is: {wind_chill:.2f}F")

# wind_chill = 35.74 + (0.6215*(user_temperature)) - (35.75 * (45**0.16)) + (0.4275 * (user_temperature) * (45**0.16))
# print(f"At temperature {user_temperature}F, and the wind speed is 45 mph, the windchill is: {wind_chill:.2f}F")

# wind_chill = 35.74 + (0.6215*(user_temperature)) - (35.75 * (50**0.16)) + (0.4275 * (user_temperature) * (50**0.16))
# print(f"At temperature {user_temperature}F, and the wind speed is 50 mph, the windchill is: {wind_chill:.2f}F")

# wind_chill = 35.74 + (0.6215*(user_temperature)) - (35.75 * (55**0.16)) + (0.4275 * (user_temperature) * (55**0.16))
# print(f"At temperature {user_temperature}F, and the wind speed is 55 mph, the windchill is: {wind_chill:.2f}F")

# wind_chill = 35.74 + (0.6215*(user_temperature)) - (35.75 * (60**0.16)) + (0.4275 * (user_temperature) * (60**0.16))
# print(f"At temperature {user_temperature}F, and the wind speed is 60 mph, the windchill is: {wind_chill:.2f}F")

# What is the temperature? 8
# Fahrenheit or Celsius (F/C)? F
# At temperature 8.0F, and wind speed 5 mph, the windchill is: -1.11F
# At temperature 8.0F, and wind speed 10 mph, the windchill is: -6.02F
# At temperature 8.0F, and wind speed 15 mph, the windchill is: -9.15F
# At temperature 8.0F, and wind speed 20 mph, the windchill is: -11.50F
# At temperature 8.0F, and wind speed 25 mph, the windchill is: -13.40F
# At temperature 8.0F, and wind speed 30 mph, the windchill is: -15.00F
# At temperature 8.0F, and wind speed 35 mph, the windchill is: -16.39F
# At temperature 8.0F, and wind speed 40 mph, the windchill is: -17.62F
# At temperature 8.0F, and wind speed 45 mph, the windchill is: -18.73F
# At temperature 8.0F, and wind speed 50 mph, the windchill is: -19.74F
# At temperature 8.0F, and wind speed 55 mph, the windchill is: -20.67F
# At temperature 8.0F, and wind speed 60 mph, the windchill is: -21.53F

# What is the temperature? -10
# Fahrenheit or Celsius (F/C)? C
# At temperature 14.0F, and wind speed 5 mph, the windchill is: 5.93F
# At temperature 14.0F, and wind speed 10 mph, the windchill is: 1.42F
# At temperature 14.0F, and wind speed 15 mph, the windchill is: -1.47F
# At temperature 14.0F, and wind speed 20 mph, the windchill is: -3.63F
# At temperature 14.0F, and wind speed 25 mph, the windchill is: -5.38F
# At temperature 14.0F, and wind speed 30 mph, the windchill is: -6.85F
# At temperature 14.0F, and wind speed 35 mph, the windchill is: -8.13F
# At temperature 14.0F, and wind speed 40 mph, the windchill is: -9.27F
# At temperature 14.0F, and wind speed 45 mph, the windchill is: -10.29F
# At temperature 14.0F, and wind speed 50 mph, the windchill is: -11.22F
# At temperature 14.0F, and wind speed 55 mph, the windchill is: -12.07F
# At temperature 14.0F, and wind speed 60 mph, the windchill is: -12.87F