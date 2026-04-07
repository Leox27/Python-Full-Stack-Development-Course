###Easy (Basics of Recursion)

#1. Print numbers from 1 to N using recursion
def print_numbers(n):
    if n == 0:
        return 
    else:
        print_numbers(n - 1)
    print(n)
print(print_numbers(5))
'''
>>>
1
2
3
4
5
None
'''

##2. Print numbers from N to 1
def print_num(N):
    if N == 0:
        return None
    else:
        print(N)
        print_num(N-1)
print_num(5)
'''
>>>
None
5
4
3
2
1
'''

##3. Find factorial of a number
def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)
print(factorial(7))
'''
>>>
5040
'''

##4. Find sum of first N natural numbers
def natural_sum(n):
    if n == 0:
        return 0
    else:
        return n+natural_sum(n-1)
print(natural_sum(5))
'''
>>>
15
'''

##5. Print all even numbers from 1 to N
def even_num(n):
    if n == 0:
        return
    even_num(n - 1)
    if n%2 == 0:
        print(n)
even_num(10)
'''
>>>
2
4
6
8
10
'''

##6. Find power of a number (xⁿ) using recursion
x = 2
def power(n):
    if n == 0:
        return
    else:
        power(n-1)
    print(x**n)
power(10)
'''
>>>
2
4
8
16
32
64
128
256
512
1024
'''

##7. Count digits in a number
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)
print(count_digits(1238))
'''
>>>
4
'''

##8. Sum of digits of a number
def sum_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_digits(n // 10)
print(sum_digits(1234))
'''
>>>
10
'''

##9. Reverse a number using recursion
def rev_num(n, rev=0):
    if n == 0:
        return rev
    
    return rev_num(n // 10, rev * 10 + (n % 10))
print(rev_num(6734))
'''
n=6734, rev=0
→ rev = 0*10 + 4 = 4

n=673, rev=4
→ rev = 4*10 + 3 = 43

n=67, rev=43
→ rev = 43*10 + 7 = 437

n=6, rev=437
→ rev = 437*10 + 6 = 4376
'''

##10. Find GCD of two numbers (basic recursion)
def gcd(a, b):
    if a == 0 or b == 0:
        return 0
    return 