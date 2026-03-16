###Dictionary Comprehansion
'''
#syntax
{key:value for key, value in collection if condition}
{key:value for key, value in zip(collection1, collection2) if condition}
{key:value1 if condition else value2 for key, value in zip(collection1, collection2)}
'''

##1. {{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}}
dictionary = {i:i**2 for i in range(1, 6)}
print(dictionary)
'''
>>>
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''

##2. {'Sam': 3, 'are': 3, 'you': 3}
string = 'Hello Sam are you fine'
split_string=string.split()
dict2 = {i:3 for i in split_string if len(i)==3}
print(dict2)
'''
>>>
{'Sam': 3, 'are': 3, 'you': 3}
'''

##3. {'Sam': 45, 'Sai': 75, 'Sujay': 32, 'Sanjay': 93}
l1 = ['Sam', 'Sai', 'Sujay', 'Sanjay']
l2 = [45, 75, 32, 93]
dict3 = {i:j for i, j in zip(l1, l2)}
print(dict3)
'''
>>>
{'Sam': 45, 'Sai': 75, 'Sujay': 32, 'Sanjay': 93}
'''

##4.  WAP to create a dictionary which consist of name as key and value as 'Pass' if marks is greater than or equal to 50 else 'Fail' using dictionary comprehension.
l1 = ['Sam', 'Sai', 'Sujay', 'Sanjay']
l2 = [45, 75, 32, 93]
dict4 = {i:'Pass' if j>=50 else 'Fail' for i, j in zip(l1, l2)}
print(dict4)
'''
>>>
{'Sam': 'Fail', 'Sai': 'Pass', 'Sujay': 'Fail', 'Sanjay': 'Pass'}
'''

