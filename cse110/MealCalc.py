# This will give the meal calculator the proper inputs.
childmeal = float(input("What is the price of a child's meal? $"))
adultmeal = float(input("What is the price of an adult's meal? $"))
children = int(input('How many children are there? '))
adults = int(input('How many adults are there? '))
taxrate= float(input('What is the sales tax rate? '))
tip_amount = float(input('Enter a tip amount: $'))

# This will show the subtotal with the tip included.
stotal = (float(childmeal * children)) + (float(adultmeal * adults))
subtotal = '{:.2f}'.format(stotal)
print('\nSubtotal: $' + subtotal)
print(f'Tip: ${tip_amount:.2f}')

# This will show the sales tax.
stax = (float(subtotal) * float(taxrate)) / 100
salestax = '{:.2f}'.format(stax)
print('Salestax: $' + salestax)

# This will show the total.
tot = float(salestax) + float(subtotal) + float(tip_amount)
total = '{:.2f}'.format(tot)
print(f'Total: $' + total)

# This will give the payment amount and proper change based on payment.
payment = float(input('\nWhat is the payment amount? $'))
chng = float(payment) - float(total)
change = '{:.2f}'.format(chng)
print('Change: $' + change)