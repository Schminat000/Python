# This is the list of names and ages.
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

# This is the variable preparation.
youngest_age = 100
youngest_name = ""

# This is our for function that cleans up the list and seperates them into names and numbers.
for information in people:
    parts = information.split(" ")
    people_names = parts[0]
    age = int(parts[1])

# This is our if statement sifting through our list to look for the youngest name and age.
    if age < youngest_age:
        youngest_age = age
        youngest_name = people_names

# This prints the youngest's name and age.
print(f"The youngest person is: {youngest_name} and they are {youngest_age} years old.")