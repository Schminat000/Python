first_number = input('What is the first number? ')
second_number = input('What is the second number? ')

if first_number > second_number:
    print('The first number is greater.')
else:
    print('The first number is not greater.')

if first_number == second_number:
    print('The numbers are equal.')
else:
    print('The numbers are not equal.')

if first_number < second_number:
    print('The second number is greater.')
else:
    print('The second number is not greater.')

fav_animal = input('\nWhat is your favorite animal? ')

if fav_animal.lower() == 'owl':
    print('That is my favorite animal too!')
else:
    print('That is not my favorite animal.')

# province = input('What province do you live in? ')
# tax = 0
# if province == 'Alberta':
#     tax = 0.05
# elif province == 'Nunavut':
#     tax = 0.05
# elif province == 'Ontario':
#     tax = 0.13
# else:
#     tax = .15
# print(tax)

#  country = input('Enter the name of your home country: ')
# if country.lower() == 'canada':
#     print('So you must like hockey!')
# else:
#     print('You are not from Canada')

# price = input('how much did you pay? ')
# price = float(price)
# if price >= 1.00:
#     tax = .07
#     print('Taxrate is: ' + str(tax))
# else:
#     tax = 0
#     print('Tax rate is: ' + str(tax))

# or

# price = input('how much did you pay? ')
# price = float(price)
# if price >= 1.00:
#     tax = .07
# else:
#     tax = 0
# print('Tax rate is: ' + str(tax))