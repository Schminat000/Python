# 1. Name:
#      -Nathan Schmidt-
# 2. Assignment Name:
#      -Lab 03: Calendar-
# 3. Assignment Description:
#      -The program takes the user's month and year to display
#      that specific calendar month and day.-
# 4. What was the hardest part? Be as specific as possible.
#      -The hardest part of the assignment to me was trying to
#      debug the program. It took me a long time to do this because
#      figuring out the kinks of how to display the 
#      calendar took me a minute.-
# 5. How long did it take for you to complete the assignment?
#      -5 hours.-

# Defines the main function.
def main():

    month = getMonth()
    userMonth = getMonthDictionery(month)
    userYear = getYear()
    day = getLeapYear(userYear, month)
    displayCalendar(month, userMonth, userYear, day)

# Defines the getMonth function.
def getMonth():
    """Moderates the user's given month to make sure 
    it is a formattable choice. It will tell you the 
    requirements if it is given invalid choices.
    Return: the user's month.
    """

    quit = False

    # When quit = True, the program will quit.
    while quit != True:

        # The progam won't quit until it is satisfied
        # with the user's answer.
        try:
            month = input("What is the month? ")
            if int(month) > 12 or int(month) < 1:
                print("Month must be between 1 and 12.")
            elif int(month) <= 12 and int(month) >= 1:
                quit = True
        except:
            print("Month must be an integer.")

    # Returns the month variable as an integer.
    return int(month)

# Defines the getYear function.
def getYear():
    """Moderates the user's given year to make sure 
    it is a formattable choice. It will tell you the 
    requirements if it is given invalid choices.
    Return: the user's year.
    """

    quit = False

    # When quit = True, the program will quit.
    while quit != True:

        # The progam won't quit until it is satisfied
        # with the user's answer.
        try:
            year = input("What is the year? ")
            if int(year) < 1753:
                print("Year must be 1753 or later.")
            elif int(year) >= 1753:
                quit = True
        except:
            print("Year must be an integer.")

# Returns the year variable as an integer.
    return int(year)

# Defines the getMonthDictionary function.
def getMonthDictionery(i):
    """Takes the user's given month and returns the month 
    based off what key the user gave. It looks at that key 
    and takes the information within that key to get the 
    appropriate month.
    Parameter
        i: an integer.
            It is the user's month and uses the dictionary 
            as a key to give the month name.
            Return: the given month's name.
            """

    month ={1:'January', 2:'February', 3:'March',
            4:'April', 5:'May', 6:'June', 7:'July',
            8:'August', 9:'September', 10:'October',
            11:'November', 12:'December'}

    dictionaryMonth = month[i]

    # Returns the dictionary with the month key.
    return dictionaryMonth

# Defines the getLeapYear function.
def getLeapYear(userYear, userMonth):
    """Determines if the year and month is in a 
    leap year.
    Parameters
        userYear: an integer.
            This is the user's chosen year.
        userMonth: an integer.
            This is the user's chosen month.
    Return: the last day of the month.
    """

    day = (userYear - 1) % 400

    day = (day // 100) * 5 + ((day % 100) - (day % 100) // 4)\
                                    + ((day % 100) // 4) * 2

    day = day % 7

    noLeapYear = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]

    leapYear = [31, 29, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]

    end_day = 0

    # Determines if there is leapYear or
    # noLeapYear.
    if userYear % 4 == 0:
        for i in range(int(userMonth) - 1):
            end_day += leapYear[i]
    else:
        for i in range(int(userMonth) - 1):
            end_day += noLeapYear[i]

    day += (end_day % 7)
    day %= 7

    # Returns the day variable.
    return day

# Defines the displayCalendar function.
def displayCalendar(userMonth, month, userYear, day ):
    """Takes all the parameters and displays everything 
    in the calendar format.
    Parameters
        userMonth: a string.
            This is the user's chosen month as a name.
        month: an integer.
            This is the user's chosen month as an integer.
        userYear: an integer.
            This is the user's chosen year.
        day: an integer.
            This is the last day of the month.
    """

    space = ''
    space = space.rjust(2, ' ')

    # Displays the month and year of the user's choice.
    print(month, userYear)
    print('Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa')

    if userMonth == 4 or userMonth == 6 or userMonth == 9 \
                                        or userMonth == 11:
        for i in range(31 + day):
            
            if i <= day:
                print(space, end = ' ')
            else:
                print("{:02d}".format(i - day), end = ' ')
                if (i + 1) % 7 == 0:
                    print()

    elif userMonth == 2:
        if (userYear % 4) == 0:
            last = 30
        else:
            last = 29
            
        for i in range(last + day):
            if i <= day:
                print(space, end = ' ')
            else:
                print("{:02d}".format(i - day), end = ' ')
                if (i + 1) % 7 == 0:
                    print()

    else:
        for i in range(32 + day):
            
            if i <= day:
                print(space, end = ' ')
            else:
                print("{:02d}".format(i - day), end = ' ')
                if (i + 1) % 7 == 0:
                    print()

# Calls the main function in an efficient
# manner.
if __name__ == "__main__":
    main()