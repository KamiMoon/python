try:
    num1 = input('Enter first number: ')
    num1 = int(num1)
    num2 = input('Enter second numer: ')
    num2 = int(num2)

    sum = num1 + num2
    print(sum)
except ValueError:
    print('Must enter a number')