'''
                               #### elif Statement ####

num=int(input("Enter the number: "))
if 0<=num<=9:
    print("1 Digit")
elif 10<=num<=99:
    print("2 Digit")
elif 100<=num<=999:
    print("3 Digit")

num=int(input("Enter the number: "))
if 0<=num<=9:
    print("1 Digit")
elif 10<=num<=99:
    print("2 Digit")
else:
    print("More than 3 Digit")
'''
'''
Cj=heck whether a given characyer is upper case, lower case, digit or special symbol.
'''

'''
char=str(input("Enter the character: "))
#upp=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#low=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
if 'A'<=char<='Z':
    print("This character is upper case")
elif 'a'<=char<='z':
    print("This character is lower case")
else:
    print("This character is Digit or Special Symbol")

char=eval(input("Enter the character: "))
if 'A'<=char<='Z':
    print("This character is upper case")
elif 'a'<=char<='z':
    print("This character is lower case")
elif char>=0 or char<=0 or char in ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*","(", ")", "-", "_", "=", "+","[", "]", "{", "}", "\\", "|",";", ":", "'", "\"",",", "<", ".", ">", "/", "?"]:
    print("This character is Digit or Special Symbol")
'''

'''
x=int(input("Enter the x: "))
y=int(input("Enter the y: "))
if x>=0 and y>=0:
    print("Ist Quadrant")
elif x<=0 and y>=0:
    print("IInd Quadrant")
elif x<=0 and y<=0:
    print("IIIrd Quadrant")
elif x>=0 and y<=0:
    print("IVth Quadrant")

x=int(input("Enter the x: "))
y=int(input("Enter the y: "))
if x>=0 and y>=0:
    print("Ist Quadrant")
elif x<=0 and y>=0:
    print("IInd Quadrant")
elif x<=0 and y<=0:
    print("IIIrd Quadrant")
else:
    print("IVth Quadrant")    
'''

'''
Que: To find the greatest of 3 numbers.

num1=int(input("Enter the number 1: "))
num2=int(input("Enter the number 2: "))
num3=int(input("Enter the number 3: "))
if num1 > num2 > num3:
    print("num1 is Greatest")
elif num1 < num2 > num3:
    print("num2 is Greatest")
elif num1 < num2 < num3:
    print("num3 is Greatest")
'''

'''
Que: To find the smallest of 3 numbers.
num1=int(input("Enter the number 1: "))
num2=int(input("Enter the number 2: "))
num3=int(input("Enter the number 3: "))
if num1 < num2 < num3:
    print("num1 is Smallest")
elif num1 > num2 < num3:
    print("num2 is Smallest")
elif num1 > num2 > num3:
    print("num3 is Smallest")
'''

'''
Que:Relation between two integer number.
num1=int(input("Enter the num1: "))
num2=int(input("Enter the num2: "))
if num1 == num2:
    print("num1 is equal to num2")
elif num1 < num2:
    print("num1 is lesser than num2")
elif num1 > num2:
    print("num1 is greate than num2")
'''

'''
Que:Consider a character input if it is uppercase convert it into lowercase, if it is
lowercase convert it into uppercase, if it is digit print the reminder when it is
divided by 3 else if it is special character print it's ASCII value.

char=input("Enter the character: ")
if 'A'<=char<='Z':
    print(chr(ord(char)+32))
elif 'a'<=char<='z':
    print(chr(ord(char)-32))
'''

'''
Que:.Wap to print 'Fizz' if the given number is multiple of three print 'buzz' if the
given number is multiple of 5 and print 'Fizzbuzz' if the number is multiple of
both 3 and 5.

num=int(input("Enter the number: "))
if num%3 == 0 and num%5 ==0:
    print("FizzBuzz")
elif num%5 == 0:
    print("Buzz")
elif num%3 == 0:
    print("Fizz")
'''
