
###filter()

'''
#syntax:
filter(function, collection)
'''
##Practice Questions

#1. from the list of integers filter the -ve numbers and convert them to +ve using map
l = [1, 2, 3, 4]
def make_positive(n):
    if n<0:
        return -n
    else:
        return n
print(list(map(make_positive, l)))
'''
>>>
[1, 2, 3, 4]
'''

#2. filter only strings whose length is greater than 4
l1 = ['Datta', 'Kashinath', 'Trimbak', 'Amar', 'Mayur']
def len4(l1):
    return l1
print(list(filter(lambda x: len(len4(x))>4, l1)))
'''
>>>
['Datta', 'Kashinath', 'Trimbak', 'Mayur']
'''

#1. take 1 input list i using filter keep only numbers divisible by 5 
numbers = [10, 15, 22, 30, 42, 50]
def divisible_by_5(n):
    return n%5==0
print(list(filter(divisible_by_5, numbers)))
'''
>>>
[10, 15, 30, 50]
'''

#2. take 1 list of strings keep only strings that start with vowel
l2 = ['Datta', 'Kashinath', 'Trimbak', 'Amar', 'Mayur']
def start_vowel(n):
    vowels = 'AEIOUaeiou'
    if n[0] in vowels:
        return n
    else: return None
print(list(filter(start_vowel, l2)))
'''
>>>
['Amar']
'''

#3. keep only palindromes from the list
l3 = ['Datta', 'Kashinath', 'mam', 'Trimbak', 'dad', 'Amar', 'Mayur']
def palindrome(n):
    if n == n[::-1]:
        return n 
    else:
        return None
print(list(filter(palindrome, l3)))
'''
>>>
['mam', 'dad']
'''

#4. keep only words that contain letter 'a' 
l4 = ['Datta', 'Kashinath', 'mam', 'Trimbak', 'dad', 'Amar', 'Mayur', 'Lion']
def contain_a(n):
    if 'a' in n:
        return n
    else:
        return None
print(list(filter(contain_a, l4)))
'''
>>>
['Datta', 'Kashinath', 'mam', 'Trimbak', 'dad', 'Amar', 'Mayur']
'''

#5. keep only prime numbers from list 1 to 100
l5 = [i for i in range(1, 101)]
def prime(n):
    if n < 2:
        return None
    for i in range(2, n):
        if n%i == 0:
            return None
    return n
print(list(filter(prime, l5)))
'''
>>>
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
'''

#6. keep only numbers 50 and 100 inclused from list of 1 to 100
l6 = [i for i in range(1, 101)]
def keep_50_100(n):
    if n == 50 or n == 100:
        return n
    else:
        return None
print(list(filter(keep_50_100, l6)))
'''
>>>
[50, 100]
'''

