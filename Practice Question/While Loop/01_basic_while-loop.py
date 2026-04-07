
###Basic While Loop Problems

##1. Print numbers from 1 to N using a while loop.
n = 10
i = 0
while i<=n:
    print(i, end=' ')
    i += 1
'''
>>>
0 1 2 3 4 5 6 7 8 9 10
'''


##2. Print all even numbers from 1 to N.
n = 10
i = 1
while i <= n:
    if i%2 == 0:
        print(i, end=' ')
    i += 1
'''
>>>
2 4 6 8 10 
'''


##3. Find the sum of first N natural numbers.
n = 10
summ = 0
i = 1
while i <= n:
    summ += i
    i += 1
print(summ)
'''
>>>
55
'''


##4. Reverse a number (e.g., 123 → 321).
n = 123
rev = 0
while n != 0:
    rev = rev*10 + (n % 10)
    n //= 10
print(rev)
'''
>>>
321
'''


##5. Count the number of digits in a number.
n = 12345
i = 0
while n != 0:
    digit = n % 10
    n //= 10
    i += 1
print(i)
'''
>>>
5
'''


##6. Find the sum of digits of a number.
n = 12345
summ = 0
while n != 0:
    digit = n % 10
    summ += digit
    n //= 10
print(summ)
'''
>>>
15
'''


##7. Check if a number is a palindrome.
n = 123321
temp = n
rev = 0
while temp != 0:
    rev = rev*10 + (temp % 10)
    temp //= 10
if rev == n:
    print("Palindrome")
else:
    print("Not palindrome")
'''
>>>
Palindrome
'''

#
n = 12332
temp = n
rev = 0
while temp != 0:
    rev = rev*10 + (temp % 10)
    temp //= 10
if rev == n:
    print("Palindrome")
else:
    print("Not palindrome")
'''
>>>
Not palindrome
'''


##8. Print multiplication table of a given number.
n = 27
i = 1
while i <= 10:
    print(f"{n} * {i} = {n*i}")
    i += 1
'''
>>>
27 * 1 = 27
27 * 2 = 54
27 * 3 = 81
27 * 4 = 108
27 * 5 = 135
27 * 6 = 162
27 * 7 = 189
27 * 8 = 216
27 * 9 = 243
27 * 10 = 270
'''


##9. Find factorial of a number using while loop.
n = 7
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(factorial)
'''
>>>
5040
'''


##10. Print numbers from N to 1 (reverse order).
n = 10
i = n
while i >= 1:
    print(i, end=' ')
    i -= 1
'''
>>>
10 9 8 7 6 5 4 3 2 1 
'''

