'''
                                      #### if ####
vowels='aeiouAEIOU'
n=str(input())
if n in vowels:
    print("vowels")

n=int(input())
if (n**2)%2 == 0:
    print("Even")
    
c=input("Enter the character: ")
if 'A'<=c<='Z':
    print(ord(c))

n=int(input("Enter the number: "))
if n%9 == 0 or n == 0:
    print("Divisible", n**3)

n=int(input("Enter the number: "))
if 100<=n<=999:
    print("Three digit")

n=int(input("Enter the number: "))
if n%10 == 5:
    num=int(n)
    print("Entered number is:",num,"Last digit is 5","and the type of data is:",type(num))

n=eval(input("Enter the number: "))
if type(n) == float:
    print("Float")

n=eval(input("Enter the number: "))
if type(n) == int or type(n) == float or type(n) == complex:
    print("Single Value Data")


n=str(input("Enter the number: "))
char='0123456789'
if n in char:
    print("Digit")

n=int(input("Enter the number: "))
if n%3 == 0:
    print("Multiple of 3")
    
'''
