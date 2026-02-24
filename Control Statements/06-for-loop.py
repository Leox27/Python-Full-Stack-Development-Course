                         #### for loop ####
'''
a='Sam'
count=0
for i in a:
    print(i, end="")
    count += 1
print(count)

##WAP to print all the integer prsent in th list
lst=eval(input("Enter the ;is: "))
lst2=[]
for i in lst:
    if type(i) ==int:
        lst2+=[i]
print(lst2)


## WAP to find the length of homogeneous tuple without len().
tup=(1, True, 'Mayur', 12.3)
count=0
for i in tup:
    count += 1
print("Length of the homogeneous tuple is:",count)


##WAP to extract all the even numbers present in the list.
lst=eval(input("Enter the is: "))
lst2=[]
for i in lst:
    if type(i) == int:
        if i%2 == 0:
            lst2 += [i]
print(lst2)


##WAP to remove duplicates from list.
lst=eval(input("Enter the is: "))
lst2=[]
for i in lst:
    if i not in lst2:
        lst2 += [i]
print(lst2)


##WAP to reverse string without using slicing.
string=input("Enter the string:")
rev_str=''
for i in range(len(string)-1,-1,-1):
    rev_str += string[i]
print(rev_str)


#@nd method
string=input("Enter the string:")
rev_str=''
for i in range(len(string)-1,-1,-1):
    rev_str += string[i]
print(rev_str)


##to extract all the lowercase char ina string only of the ascii value is even.
string=input("Enter the string: ")
out_str=''
for i in string:
    if 'a'<=i<='z':
        if ord(i)%2 == 0:
            out_str += i
            print(i,"=",ord(i))
print(out_str)

#2nd method
string=input("Enter the string: ")
out_str=''
for i in string:
    if 'a'<=i<='z' and ord(i)%2 == 0:
        out_str += i
        print(i,"=",ord(i))
print(out_str)

##WAP to check whether the last digit of an integer is even or not.
num=int(input("Enter the number: "))
num_str=str(num)
num_string=''
for i in num_str:
    num_string += i
last_digit=num_string[-1]
int_digit=int(last_digit)
if int_digit%2 == 0: 
    print("The last digit of an integer is:",int_digit)
else:
    print("The last digit is not even integer",int_digit)

#2nd method
num=input("Enter the number: ")
for i in str(num)[-1]:
    if int(i)%2 == 0:
        print("Even")
    else:
        print("Odd")
    
##WAP to extract all key value pairs from the dictionary only if both keys and valurs are exaclty same.
d=eval(input("Enter the dictionary: "))
dictionary={}
for key, value in d.items():
    if key == value:
        dictionary[key] = value
print("Keys and values are same", dictionary)

#2nd method
d=eval(input("Enter the dictionary: "))
o_d={}
for i in d:
    if type(i) == type(d[i]):
        o_d[i] = d[i]
print(o_d)

#3rd method
d=eval(input("Enter the dictionary: "))
o_d={}
for i in d:
    if i == d[i]:
        o_d[i] = d[i]
print(o_d)


##WAP to extract all the kays value pairs from the dictionary only  if the keys are of string datatype and values are integeres.
d=eval(input("Enter the dictionary: "))
dictionary={}
for key, value in d.items():
    if type(key) == str and type(value) == int:
        dictionary[key] = value
print("Keys and values",dictionary)

#2nd method
d=eval(input("Enter the dictionary: "))
o_d={}
for i in d:
    if type(i) == str and type(d[i]) == int:
        o_d[i] = d[i]
print(o_d)


##WAP to get the following output using len() function.
# S='power star'
# Out={'power':5, 'star':4}
S='power star'
Out={}
power=S[:5:]
star=S[6::]
for key, value in {power:len(power), star:len(star)}.items():
    Out[key] = value
print(Out)

#2nd method
S='power star'
Out={}
split=S.split(' ')
for i in split:
    Out[i] = len(i)
print(Out)


##WAP to fet the following output.
# S='power star'
# Out={'power':rewop, 'star':rats}
S='power star'
Out={}
power=S[:5:]
star=S[6::]
for key, value in {power:power[len(power)::-1], star:star[len(star)::-1]}.items():
    Out[key] = value
print(Out)

#2nd method
S='power star'
Out={}
split=S.split(' ')
for i in split:
    Out[i] = len(i)
print(Out)

#3rd
S='power star'
Out={}
split=S.split(' ')
for i in split:
    Out[i] = i[len(i)::-1]
print(Out)


##WAP to extract all the non-default values from a list.
#[0, 1, '', 'hi', None, 5, False, 'python']
lst=eval(input("Enter the list: "))
lst2=[]
for i in lst:
    if bool(i) == True:
        lst2.append(i)
print(lst2)

#2nd method
#do again
lst=eval(input("Enter the list: "))
lst2=[]
for i in lst:
    if i in ['', "", None, False, 0, 0.0, oj]:
        lst2.append(i)
print(lst2)

##WAP to check whether the list is homogeneous or not.
lst=eval(input("Enter the list: "))
st=set()
for i in lst:
    st.add(type(i))
if len(st) == 1:
    print("List is homogeneous", len(st), st)
else:
    print("List is not homogeneous", len(st), st)
'''
#2nd method
lst=eval(input("Enter the list: "))
for i in lst:
    if type(lst[0]) == type(i):
        print("Homogeneouos")
        break
    else:
        print("Not Homogeneous")




        




















