
###Medium For Loop Problems

##1. Find factorial of a number using a for loop.
n = 0
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(factorial)
'''
>>>
1
'''


##2. Check whether a number is prime.
n = 7
if n > 1:
    for i in range(2, n):
        if n%i == 0:
            print(f"{n} is not a Prime number")
            break
    else:
        print(f"{n} is a Prime number")
else:
    print("Number should be greater than 1")      
'''
>>>
7 is a Prime number
'''


##3. Count vowels and consonants in a string.
string3 = 'vowels and consonants'
vowels_count = 0
consonants_count = 0
for i in string3:
    if i in 'aeiuoAEIUO':
        vowels_count += 1
    #elif i.isalpha() and i not in 'aeiouAEIOU':
    elif i in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz': 
        consonants_count += 1
print(f"Coount of vowels: {vowels_count} & Count of consonants: {consonants_count}")
'''
>>>
Coount of vowels: 6 & Count of consonants: 13
'''


##4. Find the second largest element in a list.
list4 = [4, 6, 3, 7, 1, 8]
largest = 0
second_largest = 0
if len(list4) < 2:
    print("list should contain more than two elements")
else:
    for i in list4:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest:
            second_largest = i
    print(second_largest)
'''
>>>
7
'''


##5. Remove duplicates from a list using loops.
list5 = [1, 2, 3, 1, 2, 3, 4, 4, 4, 7]
seen = set()
output_list = []
for i in list5:
    if i not in output_list:
        output_list.append(i)
        seen.add(i)
print(output_list)
'''
>>>
[1, 2, 3, 4, 7]
'''


##6. Print Fibonacci sequence up to n terms.
n = 10
first, second = 0, 1
for i in range(n):
    print(first, end=' ')
    first, second = second, first + second
'''
>>>
0 1 1 2 3 5 8 13 21 34
'''


##7. Find common elements between two lists.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 7]
list2 = [1, 3, 10, 5, 27, 7, 9]
common = []
for i in list1:
    if i in list2 and i not in common:
        common.append(i)
print(common)
'''
>>>
[1, 3, 5, 7, 9]
'''

#
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 7]
list2 = [1, 3, 10, 5, 27, 7, 9]
common = list(set(list1) & set(list2))
print(common)
'''
>>>
[1, 3, 5, 7, 9]
'''
'''
set1 | set2   # union
set1 - set2   # difference
set1 & set2   # intersection
'''


##8. Check if a string is palindrome using loop logic.
string8 = input("Enter string: ").strip()
palindrome = ''
for i in range(len(string8)-1, -1, -1):
    palindrome += string8[i]
if string8 == palindrome:
    print("String is palindrome")
else:
    print("String is not palindrome")
'''
>>>
Enter string: mn
String is not palindrome
'''

#
string8 = input("Enter string: ").strip()
palindrome = True
for i in range(len(string8)//2):
    if string8[i] != string8[-(i+1)]:
        palindrome = False
        break
print("Palindrome" if palindrome else "Not palindrome")


##9. Create a star triangle pattern:
# *
# **
# ***
# ****
# *****
n = 5
for i in range(n):
    print()
    for j in range(i+1):
        print('*', end='')
'''
>>>
*
**
***
****
*****
'''

#
n = 5
for i in range(1, n+1):
    print('*'*i)


##10. Find the sum of digits of a number.
n = 12345
sum_dig = 0
for i in str(n):
    sum_dig += int(i)
print(sum_dig)
'''
>>>
5
'''

