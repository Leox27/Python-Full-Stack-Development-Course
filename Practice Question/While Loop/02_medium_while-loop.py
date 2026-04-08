
###Medium While Loop Problems

##1. Check if a number is prime using while loop.
n = 1
if n <= 1:
    print("Number is not prime")
else:
    i = 2
    count = 0
    while i < n:
        if n % i == 0:
            count += 1
        i += 1

    if count == 0:
        print("Number is prime")
    else:
        print("Number is not prime")
'''
>>>
Number is not prime
'''

# 
n = 97
if n <= 1:
    print("Number is not prime")
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            print("Number is not prime")
            break
        i += 1
    else:
        print("Number is prime")
'''
>>>
Number is prime
'''


##2. Print Fibonacci series up to N terms using while loop.
n = 10
first = 0
second = 1
i = 0
while i <= n:
    print(first, end=' ')
    first, second = second, first + second
    i += 1
'''
>>>
0 1 1 2 3 5 8 13 21 34 55
'''


##3. Find GCD (Greatest Common Divisor) of two numbers using while loop.(HCF)
a = 18
b = 27
if a < b:
    smaller = a
else:
    smaller = b
i = 1
while i <= smaller:
    if a%i == 0 and b%i == 0:
        gcd = i
    i += 1
print(gcd)
'''
>>>
9
'''


##4. Find LCM using while loop.
a = 12
b = 15
if a > b:
    greater = a
else:
    greater = b
while True:
    if greater % a == 0 and greater % b == 0:
        lcm = greater
        break
    greater += 1
print(lcm)
'''
>>>
60
'''


##5. Convert decimal number to binary using while loop.
n = 2
binary = ''
while n != 0:
    digit = (n % 2)
    binary = str(digit) + binary
    n //= 2
print(binary)
'''
>>>
10
'''

#
n = 2
binary = 0
place = 1
while n > 0:
    digit = (n % 2)
    binary += digit*place
    place *= 10
    n //= 2
print(binary)
'''
>>>
10
'''


##6. Find Armstrong number (e.g., 153).
n = 153
temp = n
len_str = len(str(n))
armstrong = 0
while temp != 0:
    digit = temp % 10
    armstrong += digit**len_str
    temp //= 10
if armstrong == n:
    print(f"{armstrong} is armstrong")
else:
    print(f"{armstrong} is not armstrong")
'''
>>>
153 is armstrong
'''


##7. Remove all zeros from a number (e.g., 102030 → 123).
n = 102030
temp = n
rev = 0
while temp != 0:
    rev = rev*10 + (temp % 10)
    temp //= 10
number = 0
while rev != 0:
    digit = rev % 10
    if digit != 0:
        number = number*10 + digit
    rev //= 10
print(number)
'''
>>>
123
'''


##8. Find largest digit in a number.
n = 653896
largest = 0
while n != 0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n //= 10
print(largest)
'''
>>>
9
'''


##9. Count frequency of digits in a number.
n = 7563736946
freq = {}
while n != 0:
    digit = n % 10
    if digit not in freq:
        freq[digit] = 1
    else:
        val = freq[digit]
        freq[digit] = val+1
    n //= 10
print(freq)
'''
>>>
{6: 3, 4: 1, 9: 1, 3: 2, 7: 2, 5: 1}
'''


##10. Check if a number is perfect (sum of divisors = number).
n = 6
i = 1
sum_div = 0
while i < n:
    if n%i == 0:
        sum_div += i
    i += 1
if n == sum_div:
    print(f"{n} is Perfect number")
else:
    print(f"{n} is not Perfect number")
'''
>>>
6 is Perfect number
'''

