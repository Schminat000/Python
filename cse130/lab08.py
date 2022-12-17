# 1. Name:
#      -Nathan Schmidt-
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      -Sort's a list of files given from .json files. Then proceeeds to
#       sort the list in order and display the results.-
# 4. What was the hardest part? Be as specific as possible.
#      -The assignment went fairly well I'd say. I ran into issues with
#       the programming part itself. It was difficult for me to get a 
#       grasp on the course content because the developer's forum
#       had way too many comments to be able to sort through in order
#       to receive help. Everything else went quite smooth I think.
#       I ran into issues with the pseudocode design because we can't
#       test it so it is hard to come up with the right answer for that
#       assignment.-
# 5. How long did it take for you to complete the assignment?
#      -3 hours-

# This imports the library used for .json files.
import json

# Creates a function that sets up the sorting process.
def sorting_program(lookup):
    
    # For loop indicating that i_pivot is where we will be
    # swapping.
    for i_pivot in range(len(lookup) -1, 0, -1):

        # Creates an assert for i_pivot that the max is equal
        # to an integer.
        assert i_pivot, int

        # Takes i_pivot and subtracts one position then stores the
        # new number into a variable.
        i_largest = i_pivot - 1

        # For each word in range of i_largest and subtract 2.
        for index_word in range(i_largest, -1, -1):

            # If lookup's value is less than index word's
            # value...
            if lookup[i_largest] < lookup[index_word]:

                # i_largest's becomes index_word's
                # value.
                i_largest = index_word

        # If lookup's value is greater than lookup's
        # i_pivot's value...
        if lookup[i_largest] > lookup[i_pivot]:

            # Swap the location of each!
            lookup[i_pivot], lookup[i_largest] = lookup[i_largest], lookup[i_pivot]

    # Returns lookup.
    return lookup

# Asks the user for the file name and stores their response
# in a variable.
FILE_NAME = input("What is the name of the file? ")

# Makes sure the file is good.
try:

    # Opens file and store it into a variable.
    # When it's done, it will close the file.
    with open(FILE_NAME, "r") as file_lookup:
        
        # Taking the load function for the .json
        # and stores it into a variable.
        lookup_file = json.load(file_lookup)

        # Looks into the .json file looking for "array"
        # then stores it into a variable.
        lookup = lookup_file["array"]

    # The assert makes sure the file has any content,
    # if not, then it says "This is an empty list therefore,
    # it cannot be sorted."
    assert len(lookup) > 0, "This is an empty list therefore, it cannot be sorted."

    # Prints the statement below.
    print(f"The values in {FILE_NAME} are: ")
    
    # For each word within the function...
    for word in sorting_program(lookup):
        
        # It prints the formatted and sorted
        # words each on new lines.
        print(f"        {word}")

# If file is not good or doesn't exist...
except (FileNotFoundError, PermissionError) as exit:

    # Prints error and closes.
    print(exit)