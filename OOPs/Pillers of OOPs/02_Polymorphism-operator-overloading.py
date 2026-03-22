### operator overloading

class Arithmetic:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a
    
    def __sub__(self, other):
        return self.a - other.a
    
    def __mul__(self, other):
        return self.a * other.a
    
    def __truediv__(self, other):
        return self.a / other.a
    
    def __floordiv__(self, other):
        return self.a // other.a
    
    def __mod__(self, other):
        return self.a % other.a
    
num1 = Arithmetic(int(input("Enter a number: ")))
num2 = Arithmetic(int(input("Enter other number: ")))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)

'''
>>>
Enter a number: 10
Enter other number: 27
37
-17
270
0.37037037037037035
0
10
'''

#
'''
In the above code, we have defined the __add__ method in the class A to overload the '+' operator. When we use the '+' operator with the objects of class A, it will call the __add__ method and return the sum of the two numbers.
'''

class A:
    def __init__(self, a):
        self.a = a
    def __add__(self, other):
        return self.a+other.a
    
obj1 = A(10)
obj2 = A(20)
print(obj1+obj2)
'''
>>>
30
'''

'''
In the above code, we have defined the __add__ method to return an object of class A. We have also defined the __str__ method to return the string representation of the object. When we use the '+' operator with the objects of class A, it will call the __add__ method and return an object of class A. When we print the object, it will call the __str__ method and return the string representation of the object.'''
class A:
    def __init__(self, a):
        self.a = a
    def __add__(self, other):
        return A(self.a+other.a)
    def __str__(self):
        return str(self.a)
    
obj1 = A(10)
obj2 = A(20)
obj3 = A(40)
print(obj1+obj2+obj3)

'''
>>>
70
'''