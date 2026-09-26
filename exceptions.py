try:
    n1 = int(input('Enter a number:'))
    n2 = int(input('Enter another number:'))
    answer1 = n1+n2
    answer2 = n1/n2
    print('Answer is :', answer1)
    print('Answer is :', answer2)

except ZeroDivisionError:
    print('Division by zero is not allowed')
except ValueError:
    print('Please enter a whole number')
