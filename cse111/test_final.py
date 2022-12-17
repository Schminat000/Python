"""Verify that the functions imported below work correctly"""

# Imports the functions being tested, random, pytest modules.
from final import get_rolls, calculate_efficiency_bonus
import random
import pytest

# Defines test_get_rolls function.
def test_get_rolls():

    # Test Case 1: 
    for _ in range(5):
        
        # Sets the dice_types array.
        dice_types = [2, 3, 4, 6, 8, 10, 12, 20, 100]

        # Creates a random number selecter.
        random_dice_picker = random.randint(0, 8)

        # Asserts that random_dice_picker is greater
        # than or equal to 0, less than or equal to 8,
        # and is an integer.
        assert random_dice_picker >= 0, "Needs to be"\
                " within the index range. Greater than"\
                " or equal to 0."
        assert random_dice_picker <= 8, "Needs to be"\
                " within the index range. Less than or "\
                " equal to 8."
        assert isinstance(random_dice_picker, int), "Needs"\
                " to be an integer."

        # If random_dice_picker is equal to
        # one of the specified numbers of
        # the array index, it takes that value
        # and stores it into the dice_type variable.
        # Or else, it will exit the program.
        if random_dice_picker == 0:
            dice_type = dice_types[0]
        elif random_dice_picker == 1:
            dice_type = dice_types[1]
        elif random_dice_picker == 2:
            dice_type = dice_types[2]
        elif random_dice_picker == 3:
            dice_type = dice_types[3]
        elif random_dice_picker == 4:
            dice_type = dice_types[4]
        elif random_dice_picker == 5:
            dice_type = dice_types[5]
        elif random_dice_picker == 6:
            dice_type = dice_types[6]
        elif random_dice_picker == 7:
            dice_type = dice_types[7]
        elif random_dice_picker == 8:
            dice_type = dice_types[8]
        else:
            exit()

    # Gives a random number between 1 and 20,
    # then stores it into a variable.
    quantity = random.randint(1, 20)
    
    # Calls the function and stores it into
    # a variable.
    roll = get_rolls(quantity, dice_type)

    # Asserts that roll is an integer and is greater than 0.
    assert isinstance(roll, int), "Needs to be an integer."
    assert roll > 0, "Not possible to get less than 0 here."

# Defines the test_calculate_efficiency_bonus
# function.
def test_calculate_efficiency_bonus():

    #Test Case 1:
    for _ in range(5):

        # Selects a random proficiency bonus modifier,
        # then stores it into a variable.
        random_prof_picker = random.randint(2, 6)

        # Asserts that random_prof_picker is greater
        # than or equal to 2, less than or equal to
        # 6, and is an integer.
        assert random_prof_picker >= 2, "Needs to be"\
                " within the range. Greater than"\
                " or equal to 2."
        assert random_prof_picker <= 6, "Needs to be"\
                " within the range. Less than or "\
                " equal to 6."
        assert isinstance(random_prof_picker, int), "Needs"\
                " to be an integer."

        # Selects a random number between 1 and 100,
        # then stores it into a variable.
        random_init_roll = random.randint(1, 100)

        # Calls the function and stores it into a variable.
        tot_roll = calculate_efficiency_bonus(random_init_roll, random_prof_picker)

        # Asserts that the function worked properly by saying it's
        # an integer and it is above 0.
        assert isinstance(tot_roll, int), "Needs to be an integer."
        assert tot_roll > 0, "Not possible to get less than 0 here."

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])