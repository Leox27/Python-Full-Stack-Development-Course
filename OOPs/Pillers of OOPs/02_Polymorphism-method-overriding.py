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