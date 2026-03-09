#Task: create relational class with magic methods related to relational operators
class Relational:
    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        return self.x < other.x

    def __gt__(self, other):
        return self.x > other.x

    def __le__(self, other):
        return self.x <= other.x

    def __ge__(self, other):
        return self.x >= other.x

    def __eq__(self, other):
        return self.x == other.x

ob1 = Relational(10)
ob2 = Relational(20)

print(ob1 < ob2)
print(ob1 > ob2)
print(ob1 <= ob2)
print(ob1 >= ob2)
print(ob1 == ob2)

'''
>>>
True
False
True
False
False
'''