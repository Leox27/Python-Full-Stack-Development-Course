#Task: create relational class with magic methods related to relational operators
class Relational:
    def __init__(self, a):
        self.a=a
    
    def __equalto__(self, other):
        self.a == other.a

    def __notequalto__(self, other):
        self.a != other.a

    def __lessthan__(self, other):
        self.a < other.a

    def __greaterthan__(self, other):
        self.a > other.a

    def __lessthanorequalto__(self, other):
        self.a <= other.a
    
    def __greaterthanorequalto__(self, other):
        self.a >= other.a

ob1 = Relational(10)
ob2 = Relational(20)

print(ob1==ob2)
print(ob1!=ob2)

'''
>>>
False
True
'''