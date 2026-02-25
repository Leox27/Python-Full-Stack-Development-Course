                                                          #### Packing ####
##Single packing or Tuple Packing
def num(*a):
    print(a)
    print(type(a))
num(1,2,3,4)
'''
>>>
(1, 2, 3, 4)
<class 'tuple'>
'''

##Double Packing or Dictionary Packing
def num(**a):
    print(a)
    print(type(a))
num(a=2, b=3)
'''
>>>
{'a': 2, 'b': 3}
<class 'dict'>
'''
