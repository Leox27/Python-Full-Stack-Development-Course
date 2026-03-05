### Multiple Inheritance

#Multiple parents followed by Single child
class A:
    a=10
    b=20
class B:
    c=30
    d=40
class c(A, B):
    def __init__(self, e, f):
        self.e=e
        self.f=f
obj=c(50, 60)
print(obj.a, obj.b, obj.c, obj.d, obj.e, obj.f)

'''
>>>
10 20 30 40 50 60
'''