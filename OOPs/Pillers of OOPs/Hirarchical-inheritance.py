###Hirarchical Inheritance

class A: #Parent
    a=10
    b=20

class B(A): #Child of class-A
    c=30
    d=40
    def __init__(self, e, f):
        self.e=e
        self.f=f

class C(A): #Child of class-A
    s=50
    t=60

ob1=B(111, 222)
print(ob1.a, ob1.b, ob1.c, ob1.d, ob1.e, ob1.f)

ob2=C()
print(ob2.a, ob2.b, ob2.s, ob2.t)
'''
>>>
10 20 30 40 111 222
10 20 50 60
'''

'''
Note:
Single child class cannot access other child properties/members/functionalities.
Single child class access only parent class properties/members/functionalities.
'''