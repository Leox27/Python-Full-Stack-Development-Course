'''
                                   #### if-else ####
n=int(input("Enter the number: "))
if n%2==0:
    print("Even")
else:
    print("Odd")

n=eval(input("Enter the number: "))
if type(n) == list or type(n) == set or type(n)== dict:
    print("Mutable")
else:
    print("Immumatable")

char=input("Enter the number: ")
if '0'<=char<='9':
    print("It is a Digit")
else:
    print("It is not a Digit")

char=input("Enter the number: ")
if '0'<=char<='9' or 'A'<=char<='Z' or 'a'<=char<='z':
    print("It is not a special Symbol")
else:
    print("It is a special Symbol")

lst=eval(input("Enter the collection: "))
if len(lst)%2 == 0:
    print("Not consist middle value")
else:
    print("Consist middle value")

val1=eval(input("Enter 1st value: "))
val2=eval(input("Enter 2st value: "))
if val1 is not val2:
    print("Address is different")
else:
    print("Address is Same")

tp1=eval(input("Enter the values: "))
if type(tp1[0]) == type(tp1[1]): 
    print("Homogeneous")
else:
    print("Not Homogeneous")

string=input("Enter the String: ")
if string[len(string)::-1] == string[::]:
    print("Palindrome")
else:
    print("Not palindrome")

num=int(input("Enter the number: "))
if num>0:
    print("Positive")
else:
    print("Negative"
'''
