
##1. Create a map function to find the length of each word in a list of words.
words = ['Amar', 'Hamza', 'Sai', 'Sharakshi']
lengths = list(map(lambda word: len(word), words))
print(lengths)

'''
>>>
[4, 5, 3, 9]
'''

##2. Output should be [(1:1), (2:4), (3:9), (4:16), (5:25)]
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: (x, x**2), numbers))
print(squared)

#2nd method
print(list(map(lambda x: (x, x**2), [1, 2, 3, 4, 5])))
'''
>>>
[(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
[(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
'''

##3. Output should be {1:1, 3:27, 5:125, 7:343}
numbers = [1, 3, 5, 7]
cubed = dict(map(lambda x: (x, x**3), numbers))
print(cubed)
'''
>>>
{1: 1, 3: 27, 5: 125, 7: 343}
'''

##4. Createa map function to print all the factorial values from 1 to 5.
numbers = [1, 2, 3, 4, 5]
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
factorials = list(map(factorial, numbers))
print(list(map(factorial, numbers)))
'''
>>>
[1, 2, 6, 24, 120]
'''

##5. Output should be {1:1, 3:27, 5:3125, 7:823543}
numbers = [1, 3, 5, 7]
cubed = dict(map(lambda x: (x, x**x), numbers))
print(cubed)
'''
>>>
{1: 1, 3: 27, 5: 3125, 7: 823543}
'''

##6. output should be {1:1, 2:2, 3:6, 4:24, 5:120}
numbers = [1, 2, 3, 4, 5]
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(dict(map(lambda x: (x, factorial(x)), numbers)))
'''
>>>
{1: 1, 2: 2, 3: 6, 4: 24, 5: 120}
'''
