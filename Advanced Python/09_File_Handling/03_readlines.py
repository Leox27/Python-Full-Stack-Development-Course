###

a = open("X:/GitHub/QSpider/Python Full Stack Development/Advanced Python/09_File_Handling/writelines.txt", 'r')
b = a.readlines()
print(b)
a.close()
'''
>>>
['I am Leo\n', 'I am a student\n', 'I am learning Python\n']
'''

# From the writelines.txt file, we have read the data using readlines() method and stored it in variable b and then printed it.
# The readlines() method reads all the lines of the file and returns them as a list of strings. The file is then closed.