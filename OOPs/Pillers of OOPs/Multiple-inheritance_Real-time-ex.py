### Basic Calculator using Multiple-Inheritance

class Addition:
    def add(self, a, b):
        print("Sum is : ", a+b)
class Substraction:
    def sub(self, a, b):
        print("Substraction is : ", a-b)
class Multiplication:
    def mul(self, a, b):
        print("Multiplication is : ", a*b)
class Division:
    def div(self, a, b):
        print("Division is : ", a/b)

class Calculator(Addition, Substraction, Multiplication, Division):
    def __init__(self):
        self.a=int(input("Enter the number a: "))
        self.b=int(input("Enter the number b: "))

obj=Calculator()
print("Enter choice: 1 - For Addition")
print("Enter choice: 2 - For Substraction")
print("Enter choice: 3 - For Multiplication")
print("Enter choice: 4 - For Division")

ch = int(input("Enter choice: ")) #Object

if ch == 1:
    obj.add(obj.a, obj.b)
elif ch == 2:
    obj.sub(obj.a, obj.b)
elif ch == 3:
    obj.mul(obj.a, obj.b)
elif ch == 4:
    obj.div(obj.a, obj.b)
else:
    print("Please enter one of these numbers _ 1, 2, 3, 4")

'''
>>>
Enter the number a: 10
Enter the number b: 10
Enter choice: 1 - For Addition
Enter choice: 2 - For Substraction
Enter choice: 3 - For Multiplication
Enter choice: 4 - For Division
Enter choice: 2
Substraction is :  0
'''