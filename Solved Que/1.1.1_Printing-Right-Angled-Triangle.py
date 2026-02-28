###Filled Right angle triangle

##Left-Down side
n=5
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()
'''
>>>
*
**
***
****
*****
'''

##Right-Down side
n=5
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(n-i, n):
        print("*", end="")
    print()
'''
>>>
    *
   **
  ***
 ****
*****
'''
##Left-Up side
n=5
for i in range(1, n+1):
    for j in range(n-i+1):
        print("*", end="")
    print()

'''
>>>
*****
****
***
**
*
'''

##Right-Up side
n=5
for i in range(1, n+1):
    for j in range(i-1):
        print(" ", end="")
    for k in range(n-i+1):
        print("*", end="")
    print()

'''
>>>
*****
 ****
  ***
   **
    *
'''

###Hollow right angle triangle

##Left-Down side
n=5
for i in range(1, n+1):
    for j in range(1, i+1):
        if i == 5 or i == j or j == 1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
'''
>>>
*
**
* *
*  *
*****
'''

##Right-Down side
n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == n or j == n or j == n-i+1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

'''
>>>
    *
   **
  * *
 *  *
*****
'''

##Left-Up side
n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or j == 1 or j == n-i+1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

'''
>>>
*****
*  *
* *
**
*
'''

##Right-Up side
n=5
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or j == 5 or i == j:
            print("*", end="")
        else:
            print(" ", end="")
    print()
'''
>>>
*****
 *  *
  * *
   **
    *
'''