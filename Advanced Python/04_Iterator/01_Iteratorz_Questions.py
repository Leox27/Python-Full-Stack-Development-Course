###
'''
##1. Divide two numbers (ZeroDivisionError, ValueError)
try:
    a = int(input('Enter the number a: '))
    b = int(input('Enter the number b: '))
    print(a/b)
    
except ZeroDivisionError:
    print('b cannot be divided by 0')
except ValueError:
    print('a & b must be integers ')

>>>
Enter the number a: 0
Enter the number b: 0
b cannot be divided by 0
Enter the number a: 4
Enter the number b: 4.8
a & b must be integers


##2. Convert string to integer
try:
    value = input("Enter the value: ")
    convert_int = int(value)  
    print(convert_int)
except ValueError:
    print("Only numeric values can be converted into integer")

Enter the value: 67
67


##3. Access list element
try:
    l1 = ['Mayur', 2, 'Vishwas', 4.7, 'Hello', 'Bye Bye']
    index = int(input('Ennter the index of collection: '))
    print(l1[index])
except IndexError:
    print(f'Please enter valid value from Right-to-Left till {len(l1)-1} or Left-to-Right till {-len(l1)}')
except ValueError:
    print('Please enter only integer type value')

Ennter the index of collection: 4
Hello
Ennter the index of collection: 7
Please enter valid value from Right-to-Left till 5 or Left-to-Right till -6


##4. Check number positive or negative
try:
    num4 = int(input('Enter an Integer: '))
    print(num4)
except ValueError:
    print('Enter a valid integer')

Enter an Integer: 1027
1027
Enter an Integer: 0
0


##5. Dictionary key search
try:
    d3 = {'Suraj':90, 'Sudarshan':51, 'Varun':70, 'Mayur':99, 'Sohel':65}
    s_name = input('Enter the Student name: ')
    marks = d3[s_name]
    print(s_name, ':', marks)
except KeyError:
    print('Enter valid key of the dictionary collection', d3)

Enter the Student name: Mayur
Mayur : 99
Enter the Student name: Sohel
Sohel : 65
'''

### Intermediate
try:
    a = int(input('Enter the number a: '))
    b = int(input('Enter the number b: '))
    operator = input('Enter operator: ')
    if operator == '+':
        print(a+b)
    elif operator == '-':
        print(a-b)
    elif operator == '*':
        print(a*b)
    elif operator == '/':
        print(a/b)
except ValueError:
    print('Enter numeric value only')
except ZeroDivisionError:
    print('Number b cannot be divisible by 0')
##6. Calculator using try-except































