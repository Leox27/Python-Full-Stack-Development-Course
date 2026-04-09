
###Medium While Loop Problems

##1. Reverse a number without using extra variable (in-place logic challenge).
'''
“For integers, strict in-place reversal isn’t feasible. I’ll use constant space with arithmetic operations.”
'''
n = 1234
rev = 0
while n != 0:
    digit = n % 10
    rev = rev*10 + digit
    n //= 10
print(rev)

##2. Detect cycle in a number transformation (like happy number problem).
n = 19
set_coll = set()
while n != 1 and n not in set_coll:
    set_coll.add(n)

    temp = n
    total = 0
    while temp != 0:
        digit = temp % 10
        total += digit*digit
        temp //= 10
    n = total
if n == 1:
    print("Happy Number")
else:
    print("Cycle detected")
'''
>>>
Happy Number
'''


##3. Check if a number is a strong number (sum of factorials of digits).
n = 145
temp = n
factorial_sum = 0
while temp != 0:
    digit = temp % 10

    summ = 1
    i = 1
    while i <= digit:
        summ *= i
        i += 1
    factorial_sum += summ
    temp //= 10
if factorial_sum == n:
    print(f"{n} is Strong Number")
else:
    print(f"{n} is Not a Strong Number")
'''
>>>
145 is Strong Number
'''


##4. Implement power function (x^y) using only while loop (no built-in).
x = 3
y = 10
result = 1
i = 1
while i <= y:
    result *= x
    i += 1
print(result)
'''
>>>
59049
'''


##5. Check if a number is palindrome without reversing the whole number.
n = 121
if n < 0:
    print("Not Palindrome")
else:
    reversed_half = 0
    while n > reversed_half:
        digit = n % 10
        reversed_half = reversed_half * 10 + digit
        n //= 10
    # For even digits: n == reversed_half
    # For odd digits: n == reversed_half // 10
    if n == reversed_half or n == reversed_half // 10:
        print("Palindrome")
    else:
        print("Not Palindrome")
'''
>>>
Palindrome
'''


##6. Check if a number is a palindrome without converting to string.
n = 1234321
temp = n
rev = 0
while temp != 0:
    rev = rev*10 + (temp % 10)
    temp //= 10
if n == rev:
    print("Palindrome")
else:
    print("Not palindrome")


##7. Implement division without using / operator (using subtraction + while loop).
m = 17
n = 3
result = 0
while m >= n:
    m -= n
    result += 1
print(f"Result: {result}")
print(f"Remainder: {m}")
'''
>>>
Result: 5
Remainder: 2
'''


##8. Count trailing zeros in factorial of a number.
n = 8
factorial = 1
i = n
while i >= 1:
    factorial *= i
    i -= 1
zeros = 0
while factorial != 0:
    digit = factorial % 10
    if digit == 0:
        zeros += 1
    else:
        break
    factorial //= 10
print(f"No. of zeros are {zeros}")
'''
>>>
No. of zeros are 1
'''
#efficient way
n = 100
count = 0
while n > 0:
    n //= 5
    count += n
print(f"No. of zeros are {count}")
'''
>>>
No. of zeros are 2
'''


##9. Generate all divisors of a number using while loop efficiently.
n = 100
i = 1
while i <= n:
    if n%i == 0:
        print(i, end=' ')
    i += 1
'''
>>>
1 2 4 5 10 20 25 50 100
'''


##10. Simulate a basic calculator using while loop (menu-driven program).
while True:
    print('''
Calculator Menu
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
''')

    choice = input("Enter choice: ")
    if choice == '5':
        print("Exiting...")
        break

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice, please select 1 to 5.")
        continue

    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))

    if choice == '1':
        print("Addition:", num1 + num2)
    elif choice == '2':
        print("Subtraction:", num1 - num2)
    elif choice == '3':
        print("Multiplication:", num1 * num2)
    elif choice == '4':
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print("Division:", num1 / num2)
'''
>>>
Calculator Menu
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Enter choice: 3
Enter number 1: 10
Enter number 2: 27
Multiplication: 270.0

Calculator Menu
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Enter choice: Exit
Invalid choice, please select 1 to 5.

Calculator Menu
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Enter choice: 5   
Exiting...

'''
