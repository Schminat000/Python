# 1. Name:
#      -Nathan Schmidt-
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      -Takes a number and uses an algorithm to do the Fibonacci Number.-
# 4. What was the hardest part? Be as specific as possible.
#      -The assignment went fairly well after I got inspiration
#       from the instructor pseudocode. The most difficult part was
#       the pseudocode and trace table as those make no sense to me
#       for some reason. This assigment was just fine to me after the
#       design stage.-
# 5. How long did it take for you to complete the assignment?
#      -4 hours.-

# Defines the main function.
def main():

    # Asks the user for an input and stores it
    # into a variable.
    input_number = int(input("Which Fibonacci number would "\
        "you like to see? "))

    # Calls the function and parameter then stores it
    # into a variable.
    fibonacci_number = get_fibonacci_number(input_number)

    # Prints to the user the original number and it's new
    # Fibonacci number.
    print(f"Fibonacci number {input_number} is {fibonacci_number}.")

# Defines the function to get the fibonacci number
# and has the parameter of input_number.
def get_fibonacci_number(input_number):
    """Takes an integer from the user's chosen number and turns it into
    a fibonacci number.
    Parameter
        input_number: an integer.
            The user's chosen input_number will go into the algorithm and
            become the fibonacci number equivalent.
    Return: the fibonacci number.
    """
    # Gives values to the specified variables.
    x = 2
    y = 1
    z = 0

    # Asserts to verify that the number contains no invalid value types,
    # that the input_number is above 0, and contains no negative
    # integers.
    assert type(input_number) == int, "Strings aren't valid."
    assert input_number != 0, "Zero isn't a valid integer for the "\
        "following algorithm."
    assert input_number > 0, "The input_number variable needs to be greater "\
        "than 0."

    # If the user input is 1, the number is now 2.
    if input_number == 1:
        input_number = x
    
    # Else if the input is 2, the number is now 1.
    elif input_number == 2:
        input_number = y

    else:
        
        # Else, we do a for loop and specify the variables
        # which then the algorithm takes place.
        for i in range(2, input_number):
            z = x + y
            x = y
            y = z
            input_number = y

    return input_number


# Efficient way to call the main function.
if __name__ == "__main__":
    main()