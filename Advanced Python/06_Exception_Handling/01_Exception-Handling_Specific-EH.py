
###Specific Exception Handling

'''
#syntax
try:
    // code
except TypeOfError:
    // display
'''

##1. WAP to create a list of 5-elements ask the user to enter an index to display the data or rules.(Handle index error, value error)
try:
    l1 = ['Mayur', 2, 'Vishwas', 4.7, 'Hello']
    index = int(input('Ennter the index of collection: '))
    print(l1[index])
except IndexError:
    print(f'Please enter valid value till {len(l1)-1} or {-len(l1)}')
except ValueError:
    print('Please enter only integer type value')
'''
>>>
Ennter the index of collection: 3
4.7
'''

##2. WAP ask the user to enter one value and convert it into integer.(Handle value error)
try:
    value = input("Enter the value: ")
    convert_int = int(float(value))   
    print(convert_int)
except ValueError:
    print("Only numeric values can be converted into integer")
'''
>>>
Enter the value: 6.9
6
'''

##3. WAP to create one dictionary of student which name & marks of them. Ask the user to enter the name and display the marks.(Handle key error)
try:
    d3 = {'Suraj':90, 'Sudarshan':51, 'Varun':70, 'Mayur':99, 'Sohel':65}
    s_name = input('Enter the Student name: ')
    marks = d3[s_name]
    print(s_name, ':', marks)
except KeyError:
    print('Enter valid key of the dictionary collection', d3)
'''
>>>
Enter the Student name: Sudarshan
Sudarshan : 51
'''

