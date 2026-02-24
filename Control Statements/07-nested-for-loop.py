'''
                       #### nested for ####
(i,j)

(1,1) (1,2) (1,3) (1,4) (1,5)
(2,1) (2,2) (2,3) (2,4) (2,5)
(3,1) (3,2) (3,3) (3,4) (3,5)
(4,1) (4,2) (4,3) (4,4) (4,5)
(5,1) (5,2) (5,3) (5,4) (5,5)

##
for i in range(1, 6):
    for j in range(1, 6):
        print(i, '-', j)

##
m=['mango', 'apple', 'orange', 'grape', 'watermelon', 'strawberry']
n=['yellow', 'red', 'orange', 'green', 'dark-green', 'reddish']
for i in m:
    for j in n:
        print(i, '-', j)

##1.Tables
for i in range(1, 6):
    print(end="\n")
    for j in range(1, 6):
        print(i*j, end="\t")
1	2	3	4	5	
2	4	6	8	10	
3	6	9	12	15	
4	8	12	16	20	
5	10	15	20	25


##2. Print '*'.
for i in range(1, 6):
    print(end="\n")
    for j in range(1, 6):
        print("*")
*****
*****
*****
*****
*****


##3. print hollow square.
for i in range(1, 6):
    print()
    for j in range(1, 6):
        if i == 1 or i == 5 or j == 1 or j == 5:
            print('*', end="")
        else:
            print(' ', end="")
*****
*   *
*   *
*   *
*****


##4. print left side triangle.
for i in range(1, 6):
    for j in range(1, 6):
        if i == 1:
            print(j*'*', end="")
        print()                 #for next line
    break
*
**
***
****
*****


##5. print hollow left side triangle.
for i in range(1, 6):
    for j in range(1, 6):
        if i == j or j == 1 or i == 5:
            print('*', end="")
        else:
            print(' ', end="")
    print()
*    
**   
* *  
*  * 
*****


##5. print hollow right side triangle.
for i in range(1, 6):
    for j in range(1, 6):
        if i + j == 6 or j == 5 or i == 5:
            print('*', end="")
        else:
            print(' ', end="")
    print()
    *
   **
  * *
 *  *
*****


##6. print plus sign.
for i in range(1, 6):
    for j in range(1, 6):
        if i == 3 or j == 3:
            print('*', end="")
        else:
            print(' ', end="")
    print()


##7. print % sign.
for i in range(1, 7):
    for j in range(1, 7):
        if i + j == 7 or (i==2 and j==2) or (i==5 and j == 5):
            print("*", end="")
        else:
            print(" ", end="")
    print()


##8. print # sign.
for i in range(1, 9):
    for j in range(1, 9):
        if j == 3 or j == 6 or i == 3 or i == 6 or (i == 4 and j == 4):
            print("#", end="")
        else:
            print(" ", end="")
    print()
  #  #  
  #  #  
########
  #  #  
  #  #  
########
  #  #  
  #  #
  

##9. print into sign.
for i in range(1, 6):
    for j in range(1, 6):
        if i == j or i+j==6 :
            print("*", end="")
        else:
            print(" ", end="")
    print()
*   *
 * * 
  *  
 * * 
*   *
'''

##10. butterfly
n = 4

# Top half
for i in range(1, n + 1):
    # Left stars
    for j in range(1, i + 1):
        print("*", end="")
    
    # Spaces
    for j in range(1, 2 * (n - i) + 1):
        print(" ", end="")
    
    # Right stars
    for j in range(1, i + 1):
        print("*", end="")
    
    print()

# Bottom half
for i in range(n, 0, -1):
    # Left stars
    for j in range(1, i + 1):
        print("*", end="")
    
    # Spaces
    for j in range(1, 2 * (n - i) + 1):
        print(" ", end="")
    
    # Right stars
    for j in range(1, i + 1):
        print("*", end="")
    
    print()


































