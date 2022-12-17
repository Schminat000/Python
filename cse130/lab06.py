# 1. Name:
#      Nathan Schmidt
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      It searches a specific file for a word prompted by the user.
# 4. Algorithmic Efficiency
#      O(log n) is the efficiency because it loops through and cuts
#      the input in half each time.
# 5. What was the hardest part? Be as specific as possible.
#      The assignment wasn't very difficult until I was trying to make
#      the program print whether or not it was found. I ran into the issue and
#      couldn't figure out the solution to the problem I was having. I went to tutoring
#      this week and it still wasn't enough for my program to work. Do you see
#      what the issue is with the code? I'd appreciate the feedback so I can figure out
#      how to print the proper things to the user. I looked at your solution but
#      still ran into the issue with your code. Thanks!
# 6. How long did it take for you to complete the assignment?
#      8 hours.

# Creates a function.
def binary_search(array, target):

    # Sorts the array and stores it into a variable
    array = sorted(array)

    # Stores information into the variables.
    start = 0
    end = len(array) - 1

    # While loop to say to stop when the start variable is
    # less than or equal to the end variable.
    while start <= end:
        middle = start + (end - start) // 2

        # Store the middle of the array into a variable.
        item = array[middle]

        # If the target is equal to the item, program
        # returns the middle.
        if target == item:
            return middle
        
        # If the target is less than the item, end variable is changed
        # to subtract the middle and one.
        elif target < item:
            end = middle - 1

        # Otherwise, program takes the middle and adds 1 to the
        # start variable.
        else:
            start = middle + 1

    # Returns none.
    return None

# Imports the json module.
import json

# Asks the user for the file name.
FILE_NAME = input("What is the name of the file? ")

# If the file name is true, program continues.
if FILE_NAME:

    # Opens the file name, reads it, and stores it into a variable.
    with open(FILE_NAME) as lab_file:
        json_dict = json.loads(lab_file.read())
        list = json_dict["array"]

        # Asks user for the desired word and stores it into a variable.
        word = input("What name are we looking for? ")

        # Calls the function.
        binary_search(list, word)

        # If the word is equal to or not equal to the item, it prints the results.
        if word:
            print(f"We found {word} in {FILE_NAME}.")
        if not word:
            print(f"Unable to find the word.")

# If the file name doesn't exist, the program tells the user it is
# unable to open it.
if not FILE_NAME:
    print("Unable to open file.")