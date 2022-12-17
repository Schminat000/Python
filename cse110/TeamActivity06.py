# Team Activity 06: Team 8

first_rider_age = int(input('What is the age of the first rider? '))
first_rider_height = int(input('What is the height of the first rider? '))
second_rider_question = input('Is there a second rider (yes/no)? ')

should_ride = False
second_rider = False

if second_rider_question.lower() == 'yes':
    second_rider = True
    if second_rider:
        second_rider_age = int(input('What is the age of the second rider? '))
        second_rider_height = int(input('What is the height of the second rider? '))
        if first_rider_height < 36 or second_rider_height < 36:
            should_ride = False
        else: 
            if first_rider_age >= 18 or second_rider_age >=18:
                should_ride = True
            else:
                should_ride = False
else:
    if first_rider_age >= 18 and first_rider_height >= 62:
        should_ride = True
    else: 
        should_ride = False
if should_ride:
    print('Welcome to the ride, please be safe and have fun!')
else:
    print('Sorry, you may not ride.')