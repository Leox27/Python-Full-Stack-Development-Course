##1. To check whether the string is starting value is vowel or not

#string = input('Enter the string: ')
vowel = lambda string: string[0] in 'AEIOUaeiou'
print(vowel('Mayur'))
print(vowel('Amar'))
'''
>>>
False
True
'''

vowel = lambda string: 'Vowel' if string[0] in 'AEIOUaeiou' else 'Consonant'
print(vowel('Mayur'))
'''
>>>
Consonant
'''

##2. Sum of the two numbers
add=lambda a, b: a+b
print(add(1, 2))
'''
>>>
3
'''

##3. Write a lambda to find the greatest of the two numbers
num = lambda m, n: m if m>n else n
print(num(10, 27))
'''
>>>
27
'''

##4. To calculate simple interest from the given principal, rate of interest and time
principal = lambda p,r,t:(p*r*t)/100
print(principal(1000, 5, 1))
'''
>>>
50.0
'''

##5. To reverse a string
rev_string = lambda string: string[::-1]
print(rev_string('Suraj'))
'''
>>>
jaruS
'''

##6. To check the length of the string
len_string = lambda string: len(string)
print(len_string('Datta'))
'''
>>>
5
'''

##7. To check whether a character is upper case
upp_char = lambda char: 'A'<=char<='Z'
print(upp_char('V'))
'''
>>>
True
'''

##8. To check whether the string is palindrome or not. if it palindrome then return the string as it is else  retrin the reverse string
palindrome = lambda pal_string: pal_string if pal_string == pal_string[::-1] else pal_string[::-1]
print(palindrome('mam'))
print(palindrome('sam'))
'''
>>>
mam
mas
'''

##9. Program to add minimum 3 numbers and maximum 5 numbers
numbers=lambda p,q,r,s=0,t=0: p+q+r+s+t
print(numbers(1, 2, 3, 5))
'''
>>>
11
'''

##10. To return concanited list if both the list has same length else return list one
list1=[1, 2, 3]
list2=[4, 5, 6]
cancanited=lambda list1, list2: list1 + list2 if len(list1) == len(list2) else list1
print(cancanited(list1, list2))
'''
>>>
[1, 2, 3, 4, 5, 6]
'''

list3=[1, 2, 3]
list4=[4, 5, 6, 7]
cancanited=lambda list3, list4: list3 + list4 if len(list3) == len(list4) else list3
print(cancanited(list3, list4))
'''
>>>
[1, 2, 3]
'''

