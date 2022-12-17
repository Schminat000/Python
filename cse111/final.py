# Imports the random module
# function called randint.
from random import randint

# Defines the main function.
def main():
    
    # Gets the user input and stores
    # it into a variable.
    level = int(input("What is your level (1-20)? "))

    # If the level is below 1 or above 20,
    # program breaks.
    if level < 1 or level > 20:
        print("Cannot be level 0 or above level 20.")
        exit()
    
    # Calls the get_dice_type function and
    # stores the results into a variable.
    dice_type = get_dice_type()

    # Gets user input for how many dice they
    # would like to roll.
    dice_quantity = int(input("How many dice would you"\
            " like to roll? "))
    
    # Calls the get_rolls function with the
    # parameters above, then stores them into
    # a variable.
    initial_roll = get_rolls(dice_quantity, dice_type)

    # Calls the calculate_efficiency_bonus function
    # with the parameters above and stores the
    # results into a variable.
    total_roll = calculate_efficiency_bonus(initial_roll, level)

    # Prints the results.
    print(f"You rolled a total of {total_roll}.")

# Defines the get_dice_type function.
def get_dice_type():
    """Returns the user chosen dice_type from a list
    which contains: d2, d3, d4, d6, d8, d10, d12, or
    d20. If the dice_type is not in dice_types list,
    the program will exit.

    Return: which dice_type was chosen.
    """
    # Sets the list of all dice types.
    dice_types = [2, 3, 4, 6, 8, 10, 12, 20, 100]

    # Gets the user's dice type and stores it into
    # a variable.
    dice_type = int(input("Choose the dice type ("\
            "d2, d3, d4, d6, d8, d10, d12, d20): d"))

    # If dice_type is in dice_types
    # dice_type stays the same. Else,
    # prints the statement below.
    if dice_type in dice_types:
        dice_type = dice_type
    else:
        print("There are no other dice choices.")
        exit()
    
    return dice_type

# Defines the get_rolls function and
# uses two parameters.
def get_rolls(quantity, type) :
    """Returns the total_roll so far from the rolls_list.
    It takes two parameters of which are put into a for
    loop and adds the random rolls into the rolls_list.
    Then, it will use another for loop to add those rolls
    to the total_roll variable.

    Parameter
        quantity: an integer.
            Whatever the quantity is, the program will
            roll that many times.
        type: an integer.
            The type of dice determines what range the
            randint function will go to. It will determine
            the random numbers each pass through.

    Return: the total random dice roll from rolls_list.
    """
    # Sets the empty rolls_list and sets
    # the total_roll variable to 0.
    rolls_list = []
    total_roll = 0

    # For each quantity in range of quantity,
    # randomly rolls a number between 1 and type.
    # Then adds that number to a list.
    for quantity in range(quantity):
        roll = randint(1, type)
        rolls_list.append(roll)

    # For each roll in rolls_list, total_roll
    # is increased.
    for roll in rolls_list:
        total_roll += roll

    return total_roll

# Defines the calculate_efficiency_bonus function
# with two parameters.
def calculate_efficiency_bonus(initial_roll, lvl):
    """Returns the computed total with all addtions. This takes
    two parameters of initial_roll and lvl. This functions takes
    lvl and sees if it is in range of any of the ranges below and
    gives the proficiency_bonus it's value through the Player's
    Handbook resource. It then takes the initial_roll and adds
    them together and stores it into the total_roll variable.
    Parameter
        initial_roll: an integer.
            It is the previous total number given from the
            get_rolls function as a variable.
        lvl: an integer.
            This is taken from the user to determine what level
            their character is and is used to get the proper
            proficiency bonus based off their level.
    Return: the absolute total from all rolls combined with the
        added proficiency bonus.
    """
    # Stores zero into the proficiency_bonus
    # variable.
    proficiency_bonus = 0

    # If lvl is in a certain range,
    # sets the proficiency_bonus to
    # a number.
    if lvl in range(1, 4):
        proficiency_bonus = 2
    elif lvl in range(5, 8):
        proficiency_bonus = 3
    elif lvl in range(9, 12):
        proficiency_bonus = 4
    elif lvl in range(13, 16):
        proficiency_bonus = 5
    elif lvl in range(17, 20):
        proficiency_bonus = 6

    # Adds initial_roll & proficiency_bonus then
    # stores the result into total_roll
    total_roll = initial_roll + proficiency_bonus

    return total_roll

# If name is main then begin program.
if __name__ == "__main__":
    main()