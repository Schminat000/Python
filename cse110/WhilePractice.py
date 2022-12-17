# positive_number = int(input('Please type a positive number: '))
# while positive_number < 0:
#     print('Sorry, that is a negative number. Please try again.')
#     positive_number = int(input('Please type a positive number: '))
# print(f'The number is: {positive_number}')

# candy = input('May I have a piece of candy? ')
# while candy.upper() == 'NO':
#     candy = input('May I have a piece of candy? ')
# else:
#     if candy.upper() == 'YES':
#         print('Thank you.')

answer = ''
while answer != 'yes':
    answer = input('May I have a piece of candy? ')
print('Thank you.')