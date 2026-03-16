###Decorators

'''
#syntax
def decor(f):
    def wrapper_or_inner():
       #code before
      f()
      #code after
   return wrapper_or_inner

@decor
def user1():
    pre-take action
    //S.B.
    post-take action
'''

def decor(f):
    def wrapper_or_inner():
        print('Log-in')
        f()
        print('Log-out')
    return wrapper_or_inner

@decor
def user1():
    print('Posted a picture')

@decor
def user2():
    print('Liked that picture')

@decor
def user3():
    print('Shared that picture')

user1()
user2()
user3()
'''
>>>
Log-in
Posted a picture
Log-out
Log-in
Liked that picture
Log-out
Log-in
Shared that picture
Log-out
'''

