
###Default E.H.

'''
#syntax
try:
    //Code
except:
    //Solution
'''
##
try:
    l = [1, 2, 4, 5, 6]
    print(l[9])
except:
    print('Error Triggered')
'''
>>>
Error Triggered
'''

###try-except-else-finally
try:
    l = [1, 2, 4, 5, 6]
    print(l[5])
except:
    print('Error Triggered')
else:
    print('No Error')
finally:
    print('Execution Completed')
'''
>>>
Error Triggered
Execution Completed
'''

###User-defined exception
class Sam(Exception):
    pass

    
###Custom exception
# 1) What type of exception to raise
# 2) Which condition will raise error
# 3) Own message


a = int(input('Enter the number a: '))
b = int(input('Enter the number b: '))
if b<a:
    raise Sam('Value of b must be Greater') #we can use In-bulit or user-defined funtion in place of exception-name.
'''
>>>
Enter the number a: 9
Enter the number b: 5
Traceback (most recent call last):
  File "x:\GitHub\QSpider\06_Exception-Handlingz_try-except-else-finally-EH.py", line 51, in <module>
    raise Sam('Value of b must be Greater')
Sam: Value of b must be Greater
'''

###Assertion Error
a = int(input('Enter the number a: '))
b = int(input('Enter the number b: '))
assert b>a, ('Value of b must be Greater')
print(a+b)
'''
>>>
Enter the number a: 4 
Enter the number b: 9
13
'''

