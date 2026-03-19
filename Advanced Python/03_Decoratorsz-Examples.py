###Examples on Decorators

##1. Create a decorator that repeat the function for three times.
def decor(f):
    def wrapper_or_inner():
        print('Coming 3-times')
        for i in range(1, 4):
            f()
    return wrapper_or_inner

@decor
def user1():
    print('I am user-1')
user1()
'''
>>>
Coming 3-times
I am user-1
I am user-1
I am user-1
'''

##2. Create a decorator that checks whether all arguments passed to a function are integers.
def check_args(f):
    def wrapper(*a):
        total_int = []
        for i in a:
            if type(i) == int:
                total_int.append(i)
        print("Total argument passed as integer are:", len(total_int))
        f(*a)
    return wrapper

@check_args
def args(*a):
    print(a)
args('Mayur', 2, 3, 4)
'''
>>>
Total argument passed as integer are: 3
('Mayur', 2, 3, 4)
'''

##3. Create a decorator that print the number of times the functuion is called.
def deccor_count(f):
    def wrapper():
        wrapper.count += 1
        print("Function called", wrapper.count, "times")
        f()
    wrapper.count = 0
    return wrapper

@deccor_count
def user1():
    print("Hello")

@deccor_count
def user2():
    print("I am useer2")

user1()
user1()

user2()
user2()
user2()

print(f"Total count of user1: {user1.count}")
print(f"Total count of user2: {user2.count}")
'''
>>>
Function called 1 times
Hello
Function called 2 times
Hello
Function called 3 times
Hello
Function called 1 times
I am useer2
Function called 2 times
I am useer2
Function called 3 times
I am useer2
Total count of user1: 2
Total count of user2: 3
'''

##4. Create a function which will give greetings to the user if the user is admin.
def decor(role):
    def inner(f):
        def wrapper():
            if f.__name__ == 'Admin':
                f()
                print("Good Morning")
        return wrapper
    return inner

@decor("admin")
def Admin():
    print("Hello! I am Admin")

@decor("user")
def user1():
    print("I am user1")
user1()
Admin()
'''
>>>
Good Morning Admin
Hello! I am Admin
'''

##5. Create  a decorator that measures and prints the execution time of a function.
import time
def measure_exe_time(f):
    def wrapper():
        start_time = time.time()
        f()
        end_time = time.time()
        total_time = end_time - start_time
        print("Total time taken by the function is %.7f seconds" % total_time)
        # print(f"Total time taken by the function is {total_time:.2f} seconds")
    return wrapper

@measure_exe_time
def user1():
    print("I am user1")

@measure_exe_time
def user2():
    print("I am useer2")

user1()
user1()
user1()
user2()
'''
>>>
I am user1
Total time taken by the function is 0.0001380 seconds
I am user1
Total time taken by the function is 0.0000489 seconds
I am user1
Total time taken by the function is 0.0022805 seconds
I am useer2
Total time taken by the function is 0.0002487 seconds
'''

