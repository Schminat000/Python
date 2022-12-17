# 1. Name:
#      Nathan Schmidt

# 2. Assignment Name:
#      Lab 02: Authentication

# 3. Assignment Description:
#      The program looks through a list of usernames and passwords to tell whether
#      or not they are authorized in the system.

# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was turning the json file
#      into a string. Another thing that took me a minute was
#      learning how to use dictionaries. I have never used those
#      before; however, I really like them! They are super nice to use.
#      EVerything else went pretty smooth, I think!

# 5. How long did it take for you to complete the assignment?
#      Probably took me about 3 hours or so to do everything.

# Imports JSON files.
import json

# This stores the file into a variable.
FILE_NAME = "Lab02.json"

# Opens the file and puts it into a variable then closes when finished.
with open(FILE_NAME) as lab_file:

    # Stores the converted string into a variable.
    user_pass_dict = json.loads(lab_file.read())

# Stores the dictionary lists into the appropriate variables.
usernames_list = user_pass_dict["username"]
passwords_list = user_pass_dict["password"]

# User states the username and password then converts into variable.
username = input("Username: ")
password = input("Password: ")

# If statement for a username in the username lists.
if username in usernames_list:

    # Gets the username list index for each username and stores it into variable.
    index = usernames_list.index(username)

    # If the password is equal to the list, they are authenticated.
    if password == passwords_list[index]:
        print("You are authenticated!")

    # If not, they are not authorized.
    else:
        print("You are not authorized to use this system.")

# Not authorized again.
else:
    print("You are not authorized to use this system.")