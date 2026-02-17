'''
                         #### nested if ####

#Given character is vowel or consonant.
c=input("Enter the character: ")
if 'A'<=c<='Z' or 'a'<=c<='z':
    if c in 'AEIOUaeiou':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")

#Wap to login into the Instagram with valid username and password.(enter
password only if the user name is valid)

un='mayur.x27_'
pwd='Mayur@123'
username=input("Enter your valid username: ")
if username == un:
    password=input("Enter your valid password: ")
    if password == pwd:
        print("Login Successful")
    else:
        print("Invalid Password")
elif username != un:
    print("Invalid username")

#Wap to print the middle value of a list only if it is string.

lst=eval(input("Enter the list: "))
middle_val=len(lst)//2
middle_index=lst[middle_val]
if len(lst)%2 != 0:
    if type(lst[middle_val]) == str:
        print("Middle value of the list is String: ",middle_index)
    else:
        print("Middle value of the list is not a String")
else:
    print("List has not middle value")

#WAP to find greatest of 4 number
a=int(input("Enter number a: "))
b=int(input("Enter number b: "))
c=int(input("Enter number c: "))
d=int(input("Enter number d: "))
if a >= b:
    if a >= c:
        if a >= d:
            print("a is the greatest number")
        else:
            print("d is the greatest number")
    else:
        if c >= d:
            print("c is the greatest number")
        else:
            print("d is the greatest number")
else:
    if b >= c:
        if b >= d:
            print("b is the greatest number")
        else:
            print("d is the greatest number")
    else:
        if c >= d:
            print("c is the greatest number")
        else:
            print("d is the greatest number")

#Wap to print the value as it is only if the length of the value is even.
val=eval(input("Enter the value: "))
if type(val) in (str, list, tuple, set, dict):
    if len(val)%2 == 0:
        print("Length of val us even")
    else:
        print("Length of val is Odd")
else:
    print("The given val is Sigle-Value-Datatype")

#Wap to print the last value of a list only if it is palindrome string starting with vowel.
lst=eval(input("Enter the List: "))
last_index=lst[-1]
if type(last_index) == str:
    if last_index[0] in 'AEIOUaeiou':
        if last_index == last_index[::-1]:
            print("The last value of list is palindrome with 1st vowel",last_index)
        else:
            print("The list value of list is not palindrome")
    else:
        print("The last value of list doesn't start with vowel")
else:
    print("The last value of list is not Collection")

##Wap to print the reversed string only if it is starting with vowel ,ending with consonant and having a middle value.
string=input("Enter the String: ")
if len(string)%2 != 0:
    if string[0] in 'AEIOUaeiou':
        if string[-1] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            print("String is ", string[::-1])
        else:
            print("Not ending with consonant")
    else:
        print("Not starting with vowel")
else:
    print("Don't have middle value")
    
##Wap to find the second greatest of 4 values.
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))
d = int(input("Enter number d: "))

if a >= b and a >= c and a >= d:
    if b >= c and b >= d:
        print("Second greatest number is:", b)
    elif c >= b and c >= d:
        print("Second greatest number is:", c)
    else:
        print("Second greatest number is:", d)

elif b >= a and b >= c and b >= d:
    if a >= c and a >= d:
        print("Second greatest number is:", a)
    elif c >= a and c >= d:
        print("Second greatest number is:", c)
    else:
        print("Second greatest number is:", d)

elif c >= a and c >= b and c >= d:
    if a >= b and a >= d:
        print("Second greatest number is:", a)
    elif b >= a and b >= d:
        print("Second greatest number is:", b)
    else:
        print("Second greatest number is:", d)

else:
    if a >= b and a >= c:
        print("Second greatest number is:", a)
    elif b >= a and b >= c:
        print("Second greatest number is:", b)
    else:
        print("Second greatest number is:", c)

##Wap to find the smallest of 4 numbers.
# WAP to find the smallest of 4 numbers using nested if

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))
d = int(input("Enter number d: "))

if a <= b:
    if a <= c:
        if a <= d:
            print("Smallest number is:", a)
        else:
            print("Smallest number is:", d)
    else:
        if c <= d:
            print("Smallest number is:", c)
        else:
            print("Smallest number is:", d)
else:
    if b <= c:
        if b <= d:
            print("Smallest number is:", b)
        else:
            print("Smallest number is:", d)
    else:
        if c <= d:
            print("Smallest number is:", c)
        else:
            print("Smallest number is:", d)

##Write a program to print middle Character of the given string only if it is upper Case Character.
string=input("Enter the string: ")
middle_char=len(string)//2
if len(string)%2 != 0:
    if string[middle_char].isupper():
        print("Middle character of string is",string[middle_char])
    else:
        print("Character is not upper case")
else:
    print("Length of the string is Odd") 
'''
