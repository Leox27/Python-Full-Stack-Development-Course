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