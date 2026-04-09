
###Easy For Loop Problems
"""
##1. Write a program to print numbers from 1 to 50 using a for loop.
for i in range(1, 51): #range(start, stop+1, step) - generates numbers from start to stop-1, excluding stop
  print(i, end=' ')
'''
>>>
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50
'''


##2. Print all odd numbers between 1 and 100.
for i in range(1, 101, 2):
    print(i, end=' ')
'''
>>>
 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99 
'''


#alternate approach
for i in range(1, 101):
    if i % 2 != 0:
        print(i, end=' ')
'''
>>>
 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99 
'''


##3. Find the sum of first n natural numbers.
n = 10
sum_natural = 0
for i in range(1, n + 1):
    sum_natural += i
print(sum_natural)
'''
>>>
55
'''


#Withput loop
n = 10
sum_natural = (n * (n + 1)) // 2
print(sum_natural)
'''
>>>
55
'''


##4. Print each character in a string and count total characters.
string4 = 'Mayur Jadhav'
count = 0
for i in string4:
    print(i, end=' ')
print()
print(f"Count of the characters are {count}")
'''
>>>
M a y u r   J a d h a v 
Count of the characters are 0
'''


##5. Find the largest number in a list using a for loop.
list5 = [1, 9, 5, 3, 7]
largest = 0
for i in list5:
    if i > largest:
        largest = i
print(f"The largest number in a list4 is {largest}")
'''
>>>
The largest number in a list4 is 9
'''


##6. Count how many numbers in a list are even.
list6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, False, 'Mayur']
count = 0
for i in list6:
    if type(i) == int and i%2 == 0:
        count += 1
print(f"The count of even number is {count}")
'''
>>>
The count of even number is 5
'''


##7. Print the multiplication table of a given number up to 10.
n = 27
for i in range(1, 11):
    print(f"27 * {i} = {n*i}")
'''
>>>
27 * 1 = 27
27 * 2 = 54
27 * 3 = 81
27 * 4 = 108
27 * 5 = 135
27 * 6 = 162
27 * 7 = 189
27 * 8 = 216
27 * 9 = 243
27 * 10 = 270
'''


##8. Reverse a string without using slicing.
string8 = 'Mayur'
reverse = ''
for i in range(1, len(string8)+1):
    reverse += string8[-i]
print(reverse)
'''
>>>
ruyaM
'''


##9. Count occurrences of a specific character in a string.
string9 = 'Python is programming language'
target = input("Enter one character: ").strip()
if len(target) == 1:
    count = 0
    for i in string9:
        if i == target:
            count += 1
    print(count)
else:
    print("Please enter only one character")
'''
>>>
Enter one character: g
4
'''

"""
##10. Print all elements of a list in reverse order.
list10 = [7, 2, 9, 4, 27]
for i in range(len(list10)-1, -1, -1):
    print(list10[-i], end=' ')
'''
>>>
2 9 4 27 7 
'''

