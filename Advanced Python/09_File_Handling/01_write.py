###

a = open("X:/GitHub/QSpider/Python Full Stack Development/Advanced Python/09_File_Handling/write.txt", 'w')
data = 'I am Leo'
b = a.write(data)
a.close()

# The data is written in the file and the file is closed. The file name is write.txt.