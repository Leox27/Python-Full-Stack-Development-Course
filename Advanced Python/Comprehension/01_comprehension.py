
##1. Write a program to create a list consisting of numbers from 1 to 10.
l1 = [i for i in range(1, 11)]
print(l1)
'''
>>>
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

##2. Write a program to create a list which consist of square of each and every integer of between  the range of 1 to 21 only if it is multiple of 3.
l2 = [x for x in range(1, 22) if x%3 == 0]
print(l2)
'''
>>>
[3, 6, 9, 12, 15, 18, 21]
'''

##3. Wrtie a program to extract string from a list only if it is a palindrome.
l3 = ['Amar', 'mam', 'datta', 'yoy']
output_string = [string for string in l3 if string == string[::-1]]
print(output_string)
'''
>>>
['mam', 'yoy']
'''

##4. Write a progeam to store the square of integer if it is even else store the cube of integer from the range of 1 to 11.
l4 = [x**2 if x%2 == 0 else x**3 for x in range(1, 12)]
print(l4)
'''
>>>
[1, 4, 27, 16, 125, 36, 343, 64, 729, 100, 1331]
'''

##5. string = 'Programs based open comprehension happy'
  #  ['Programs', 'bd', 'open', 'cn', 'hy']
string = 'Programs based open comprehension happy'
l5 = string.split()
out_l = [x if len(x)%2 == 0 else x[0]+x[-1] for x in l5]
print(out_l)
'''
>>>
['Programs', 'bd', 'open', 'cn', 'hy']
'''

##6. Output: [('A1'), ('A2'), ('A3'), ('B1'), ('B2'), ('B3')] using list comprehension.
# l6 = [tuple(letter + str(num)) for letter in ['A', 'B'] for num in range(1, 4)]
l6 = [(letter+num) for letter in 'AB' for num in ['1', '2', '3']]
out_l=[]
for i in l6:
    out_l.append(tuple(i))
print(out_l)
'''
>>>

'''

##7. Program ti find the square root of a number from range 1 to 10
#    ['HEY', 'PYTHON', 'sedoc', 'era', 'INTELLIGENT']
s = 'Hey Python codes are Intelligent'
s_split = s.split()
l7 = {string.upper() if string[0].isupper() else string[::-1] for string in s_split}
print(l7)
'''
>>>
{}'HEY', 'PYTHON', 'sedoc', 'era', 'INTELLIGENT'}
'''
