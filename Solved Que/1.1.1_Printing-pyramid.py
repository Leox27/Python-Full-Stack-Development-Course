##Pyramid print
n=5
for i in range(1,n+1): #7 rows
    for j in range(n-i): #spaces
        print(" ", end="")
    for k in range(2*i-1): #'*' print
        print("*", end="")
    print()

'''
>>>
    *
   ***
  *****
 *******
*********
'''

##Reverse Pyramid print
n=5
for i in range(1, n+1):
    for j in range(i-1):
        print(" ", end="")
    for k in range(2*(n-i)+1):
        print("*", end="")
    print()

'''
>>>
*********
 *******
  *****
   ***
    *
'''

##Inceasing Pyramid from left to right
# n = 5
# #Upper half
for i in range(1, n+1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

#Lower half
for i in range(1, n):
    for j in range(i):
        print(" ", end="")
    for k in range(n - i):
        print("*", end="")
    print()

'''
>>>
    *
   **
  ***
 ****
*****
 ****
  ***
   **
    *

'''

##Decreasing Pyramid from left to right
n = 5
#Upper half
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    for k in range(1, n+1):
        print(" ", end="")
    print()

#Lower half
for i in range(1, n+1):
    for j in range(n-i):
        print("*", end="")
    for k in range(2*(n-i)-1):
        print(" ", end="")
    print()

'''
>>>
*
**
***
****
*****
****
***
**
*
'''