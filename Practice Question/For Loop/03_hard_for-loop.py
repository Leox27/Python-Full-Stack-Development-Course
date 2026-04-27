
###Hard For Loop Problems
"""
##1. Find all prime numbers in a given range.
n = 50
if n > 1:
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, i):
            if i%j == 0:
                is_prime = False
                break
        if is_prime:
            print(i, end=' ')
'''
>>>
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
'''


##2. Print Floyd’s Triangle using nested for loops.
n = 5
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end='\t')
        num += 1
    print()
'''
>>>
1
2       3
4       5       6
7       8       9       10
11      12      13      14      15
'''


##3. Find duplicate elements and their counts in a list.
list3 = [1, 2, 2, 3, 4, 2, 5, 1, 3, 7, 8, 8, 1]
duplicates = {}

for j in list3:
    if j not in duplicates:
        duplicates[j] = 1
    else:
        val = duplicates[j]
        duplicates[j] = val+1
result = {}
for key, val in duplicates.items():
    if val > 1:
        result[key] = val
print(result)
'''
>>>
{1: 3, 2: 3, 3: 2, 8: 2}
'''


##4. Print Pascal’s Triangle.
n = 5
for i in range(n):
    num = 1
    for j in range(n-i-1):
        print(' ', end='')
    for k in range(i+1):
        print(num, end=' ')
        num = num * (i-k)//(k+1)
    print()
'''
>>>
    1 
   1 1 
  1 2 1 
 1 3 3 1 
1 4 6 4 1 
'''


##5. Find missing number in a sequence from 1 to n.
list7 = [1,2,3,4,5,6,8,9,10]
for i in range(1, len(list7)+2):
    if i not in list7:
        print(i)
'''
>>>
7
'''


##6. Find second smallest and second largest in one traversal.
n = 12348765
largest = 0
second_largest = 0
smallest = 9
second_smallest = 9
for i in range(1, len(str(n))+1):
    digit = n % 10
    if digit > largest:
        second_largest = largest
        largest = digit
    elif digit > second_largest and digit != largest:
        second_largest = digit

    if digit < smallest:
        second_smallest = smallest
        smallest = digit
    elif digit < second_smallest and digit != smallest:
        second_smallest = digit
    n //= 10
print(f"The second_smallest is {second_smallest}")
print(f"The second_largest is {second_largest}")
'''
>>>
The second_smallest is 2
The second_largest is 7
'''


##7. Check if two strings are anagrams using loops.
string1 = input('Enter string1: ')
string2 = input('Enter string2: ')
if len(string1) != len(string2):
    print('Length of both string should be same')
else:
    freq1 = {}
    freq2 = {}
    for i in string1:
        if i not in freq1:
            freq1[i] = 1
        else:
            val = freq1[i]
            freq1[i] = val+1
    for j in string2:
        if j not in freq2:
            freq2[j] = 1
        else:
            val = freq2[j]
            freq2[j] = val+1
    if freq1 == freq2:
        print('It;s Anagram')
    else:
        print('Its not Anagram')
    print(freq1)
    print(freq2)
'''
>>>
Enter string1: silent
Enter string2: listen
It;s Anagram
{'s': 1, 'i': 1, 'l': 1, 'e': 1, 'n': 1, 't': 1}
{'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1}
'''

#2nd method
string1 = input('Enter string1: ')
string2 = input('Enter string2: ')
if len(string1) != len(string2):
    print('Not Anagram')
else:
    freq = {}
    for ch in string1:
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] += 1
    for ch in string2:
        if ch not in string2:
            print('Its not Anagram')
            break
        freq[ch] -= 1
        if freq[ch] < 0:
            print('Its not Anagram')
            break
    else:
        print('Anagram')
'''
>>>
Enter string1: silent
Enter string2: listee
Its not Anagram
'''

##8. Print pyramid pattern:
#     *
#    ***
#   *****
#  *******
# *********

n = 9
for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(' ', end='')
    for k in range(1, 2*i):
        print('*', end='')
    print()

# 2nd method
n=5
for i in range(1, n+1):
    print(' '*(n-i) + '*'*(2*i-1))
"""

##9. Generate multiplication matrix table using nested loops.
n = 5
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i*j, end='\t')
        # print(f"{i*j:3}", end=' ') #we can indicate no. of spaces(n) - {i*j:n}
    print()
'''
>>>
1       2       3       4       5
2       4       6       8       10
3       6       9       12      15
4       8       12      16      20
5       10      15      20      25
'''


##10. Solve the “Armstrong number” problem for a range.
n = 153
degree = len(str(n))
sum_digits = 0
for i in str(n):
    sum_digits += int(i)**degree
if sum_digits == n:
    print('Given number is Armstrong')
else:
    print('Given number is not Armstrong')
'''
>>>
Given number is Armstrong
'''

# 2nd method without string
n = 153
temp = n
degree = len(str(n))
sum_digits = 0
for i in range(degree):
    digit = temp % 10
    sum_digits += digit**degree
    temp //= 10
if sum_digits == n:
    print('Given number is Armstrong')
else:
    print('Given number is not Armstrong')
'''
>>>
Given number is Armstrong
'''
