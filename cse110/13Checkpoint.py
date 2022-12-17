def write_message(message):
    print(message)
    print(message.upper())
    print(message.lower())

user_message = input("What is your message? ")
write_message(user_message)

# def display_regular(message):
#     print(message)

# def display_uppercase(message):
#     print(message.upper())

# def display_lowercase(message):
#     print(message.lower())

# user_message = input("What is your message? ")

# display_regular(user_message)
# display_uppercase(user_message)
# display_lowercase(user_message)


# from datetime import datetime

# def print_time(task_name):
#     print(task_name)
#     print(datetime.now())
#     print()

# first_name = "Nathan"
# print_time("first name assigned")

# for x in range(0,10):
#     x += 1
#     print(x)
# print_time("\nLoop Completed.")



# def get_initial(name):
#     initial = name[0:1].upper()
#     return initial

# first_name = input("Enter your first name: ")
# middle_name = input("Enter your middle name: ")
# last_name = input("Enter your last name: ")

# print("Your initials are " + get_initial(first_name) + get_initial(middle_name) + get_initial(last_name))



# def get_initial(name, force_uppercase):
#     if force_uppercase:
#         initial = name[0:1].upper()
#     else:
#         initial = name[0:1]
#     return initial

# first_name = input("Enter your first name: ")
# first_name_initial = get_initial(force_uppercase=True, name=first_name)

# print("Your initial is: " + first_name_initial)