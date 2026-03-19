###Generators

##1. WAP to extract all tje string from tje list only if it is palindrome
def extract(l):
    for i in l:
        if type(i) == str and i == i[::-1]:
            yield i
print(list(extract(['mam', 'Boomer', 'Trimbak', 'leooel'])))
'''
>>>
['mam', 'leooel']
'''

##2. {'A':65, 'B':66, ....., 'Z':96}

def ascii_value():
    for val in range(65, 91):
        yield chr(val), val
print(dict(ascii_value()))
'''
>>>
{'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90}
'''

##3. I/P: 'GenERat@rZ'
    #O/P: {'G':'g', 'e':'E',.....,'@':'@', 'r':'R', 'Z':'z'}
s = 'GenERat@rZ'
def swap(s):
    for i in s:
        if 'A'<=i<='Z':
            yield i, chr(ord(i)+32)
        elif 'a'<=i<='z':
            yield i, chr(ord(i)-32)
        else:
            yield i, i
print(dict(swap(s)))
'''
>>>
{'G': 'g', 'e': 'E', 'n': 'N', 'E': 'e', 'R': 'r', 'a': 'A', 't': 'T', '@': '@', 'r': 'R', 'Z': 'z'}
'''

##4.
def cube():
    for i in range(1, 11):
        yield i, i**3
print(dict(cube()))
'''
>>>
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}
'''

##5. WAP to print square of numbers from 1 to 10 by using yield
def square():
    for i in range(1, 11):
        yield i**2
print(list(square()))
'''
>>>
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''


