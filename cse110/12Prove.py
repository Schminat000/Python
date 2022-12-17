# Creates variables and adds values to them for later use.
chosen_year_life_expectancy_list = []
max_life = -1
max_life_country = ""
min_life = 999999
min_life_country = ""
chosen_max_life = -1
chosen_max_life_country = ""
chosen_min_life = 999999
chosen_min_life_country = ""

# User inputs wanted year.
chosen_year = int(input("Enter the year of interest: "))

# Opens the file and closes when done.
with open("life-expectancy.csv") as file_data:
    
    # For each line in the date file.
    next(file_data)
    for line in file_data:
        
        # Line cleanup.
        line = line.strip()
        parts = line.split(",")

        # List organization and appends.
        country = parts[0]
        year = int(parts[2])
        life_expectancy = float(parts[3])

        # If statement to change the variables of the max data in the respective list.
        if life_expectancy > max_life:
            max_life = life_expectancy
            max_life_country = country
            max_life_year = year

        # If statement to change the variables of the min data in the respective list.
        if life_expectancy < min_life:
            min_life = life_expectancy
            min_life_country = country
            min_life_year = year

       # If statement to take info from the given user input to append that info into it's list and to grab the average/max/min of that year.
        if year == chosen_year:
            
            # Adds the information to a list.
            chosen_year_life_expectancy_list.append(life_expectancy)

            # Creates the average of the chosen year.
            chosen_average_life_expectancy = sum(chosen_year_life_expectancy_list) / len(chosen_year_life_expectancy_list)

            # This gives the user input's max life expectancy and in which country.
            if life_expectancy > chosen_max_life:
                chosen_max_life = life_expectancy
                chosen_max_life_country = country

            # This gives the user input's min life expectancy and in which country.
            if life_expectancy < chosen_min_life:
                chosen_min_life = life_expectancy
                chosen_min_life_country = country

# Print the values.
print(f"\nThe overall max life expenctancy is: {max_life} from {max_life_country} in {max_life_year}")
print(f"The overall min life expectancy is: {min_life} from {min_life_country} in {min_life_year}")
print(f"\nFor the year {chosen_year}:")
print(f"The average life expectancy across all countries was: {chosen_average_life_expectancy:.2f}")
print(f"The max life expectancy was in {chosen_max_life_country} with {chosen_max_life}")
print(f"The min life expectancy was in {chosen_min_life_country} with {chosen_min_life}")

# python 12Prove.py