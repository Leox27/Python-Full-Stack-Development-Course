                                                                #### Recursion ####


##1. Factorial
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(7))
'''
>>>
5040'''


##2. Sumnum
def Sumnum(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n+Sumnum(n-1)
print(Sumnum(7))
'''
>>>
28
'''

##3. reverse the nu,ber
def num(n):
    if n == 0:
        return
    else:
        print(n)
    n=n-1
    num(n)
print(num(7))
'''>>>
7
6
5
4
3
2
1
None
'''

##4. Reverse number with id
def num(n):
    if n == 0:
        return
    else:
        print(n, "id", id(n))
    n=n-1
    num(n)
print(num(7))
'''
>>>
7 id 140735047496808
6 id 140735047496776
5 id 140735047496744
4 id 140735047496712
3 id 140735047496680
2 id 140735047496648
1 id 140735047496616
None
'''

##5. Reversethe number woth thhe function address
import inspect
def num(n):
    print(inspect.currentframe())
    if n == 0:
        return
    else:
        print(n, "id", id(n))
    n=n-1
    num(n)
print(num(7))
'''
>>>
<frame at 0x0000024733AB6420, file 'c:\\Users\\Asus\\Downloads\\Untitled-1.py', line 3, code num>
7 id 140732134093928
<frame at 0x0000024733AB6B20, file 'c:\\Users\\Asus\\Downloads\\Untitled-1.py', line 3, code num>
6 id 140732134093896
<frame at 0x0000024733AB7060, file 'c:\\Users\\Asus\\Downloads\\Untitled-1.py', line 3, code num>
5 id 140732134093864
<frame at 0x0000024733AB7140, file 'c:\\Users\\Asus\\Downloads\\Untitled-1.py', line 3, code num>
4 id 140732134093832
<frame at 0x0000024733D0D8C0, file 'c:\\Users\\Asus\\Downloads\\Untitled-1.py', line 3, code num>
3 id 140732134093800
<frame at 0x0000024733D0DC40, file 'c:\\Users\\Asus\\Downloads\\Untitled-1.py', line 3, code num>
2 id 140732134093768
<frame at 0x0000024733D0DA80, file 'c:\\Users\\Asus\\Downloads\\Untitled-1.py', line 3, code num>
1 id 140732134093736
<frame at 0x0000024733D0D9A0, file 'c:\\Users\\Asus\\Downloads\\Untitled-1.py', line 3, code num>
None
'''

##5. Factorial with address
import inspect
def factorial(n):
    print(inspect.currentframe())
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(7))
'''>>>
<frame at 0x000001E0B0A0A4D0, file 'X:/GitHub/QSpider/Recursion.py', line 76, code factorial>
<frame at 0x000001E0B32D7370, file 'X:/GitHub/QSpider/Recursion.py', line 76, code factorial>
<frame at 0x000001E0B33D6A80, file 'X:/GitHub/QSpider/Recursion.py', line 76, code factorial>
<frame at 0x000001E0B33D6C20, file 'X:/GitHub/QSpider/Recursion.py', line 76, code factorial>
<frame at 0x000001E0B33D6CF0, file 'X:/GitHub/QSpider/Recursion.py', line 76, code factorial>
<frame at 0x000001E0B33D6DC0, file 'X:/GitHub/QSpider/Recursion.py', line 76, code factorial>
<frame at 0x000001E0B33D6E90, file 'X:/GitHub/QSpider/Recursion.py', line 76, code factorial>
5040
'''
