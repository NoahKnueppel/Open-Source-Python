def calculate():
    operation = input('''
Please enter the mathmatical operation you would like to use:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Please enter your first number: '))
    number_2 = int(input('Please enter your second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('The operator you have entered is invalid, please restart the program and enter a valid operator')

    again()

def again():
    calc_again = input('''
Would you like to make another calculation?
Enter Y if yes and N if no
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
      print('Goodbye')
    else:
        again()

calculate()