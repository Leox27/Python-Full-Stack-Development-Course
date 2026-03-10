###Lambda Function

##with expression
'''
syntax:
lambda arguments: expression
'''
a = lambda n:n%2==0
print(a(2))
'''
>>>
True
'''

##1. with condition

#with if condion
'''
syntax:
lambda arguments: expression if condition
'''
a = lambda n: n%2==0
print(a(11))

#with if -else condition
'''
syntax:
lambda arguments: expression if condition else expression
'''
a = lambda n: 'Even' if n%2==0 else 'Odd'
print(a(11))

