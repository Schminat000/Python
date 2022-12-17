# Creates a list to append age values into.
age_list = []

# Opens the file and closes when done.
with open("life-expectancy.csv") as file_data:
    
    # For each line in the date file.
    next(file_data)
    for line in file_data:
        
        # Line cleanup.
        clean_line = line.strip()
        parts = clean_line.split(",")

        # List organization and appends.
        life_expectancy = parts[3]
        age_list.append(life_expectancy)

# Print the values.
print(f"Maximum age value: " , max(age_list))
print(f"Minimum age value: " , min(age_list))