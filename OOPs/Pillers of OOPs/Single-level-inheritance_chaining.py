                                            #### Single-level Inheritance - Chaining ####
###Single-level Inheritance Chaining
class A:
    a=100
    b=200
    
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def ex(self): #For class A
        print("Today is Monday")

class B(A):
    p=111
    q=222
    
    def __init__(self, m, n, o):
        super().__init__(m, n)
        self.o=o

    def ex1(self): #For class B
        super().ex() #From class A
        print("Today I am feeling very bored")
        
Obj1=B(1, 2, 3)
Obj1.ex1()

'''
>>>
Today is Monday
Today I am feeling very bored
'''

###Multi-level Inheritance Chaining
class A:
    a=100
    b=200
    
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def ex(self): #For class A
        print("Today is Monday")

class B(A):
    p=111
    q=222
    
    def __init__(self, m, n, o):
        super().__init__(m, n)
        self.o=o

    def ex1(self): #For class B
        #super().ex() #From class A
        print("Today I am feeling very bored")

class C(B):
    name="Abhishek"
    
    def ex2(self): #For class C
        super().ex() #From class A
        super().ex1() #From class B
        print("Tomorrow i will be in Energy")
        
Obj2=C(4, 5, 6)
Obj2.ex2()

'''
>>>
Today is Monday
Today I am feeling very bored
Tomorrow i will be in Energy
'''







