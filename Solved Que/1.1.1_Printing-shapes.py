##Diamond

n=5
#Upper side
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()

#Lower side
for i in range(2, n+1):
    for j in range(1, i):
        print(" ", end="")
    for k in range(2*(n-i)+1):
        print("*", end="")
    print()
    
'''
>>>
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

#2nd method optimized

n = 5
#Upper side
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))

#Lower side
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "*"*(2*i-1)) 

'''
>>>
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
