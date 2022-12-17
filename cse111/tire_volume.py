# Imports the math library and date time library.
from datetime import datetime
import math

# Saves the current date of the user's computer and saves
# it to a variable. Prints as well.
current_date = datetime.now()
print(f"{current_date:%Y-%m-%d}")

# This takes the user's inputs and stores them into variables.
width_tire = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_tire = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter_wheel = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# This is the math formula then formats and stores it to a variable
# with two decimal places.
volume_liters = (((math.pi * width_tire ** 2) * aspect_tire) * 
    ((width_tire * aspect_tire) + (2540 * diameter_wheel)) / 10000000000)
format_volume_liters = "{:.2f}".format(volume_liters)

# Prints the results.
print(f"The approximate volume is {volume_liters:.2f} liters.")

# Asks the user if they would like to buy the tire.
to_buy = input("Would you like to buy the tires with the specified "
    "dimensions? (Y/N): ")

# If they answer yes, the program will ask for the user's phone
# number.
if to_buy.upper() == "Y":
    phone_number = input("What is your phone number? (###-###-####): ")
    print("Thank you! We will be in touch soon.")
else:
    print("Okay! Comeback soon.")

# If the user said yes, it saves a string of all information to be used in
# the volume.txt file and storesit into a variable with the phone number.
if to_buy.upper() == "Y":
    txt_save = (f"{current_date:%Y-%m-%d}, {width_tire}, "
        f"{aspect_tire}, {diameter_wheel}, {format_volume_liters}, "
        f"{phone_number}\n")

# If the user says no, it saves a string of all information to be used in the
# volume.txt file and stores it into a variable without the phone number.
else:
    txt_save = (f"{current_date:%Y-%m-%d}, {width_tire}, "
        f"{aspect_tire}, {diameter_wheel}, {format_volume_liters}\n")

# Opens the file and stores that as a variable, then saves
# the txt_save string into the document.
with open("volumes.txt", "at") as volumes_file:
    volumes_file.write(str(txt_save))
