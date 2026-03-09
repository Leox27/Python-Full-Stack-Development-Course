###Monkey patching

def add(a, b):
    print("The sum is: ", a+b)
prev=add #monkey patching - storing the reference of original function in another variable

def add(a, b, c, d):
    print("The sum is: ", a+b+c+d)

add(10, 20, 30, 40) #calling the new function
prev(10, 20) #calling the original function using the reference variable

'''
>>>
The sum is:  100
The sum is:  30
'''

##Using classes & Objects

class Dog:
    def bark(self):
        print("Woof Woof")

    def eat(self):
        print("Dog is eating")

class Cat:
    def bark(self):
        print("Meow Meow")

    def eat(self):
        print("Cat is eating")

#monkey patching - replacing the original method with new method
def new_bark(self):
    print("Bow Bow")
Dog.bark = new_bark 

def new_eat(self):
    print("Dog is eating bones")
Dog.eat = new_eat

def new_bark_cat(self):
    print("Meow Meow Meow")
Cat.bark = new_bark_cat

def new_eat_cat(self):
    print("Cat is eating fish")
Cat.eat = new_eat_cat

dog=Dog()
dog.bark()
dog.eat()

cat=Cat()
cat.bark()
cat.eat()

'''
>>>
Bow Bow
Dog is eating bones
Meow Meow Meow
Cat is eating fish
'''

##Using Inheritance

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        print("Area of Rectangle: ",self.length*self.width)

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print("Area of circle: ", 3.14*self.radius*self.radius)

#Monkey patch
def new_circle_area(self):
    print("Monkey patched area: ", 3.14*self.radius*self.radius)
Circle.area = new_circle_area

circle = Circle(10)
rect = Rectangle(4,6)

# using loop to call area method of both classes
shapes = [Circle(10), Rectangle(4,6)]

for a in shapes:
    a.area()

'''
>>>
Monkey patched area:  314.0
Area of Rectangle:  24
'''
