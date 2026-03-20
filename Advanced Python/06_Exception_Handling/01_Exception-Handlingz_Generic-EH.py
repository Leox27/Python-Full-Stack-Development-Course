###Generic EH

##1. Divide two numbers
try:
    a = int(input('Enter the number a: '))
    b = int(input('Enter the number b: '))
    print(a/b)
except Exception as e:
    print(e)
'''
Enter the number a: 3
Enter the number b: 0
division by zero
'''

##2. 
try:
    for i in range(1, 1000):
        print(i)
except Exception as e:
    print(e)
'''
>>> #KeyBoardInterruptError
'''

##3. WAP Take a number from the user as input print whether it is even or odd handle an invalid input using generic exdeption.
try:
    num3 = int(input('Enter the number: '))
    if num3%2 == 0:
        print(num3, 'is Even')
    else:
        print('Odd')
except Exception as e:
    print(e)
'''
>>>
Enter the number: '7'
invalid literal for int() with base 10: "'7'"
'''

##4. WAP Ask the userto enter the string print its length handle unexpeted error like user wntered non-string type.
try:
    string4 = eval(input('Enter the string: '))
    print('Length of the string is', len(string4))
except Exception as e:
    print(e)
'''
>>>
Enter the string: 678
object of type 'int' has no len()
'''

##5. WAP predefined username & password ask user to log-in handle the error like 'wrong type empty input login' generic exception.
try:
    username = 'mayur.x27_'
    pwd = 'Legend@123'

    un = input('Enter valid username: ')
    p = input('Enter valid password: ')

    if un == "" or p == "":
        raise Exception("Input cannot be empty")
    if un == username and p == pwd:
        print('Logged in successfully')
    else:
        raise Exception("Invalid username or password")
except Exception as e:
    print(e)
'''
>>>
Enter valid username: 
Enter valid password: 890
Input cannot be empty
'''

