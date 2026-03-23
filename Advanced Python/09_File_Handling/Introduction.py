####

a = open("X:/GitHub/QSpider/Python Full Stack Development/Advanced Python/09_File_Handling/introduction.txt", 'a')
data = ['I am Mayur Jadhav. I am originally from Solapur, currently living in Pune.\n', 'Currently I am pursuing Btech in E&TC at BMIT college.\n', 'Along with my degree I have enrolled in the skill development courses at QSpider.\n', 'My technical skills are Python, SQL in MySQL & Oracle, etc.\n', 'I have some projects that is in my academics I have completed a project on the Smart Car Parking System and i have some self-paced projects that are Weather forecasting using FB Prophet, Classification of Dogs vs cats using CNN, Diabattes data prediction using KNN\n', 'My career objective is i want to get a job in a reputated comapany and work with professionals with real datasets\n']
b = a.writelines(data)
a.close()

# The data is added in the file and the file is closed. The file name is introduction.txt.
# The data is added in the file using writelines() method and the file is closed. The writelines() method writes a list of strings to the file. Each string in the list is written as a separate line in the file.