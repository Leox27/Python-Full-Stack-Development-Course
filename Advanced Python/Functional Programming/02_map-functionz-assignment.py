##1. Create a map() to add 10 in all numbersnpresent inside a collection.
numbers = [1, 2, 3, 4, 5]
print(list(map(lambda x: x+10, numbers)))

##2. Creaate map() to extract all prime numbers from 1 to 100 and store them in a list.
# l1 = [i for i in range(1, 101)]
def prime(n):
    if n < 2:
        return  
    for i in range(2, n):
        if n%i == 0:
            return  
    return n
result = list(map(prime, range(1, 101)))
l1=[]
for i in result:
    if i != None:
        l1.append(i)
print(l1)

##3. Create a map() to extract all the armstrong numbers from 1 to 10,000 and store them in a list.
def armstrong(n):
    sum = 0
    num_string = str(n)
    degree = len(str(n))
    for i in num_string:
        sum += int(i)**degree
    if sum == n:
        return n
result = list(map(armstrong, range(1, 10000)))
l1=[]
for i in result:
    if i != None:
        l1.append(i)
print(l1)
'''
>>>
[1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474]
'''

##4. Create a map() to extract all the string number from 1 to 1,00,000 and store them in a list.
def strong(n):
    sum = 0
    num_string = str(n)
    for i in num_string:
        def factorial(i):
            if i == 1 or i== 0:
                return 1
            else:
                return i*factorial(i-1)
        factorials = factorial(int(i))
        sum += factorials
    if sum == n:
        return n
result = list(map(strong, range(1, 100000)))
l1=[]
for i in result:
    if i != None:
        l1.append(i)
print(l1)
'''
>>>
[1, 2, 145, 40585]
'''

##5. Write a program to print same character double time of a string and store them in a list.
string = input("Enter the string: ")
def duo_string(double_string):
    return double_string*2
print(list(map(duo_string, string)))
'''
>>>
['kk', 'aa', 'ss', 'hh', 'ii', 'nn', 'aa', 'tt', 'hh']
'''

##6. Create a map() and reverse all the strings and store them into a list.
string = ['kashinath', 'Amar', 'Datta', 'Prasad', 'Trimbak']
def rev_string(string):
    return string[::-1]
result = list(map(rev_string, string))
print(result)
'''
>>>
['htanihsak', 'ramA', 'attaD', 'dasarP', 'kabmirT']
'''