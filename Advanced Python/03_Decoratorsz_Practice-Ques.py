###Basic Practice Questions for Decorators

##1. Create a decorator that prints "Function started" and "Function ended".
def start_end(f):
    def wrapper():
        print("Function startedd")
        f()
        print("Function ended")
    return wrapper
@start_end
def user1():
    print("Hello ! I am user1")

user1()
'''
>>>
Function startedd
Hello ! I am user1
Function ended
'''

##2. Create a decorator that repeats a function 5 times.
def repeat(n):
    def decorator(f): #decorator (outer-function)
        def wrapper(*args, **kwargs): #inner-function
            for _ in range(n):
                f(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def user1():
    print("Hello, I am user 1")

user1()
'''
>>>
Hello, I am user 1
Hello, I am user 1
Hello, I am user 1
'''

##3. Create a decorator that prints the function name before execution.
def fun_name(f):
    def wrapper(*args, **kwargs):
        print(f.__name__)
        f(*args, **kwargs)
    return wrapper

@fun_name
def user1():
    print("I am user1")
user1()
'''
>>>
user1
I am user1
'''

##4. Create a decorator that checks if a number is positive before running the function.
def if_positive(f):
    def wrapper(*args, **kwargs):
        num = args[0]
        f(*args, *kwargs)
        print("Checking the number is positive or not")
        if num>0:
            print(num, "is positive")
        else:
            print("The number is not positive")
    return wrapper

@if_positive
def user1(num):
    print("Check the number is positive or not")

user1(9)
'''
>>>
Check the number is positive or not
Checking the number is positive or not
9 is positive
'''

##5. Create a decorator that converts the return value to uppercase (for strings).
def converter(f):
    def wrapper(string):
        string = string.upper()
        f(string)
    return wrapper
@converter
def user1(string):
    print(string)

user1('Suraj Lohar')
user1('Mayur Jadhav')
'''
>>>
SURAJ LOHAR
MAYUR JADHAV
'''

##6. Create a decorator that prints all arguments passed to a function.
def print_args(f):
    def wrapper(*args, **kwargs):
        arguments = []
        f(*args)
        print(f'For {f.__name__}')
        for i in args:
            arguments.append(i)
        for i in arguments:
            print(i)
    return wrapper

@print_args
def user1(*a):
    pass
user1('Kashinath', 1, 1.2, 4+0j, 'Hello')

@print_args
def user2(*b):
    pass
user2('Naruto Shipudden', 'One Piece', 'Dragon Ball Z', 'Bleach', 'JuJutsu Kaisen')
'''
>>>
For user1
Kashinath
1
1.2
(4+0j)
Hello
For user2
Naruto Shipudden
One Piece
Dragon Ball Z
Bleach
JuJutsu Kaisen
'''

##7. Create a decorator that counts the number of arguments passed.
def count(f):
    def wrapper(*args, **kwargs):
        total = len(args) + len(kwargs)
        print(f"Total arguments passed to {f.__name__} is {total}")
        return f(*args, **kwargs)
    return wrapper

@count
def user1(*args, **kwargs):
    pass

user1('Mayur', 1, 1.7, 9+1j, [1], True, a=14)
'''
>>>
Total arguments passed to user1 is 7
'''

###Medium Practice Questions for Decorators

##1. Create a decorator that validates all arguments are integers.
def args_int(f):
    def wrapper(*args):
        f(*args)
        total_int = 0
        total_non_int = 0
        for i in args:
            if type(i) == int:
                total_int += 1
                print(f'The argument passed in the function is Integer: {i}')
            else:
                total_non_int += 1
                print(f'The argument passed in the function is not an Integer: {i}, {type(i)}')
        print(f'Total integers values passed as arguments are {total_int}')
        print(f'Total non Integers values passed as arguments are {total_non_int}')
    return wrapper

@args_int
def user1(*args):
    pass

user1(1, 7, 9, [1], True, 14)
'''
>>>
The argument passed in the function is Integer: 1
The argument passed in the function is Integer: 7
The argument passed in the function is Integer: 9
The argument passed in the function is not an Integer: [1], <class 'list'>
The argument passed in the function is not an Integer: True, <class 'bool'>
The argument passed in the function is Integer: 14
Total integers values passed as arguments are 4
Total non Integers values passed as arguments are 2
'''

##2.  Create a decorator that checks if user is logged in before executing a function.
user2 = {"name": "Suraj", "logged_in": True}
user1 = {"name": "Mayur", "logged_in": False}
users = [user1, user2]

def check_login(f):
    def wrapper(*args, **kwargs):
        for user in users:
            if user["logged_in"]:
                print(f"Welcome {user['name']}")
                return f(*args, **kwargs)
            else:
                print(user['name'])
                print("Please login first")
    return wrapper

@check_login
def profile():
    print("This is your profile page")

profile()
'''
>>>
Mayur
Please login first
Welcome Suraj
This is your profile page
'''

##3. Create a decorator that limits a function to run only once.
def limit(f):
    called = False
    def wrapper(*args):
        nonlocal called
        if not called:
            called = True
            f(*args)
        else:
            print("Function can called only once")
    return wrapper

@limit
def one_limit(*args):
    pass

one_limit('Hii')
one_limit('Hii')
'''
>>>
Function can called only once
'''

##4. Create a decorator that caches the result (simple memoization).
def cache_result(f):
    cache = {}   # stores previous results
    def wrapper(*args):
        if args in cache:
            print("Fetching from cache...")
            return cache[args]
        else:
            print("Calculating result...")
            result = f(*args)
            cache[args] = result   # store result
            return result
    return wrapper

@cache_result
def add(a, b):
    return a + b

print(add(2, 3))   
print(add(2, 3))   
'''
>>>
Calculating result...
5
Fetching from cache...
5
'''

##5. Create a decorator that logs function calls into a file.
def log_function(f):
    def wrapper(*args):

        file = open("log.txt", "a")
        file.write(f.__name__, args)
        file.close()

##6. Create a decorator that checks if input string is not empty.

##7. Create a decorator that retries a function 3 times if it fails.

##8. Create a decorator that rounds off the return value to 2 decimal places.

###Hard Practice Questions for Decorators

##1. Create a decorator that measures execution time and logs slow functions (>1 sec).

##2. Create a decorator that limits API calls (rate limiting) — max 3 calls per 10 seconds.

##3. Create a decorator that checks user roles (admin/user/guest) before access.

##4. Create a decorator that tracks how many times each user calls a function.

##5. Create a decorator that handles exceptions and logs errors instead of crashing.

# 🔥 BONUS (Very Real-World Inspired)

# Create a decorator that simulates authentication using a token.

# Create a decorator that formats API response into JSON-like structure.

# Create a decorator that blocks function execution during certain hours (e.g., maintenance mode).

# Create a decorator that validates email format before function execution.

# Create a decorator that limits file upload size (simulate).

# def ascii_value():
#     char = [str(ord(i)) for i in range(65, 97)]
#     ascii_val = [i for i in range(65, 97)]
#     for i, j in zip(char, ascii_val):
#         yield i, j
# print(dict(ascii_value()))
