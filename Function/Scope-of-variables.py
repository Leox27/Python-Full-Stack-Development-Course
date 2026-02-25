                                        #### Scope of variables ####
###Global variable
##
a=5 #main space or global space
b=4
def func():
    global a #global variable inside def(User defined function)
    a=100 
    print(a)
func()
print(a)
'''
>>>
100
100
'''

##Without global space
a=100
print(a, id(a))
def func():
    a=110
    print(a, id(a))
func()
print(a, id(a))
'''
>>>
100 140719672819720
110 140719672820040
100 140719672819720
'''

###Local variable
##
a=100
print(a, id(a))
def func():
    global a
    b=100+a
    a=110
    print(a, id(a))
    def func2():
        nonlocal b
        print(b, id(b))
    func2()
func()
print(a, id(a))
print('110 ID is', id(110))
print('100 ID is', id(100))
print('200 ID is', id(200))
'''
>>>
100 140719672819720
110 140719672820040
200 140719672822920
110 140719672820040
110 ID is 140719672820040
100 ID is 140719672819720
200 ID is 140719672822920
'''

##Returning the global address
def func():
    a=10
    print(a, id(a))
    def func2():
        nonlocal a
        print(a, id(a))
        a=100
        print(a, id(a))
    func2()
    print(a, id(a))
func()
'''
>>>
10 140719672816840
10 140719672816840
100 140719672819720
100 140719672819720
'''      

##ex1
a=10 #main space or global space
def fun():
    global a #global variable inside def
    c=10+a
    a=100 
    print("fun",a)
    print("fun",c)
    def nested_fun():
        c=150
        print("nested_fun",c)
    nested_fun()
fun()
'''
>>>
fun 100
fun 20
nested_fun 150
'''

##ex2
a=10 #main space or global space
def fun():
    global a #global variable inside def
    c=10+a
    a=100 
    print("fun a:",a)
    print("fun c:",c)
    def nested_fun():
        nonlocal c
        d=c+100
        c=150
        print("nested_fun c:",c)
        print("nested_fun d:",d)
    nested_fun()
fun()
'''
>>>
fun a: 100
fun c: 20
nested_fun c: 150
nested_fun d: 120
'''

##nonlocal variable
a=10 #main space or global space
c=100
def fun():
    global a #global variable inside def
    #global c
    c=10+a
    a=100
    print("fun a:",a)
    print("id",id(a))
    
    print("fun c:",c)
    def nested_fun():
        nonlocal c
        d=c+100
        c=150
        print("nested_fun c:",c)
        print("nested_fun d:",d)
    nested_fun()
fun()
'''
>>>
fun a: 100
id 140719672819720
fun c: 20
nested_fun c: 150
nested_fun d: 120
'''
