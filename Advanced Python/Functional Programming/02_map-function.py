###map()

'''
#syntax:
map(function, collection)
'''

#with lambda function
a = [1,2,3,4,5]
b = map(lambda x: x**2, a)
print(list(b))

'''
>>>
[1, 4, 9, 16, 25]
'''

#with condition
a = [1,2,3,4,5]
b = list(map(lambda x:'Even' if x%2==0 else 'Odd', a))
print(b)

'''
>>>
['Odd', 'Even', 'Odd', 'Even', 'Odd']
'''

#with function
a = [1,2,3,4,5]
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(list(map(factorial, a)))

'''
>>>
[1, 2, 6, 24, 120]
'''

#with multiple collections
a = [1,2,3]
b = [4,5,6]
c = (map(lambda x, y: x + y, a, b))
print(list(c))

'''
>>>
[5, 7, 9]
'''

#with multiple collections and different lengths
a = [1,2,3]
b = [4,5,6,7,8]
c = (map(lambda x, y: x + y, a, b))
print(list(c))

'''
When the collections have different lengths, the map function will stop when the shortest collection is exhausted. In this case, since 'a' has 3 elements and 'b' has 5 elements, the map function will only iterate 3 times, resulting in:
>>>
[5, 7, 9]
'''
