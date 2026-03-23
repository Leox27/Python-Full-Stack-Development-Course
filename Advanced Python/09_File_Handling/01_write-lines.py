###

a = open("X:/GitHub/QSpider/Python Full Stack Development/Advanced Python/09_File_Handling/writelines.txt", 'w')
data = ['I am Leo\n', 'I am a student\n', 'I am learning Python\n']
b = a.writelines(data)
a.close()

# The data is written in the file and the file is closed. The file name is writelines.txt.