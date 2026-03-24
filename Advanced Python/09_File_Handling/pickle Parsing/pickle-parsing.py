
'''
#Sender:
Take one list of numbers from 1 to 10 convert into string form check with the tyow of the collection befire and after the collectuin create one text file and write this data into the same file. 
'''

import pickle

data = [x for x in range(1, 11)]
b = pickle.dumps(data)
print(data, type(data))
print(b, type(b))

with open(r"X:\GitHub\QSpider\Python Full Stack Development\Advanced Python\09_File_Handling\pickle Parsing\parsing-by-pickle.pkl", 'wb') as a:
    a = a.write(b)


'''
#Receiver:
Read the file and then convert it to ita original form after doing the conversion again check the type of data
'''
with open(r"X:\GitHub\QSpider\Python Full Stack Development\Advanced Python\09_File_Handling\pickle Parsing\parsing-by-pickle.pkl", 'rb') as a:
    a = a.read()
    b = pickle.loads(a)
    print(a, type(a))
    print(b, type(b))

    