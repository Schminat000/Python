# Imports the csv library and the datetime modules.
import csv
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

def main():

    # Verifies that everything is correct.
    try:
        # Opens the file and stores it into
        # csv_file.
        with open("products.csv", "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
            reader = csv.reader(csv_file)

        # Index of the key column
        # in the products.csv file.
        KEY_INDEX = 0
        NAME_INDEX = 1
        PRICE_INDEX = 2

        # Names variables and gives values
        # to be used later.
        number_of_items = 0
        subtotal = 0

        # Read the contents of the products.csv into a
        # compound dictionary named product_dictionary.
        # Use the phone numbers as the keys in the dictionary.
        product_dictionary = read_dict("products.csv", KEY_INDEX)

        # Print the products compound dictionary.
        print(f"Inkom Emporium\n")

        # Opens the file and stores it into the variable
        # csv_file. It closes when complete.
        with open("request.csv", "rt") as csv_file:
            
            # Reads the file and stores it into
            # a variable.
            reader = csv.reader(csv_file)

            # Skips the first line of the file.
            next(reader)

            # For each line in reader...
            for line in reader:

                # If the line with the 0 index matches a key
                # from product_dictionary...
                if line[KEY_INDEX] in product_dictionary:

                    # The variable product_request takes the
                    # product_dictionary index of line of index 0 spot.
                    product_request = product_dictionary[line[KEY_INDEX]]

                    # Takes product_request of index 0 and stores
                    # it into a variable.
                    name = product_request[NAME_INDEX]

                    # Takes product_request of index 2 and stores
                    # it into a variable.
                    price = product_request[PRICE_INDEX]

                    # Takes product_request of index 1 and stores
                    # it into a variable.
                    quantity = line[NAME_INDEX]

                    # Prints the requests.
                    print(f"{name}: {quantity} @ {price}")
                    
                    # Gets the total number of items
                    # from the quantity variable then stores
                    # it into a variable.
                    number_of_items += int(quantity)

                    # Gets the subtotal price by multiplying
                    # price and quantity together then stores
                    # it into a variable.
                    subtotal += float(price) * int(quantity)

                    # Gets the total by multiplying the subtotal
                    # and stores it into a variable.
                    total = subtotal * 1.06

                    # Gets the sales tax total by subtracting
                    # the total and subtotal then stores it into
                    # a variable.
                    sales_tax = total - subtotal

            # Prints the receipt and all it's contents.
            print(f"\nNumber of Items: {number_of_items}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Sales Tax: ${sales_tax:.2f}")
            print(f"Total: ${total:.2f}")
            print("\nThank you for shopping at the Inkom Emporium.")

            # Print the current day of the week and the current time.
            print(f"{current_date_and_time:%a %b %d %Y %I:%M %p}\n")

            # To exceed requirements, prints a statement
            # asking the customer if they'd like to complete
            # an online survey and potentially win a gift card.
            # (The website is fake. So, don't go there.)
            print("Did you have a good or bad experience today? \n"\
                    "Well, we'd like to hear about it! If you \n"\
                    "complete our survey, you'll be entered in \n"\
                    "a raffle to win a $100 gift card to Inkom \n"\
                    "Emporium! Complete it now for a chance to \n"\
                    "win! Go to: www.inkomemporium.com/survey")

    # Except block catches the problem if file is not found.
    except FileNotFoundError as error:
        print("Error: missing file")
        print(error)
        print("Please make sure the file name is correct.")

    # Except block catches the problem if file is not found.
    except PermissionError as error:
        print("Error: permission required")
        print(error)
        print("Please make sure you have permission " \
                "to use the file.")

    # Except block catches the problem if file is not found.
    except KeyError as error:
        print("Error: key value is invalid")
        print(error)
        print(f"Please make sure the key value is "\
                "correct.")

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    products_dictionary_list = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]

                # Store the data from the current
                # row into the dictionary.
                products_dictionary_list[key] = row_list

    # Return the dictionary.
    return products_dictionary_list

# Call main to start this program.
if __name__ == "__main__":
    main()