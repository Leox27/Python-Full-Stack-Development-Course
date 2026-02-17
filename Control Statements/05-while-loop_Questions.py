'''
                            #### while loop ####
##WAP tp print n natural numbers.

num=int(input("Enter the number: "))
i=1
while num<=10:
    print(num)
    num += 1

    
i=1
num=int(input("Enter the number: "))
while i<=10:
    print(num*i)
    i += 1

#WAp to find the sum of natural numbers.

i=1
total_sum=0
while i<=5:
    n=int(input("Enter the natural number: "))
    total_sum+=n
    i += 1
print(total_sum)

#WAp to find the product of n natural numbers or factorial of a number
i=1
factorial=1
n=int(input("Enter the natural number: "))
while i<=n:
    factorial*=i
    i += 1
print(factorial)

#WAP all the characters in the string.
i=0
char=input("Enter the string: ")
while i<len(char):
    print("String:", char[i])
    i += 1

#WAP to print all the characters present at even index of a string.
i=0
char=input("Enter the string: ")
while i<len(char):
    if i == 0 or i%2 == 0: 
        print("String:", char[i])
    i += 1

or
i=0
char=input("Enter the string: ")
while i<len(char):
    even_index=char[i]
    print("String:", char[i])
    i += 1 

#WAp to extract all the lowercase character present ina string.
i=0
string=input("Enter the string: ")
while i<len(string):
    low=string[i]
    #if 'a'<=string[i]<='z':
    if low.islower():
        print("String:",string[i])
    i += 1

#WAP to extract all the vowels present in the string.
string=input("Enter the string: ")
i=0
#vowels=['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
vowels = 'AEIOUaeiou'
while i<len(string):
    if string[i] in vowels:
        print("Vowel:",string[i])
    i += 1

##WAP to print the place values of a integer number.
num=int(input("Enter the number: "))
s=str(num)
l=len(str(num))
i=0
while i<len(str(num)):
    a=s[i]
    op=a+'0'*(l-i-1)
    final=int(op)
    print("Here the factor for",i+1, final)
    i += 1

##WAP to print the factors of a integer number.
num=int(input("Enter the number: "))
i=1
while i<=num:
    if num%i == 0:
        print(i)
    i += 1

##WAP to toggle a string
string=input("Enter the string: ")
i=0
toggle=''
while i<len(string):
    if 'A'<=string[i]<='Z':
        toggle += chr(ord(string[i])+32)
    elif 'a'<=string[i]<='z':
        toggle += chr(ord(string[i])-32)
    else:
        toggle += string[i]
    i += 1
print("String is toggled: ", toggle)

##WAP to reverse given number.
num=int(input("Enter the number: "))
string=str(num)
i=0
while i<len(string):
    rev=string[::-1]
    reverse=int(rev)
    i += 1
print(reverse, end="")


n = int(input("Enter the number: "))
rev = 0
while 0<n:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print("Reversed number:", rev)

##WAP to find the sum of individual digits of a number.
num=int(input("Enter the number: "))
summ=0
while 0<num:
    digit = num%10
    summ += digit
    num //= 10
print(summ)

#WAP to check whether the number is perfect or not.
num=int(input("Enter the number: "))
i=1
summ = 0
while i<num:
    if num%i == 0:
        summ = summ+i 
    i += 1
if summ == num:
    print(summ,"is Perfect number")
else:
    print(summ,"is not perfect number")
'''
'''
#WAP to login to phonepe by entering correct otp.
#################do it again
OTP='1299'
otp=""
while OTP!=otp:
    otp=str(input("Enter the OTP: "))
    if otp == OTP:
        #print("Checking...")
       
        print("Login Successful")  
print("wrong otp")

otp=str(input("Enter the OTP: "))
OTP='1299'
i=0
while i<len(otp):
    if otp[i] == OTP[i]:
        i += 1
        print("Login Successful")
    else:        
        print("Entered correct OTP")

##WAP to run infinite loop until user enters the correct password.
correct_pass = "Mayur123"
while True:
    password = input("Enter password: ")
    if password == correct_pass:
        print("Entered password is correct")
        break
    else:
        print("Wrong password, try again")
'''
'''
##WAP to extract all the even integers present in a tuple at odd index.
tup=tuple([input("Enter the tuple:")])
i = 1
l=[]
while i<len(tup):
    if i%2 != 0:
        if type(tup[i]) == int:
            if tup[i]%2 == 0:
                l.append(tup[i])
    i += 2
print(l)

##WAP to remove duplicates from a list without converting inro set.
lst=eval(input("Enter the list: "))
i=0
lst2=[]
while i<len(lst)-1:
    if lst[i] not in lst2:
        lst2.append(lst[i])
    i += 1
print("Original list",lst)
print("Removed duplicated list",lst2)

##WAP to find the sum of all the odd numbers between the given range.
lst=eval(input("Enter the list: "))
i=0
summ=0
while i<len(lst)-1:
    if lst[i]%2 != 0:
        summ += lst[i]
    i += 2
print("Summ of all the odd number is:",summ)

##WAP to find the greatest number in a given list of integers.
lst=eval(input("Enter the list: "))
i=0
greatest_num=lst[0]
while i<len(lst)-1:
    if lst[i]> greatest_num:
        greatest_num = lst[i]
    i += 1
print("Greatest number in list of integers is:",greatest_num)

##WAp to find the sum of cube of a number is a string.
string=input("Enter the number of string:")
i=0
summ=0
while i<len(string):
    integer=int(string[i])
    if type(integer) == int:
        summ += integer**3
    i += 1
print("The sum of cune of numbers is:",summ)

##WAP to check whether the number is ArmStrong or not.
num=int(input("Enter the number of string:"))
i=0
summ=0
str_num=str(num)
digit=len(str_num)
while i<len(str_num):
    int_num=int(str_num[i])
    summ += int_num**digit
    i += 1
if summ == num:
    print("The given number is ArmStrong and the sum is",summ)
else:
    print("Number is not ArmStrong")
'''
        


























