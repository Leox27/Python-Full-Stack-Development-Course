                                                  #### Unpacking ####

##Unpacking using * which extracts only values from the list
#No. of arguments in the function should be less than or equal to the number of values in the list
lst=[1, 2, 3, 4, 5]
def func(a, b, c, d, e):
    print(a, b, c)
func(*lst)
'''
>>>
1 2 3
'''

##Unpacking using * which extracts only values from the dictionary
#No. of arguments in the function should be less than or equal to the number of values in the dictionary
dct={'a':1, 'b':2}
def func(a, b):
    print(a, b)
func(*dct)
'''
>>>
a b
'''

##Unpacking using ** which extracts only values from the dictionary
#No. of arguments in the function should be less than or equal to the number of values in the dictionary
dct={'a':1, 'b':2}
def func(a, b):
    print(a, b)
func(**dct)
'''
>>>
1 2
'''
