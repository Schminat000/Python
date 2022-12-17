print('On a rating scale of 1-10, please rate the following:')

loan_size = int(input('\nHow large is the loan? '))
credit = int(input('How good is your credit history? '))
income = int(input('How high is your income? '))
down_payment = int(input('How large is your down payment? '))

should_loan = False

if loan_size >= 5:
    if credit >= 7 and income >= 7:
        should_loan = True
    elif credit >= 7 or income >= 7:
        if down_payment >= 5:
            should_loan = True
        else:
            should_loan = False
    else:
        should_loan = False
else:
    if credit < 4:
        should_loan = False
    else:
        if income >= 7 or down_payment >= 7:
            should_loan = True
        elif income >= 4 and down_payment >= 4:
            should_loan = True
        else:
            should_loan = False

if should_loan:
    print('You have a good loan.')
else:
    print('This is not a good loan.')


# print("For each of these questions, please provide a 1-10 rating:")

# loan_size = int(input("How large is the loan? "))
# credit = int(input("How good is your credit history? "))
# income = int(input("How high is your income? "))
# down_payment = int(input("How large is your down payment? "))

# should_loan = False

# if loan_size >= 5:
#     if credit >= 7 and income >= 7:
#         should_loan = True
#     elif credit >= 7 or income >= 7:
#         if down_payment >= 5:
#             should_loan = True
#         else:
#             should_loan = False
#     else:
#         should_loan = False
# else:
#     if credit < 4:
#         should_loan = False
#     else:
#         if income >= 7 or down_payment >= 7:
#             should_loan = True
#         elif income >= 4 and down_payment >= 4:
#             should_loan = True
#         else:
#             should_loan = False

# if should_loan:
#     print("The decision is yes. This is a good loan.")
# else:
#     print("The decision is no. You should not loan this money.")


# if gpa >= .85:
#     if lowerst_grade >= .70:
#         print('Well done')

# if gpa>= .85 and lowest_grade >= .70:
#     print('Well done')

# if gpa >= .85 and lowest_grade >= .70:
#     honor_roll = True
# else:
#     honor_roll = False
# if honor_roll:
#     print('Well done')

# gpa = float(input('What was your Grade Point Average? '))
# lowest_grade = float(input('What was your lowest grade? '))

# if gpa >= .85 and lowest_grade >= .70:
#     honor_roll = True
# else:
#     honor_roll = False
# if honor_roll:
#     print('You made the honor roll')