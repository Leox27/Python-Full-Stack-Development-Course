###

a = open("X:/GitHub/QSpider/Python Full Stack Development/Advanced Python/09_File_Handling/writelines.txt", 'r')
b = a.readline()
print(b)
a.close()
'''
>>>
I am Leo

'''

# From the writelines.txt file, we have read the data using readline() method and stored it in variable b and then printed it.
# The readline() method reads only the first line of the file and returns it as a string. The file is then closed.