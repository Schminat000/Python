# 1. Name:
#      -Nathan Schmidt-
# 2. Assignment Name:
#      Lab 13: Prime Numbers
# 3. Assignment Description:
#      -User chooses an integer and then the program tells
#      which prime numbers are within that integer.-
# 4. What was the hardest part? Be as specific as possible.
#      -The assignment went fairly well after I got inspiration
#       from the instructor pseudocode. The most difficult part was
#       the pseudocode and trace table as those make no sense to me
#       for some reason. This assigment was just fine to me after the
#       design stage.-
# 5. How long did it take for you to complete the assignment?
#      -4 hours.-

# While the statment is true...
while True:

    # Gets the user's input and stores it into
    # max_number.
    max_number = int(input("What is the max number? "))

    # If max_number is greater than or equal to 2...
    if max_number >= 2:

        # Program breaks.
        break

    # Makes sure the max_number is greater than 0.
    assert max_number >= 2, "Number is expected to be greater" \
            f" than or equal to 2, got: {max_number}."

    assert isinstance(max_number, int), "The variable max_number " \
            f"should be an integer not a {type(max_number)}."

# Setting primes_list to make the list of primes.
primes_list = list(range(2, max_number + 1))

# Makes sure the primes_list is a list.
assert isinstance(primes_list, list), "This should be a list not a" \
        f" {type(primes_list)}."

# For each prime_number in primes_list...
for prime_number in primes_list:

    # If prime number is greater than max_number
    # times 0.5...
    if prime_number > max_number ** 0.5:

        # Program breaks.
        break

    # For each multiple in the range of increments of 2 of the
    # length of primes_list -1...
    for multiple in range(2, primes_list[len(primes_list) - 1]):

        # Multiply multiple and prime_number together and
        # stores it into the variable cross_out.
        cross_out = multiple * prime_number

        # Makes sure the cross_out variable is an integer.
        assert isinstance(cross_out, int), "The variable cross_out " \
                f"should be an integer not a {type(cross_out)}."

        # Makes sure cross_out is greater than 0.
        assert cross_out > 0, "Number is expected to be greater" \
                f" than 0, got: {cross_out}."

        # If cross_out is greater than the primes_list length
        # -1...
        if cross_out > primes_list[len(primes_list) - 1]:

            # Program breaks.
            break

        # Else if cross_out is in primes_list...
        elif cross_out in primes_list:

            # Remove the cross_out location in
            # primes_list.
            primes_list.remove(cross_out)

# Makes sure the primes_list is a list.
assert isinstance(primes_list, list), "This should be a list not a" \
        f" {type(primes_list)}."

# Prints prime_list.
print(primes_list)