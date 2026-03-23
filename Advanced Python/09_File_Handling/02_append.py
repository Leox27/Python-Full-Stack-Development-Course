###

a = open("X:/GitHub/QSpider/Python Full Stack Development/Advanced Python/09_File_Handling/append.txt", 'a')
data = ['Meet my friend tiger\n', 'He is a good boy\n', 'He is my best friend\n']
b = a.writelines(data)

data2 = ['Meet my 2nd friend\n', 'He is a good boy\n', 'He is my best friend\n']
b = a.writelines(data2)
a.close()

# The data is added in the file and the file is closed. The file name is append.txt.