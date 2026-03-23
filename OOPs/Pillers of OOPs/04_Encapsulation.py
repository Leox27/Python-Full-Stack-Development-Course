###Encapsulation

##Public 
class A:
    def __init__(self, a):
        self.a= a

obj1 = A(10)

print(obj1.a)
'''
>>>
10
'''

##Protected 
class A:
    def __init__(self, a, b):
        self.a= a
        self._b=b # using '_'

obj1 = A(10, 20)

print(obj1.a, obj1._b)
'''
>>>
10 20
'''

##Private
'''
We can not access private members outside the class. We can access private members using getter and setter methods or using property decorator.
'''
class A:
    def __init__(self, a, b,c):
        self.a= a
        self._b=b
        self.__c=c

    # getter & setter
    #getter
    def gett(self): #access
        return self.__c
    
    #setter
    def sett(self, n): #modify
        self.__c=n

    #property
    @property #access
    def gettt(self):
        return self.__c
    
    @gettt.setter #modify (using ''setter'' keyword)
    def gettt(self, n):
        self.__c=n

obj1 = A(10, 20, 30)

# print(obj1.a, obj1._b, obj1.__c) #cannot access __c which is private attribute
# '''
# >>>
#     print(obj1.a, obj1._b, obj1.__c)
#                            ^^^^^^^^
# AttributeError: 'A' object has no attribute '__c'
# '''

# accessing private attribute using getter method
print(obj1.gett()) #accessing private attribute using getter method
'''
>>>
30
'''

# modifying private attribute using setter method
obj1.sett(1027) #value modified of __c: 10->1027
print(obj1.gett())
'''
1027
'''

# using property decorator
print(obj1.gettt) #accessing private attribute using property decorator
obj1.gettt= 2024 #modifying private attribute using property decorator
print(obj1.gettt)
'''
>>>
1027
2024 #value modified of __c: 1027->2024
'''

# mangling of private members
print(obj1._A__c) #accessing private attribute using name mangling
'''
>>>
2024
'''