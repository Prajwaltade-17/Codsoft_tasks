print('Calculate the Values')
a = int(input('Enter 1st value: '))
b = int(input('Enter 2nd value: '))
ch = 0

while ch != 5:
    print('Choose an operation:')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Exit')
    
    ch = int(input('Enter your choice: '))
    
    if ch == 1:
        c = a + b
        print('Sum:', c)
    elif ch == 2:
        c = a - b
        print('Subtraction:', c)
    elif ch == 3:
        c = a * b
        print('Product:', c)
    elif ch == 4:
        if b != 0:  # Prevent division by zero
            c = a / b
            print('Quotient:', c)
        else:
            print('Error: Division by zero is not allowed.')
    elif ch == 5:
        print('Exiting...')
        break
    else:
        print('Invalid choice, please try again.')
2