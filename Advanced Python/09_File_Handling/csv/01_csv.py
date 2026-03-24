###For csv

##
import csv

with open(r"X:\GitHub\QSpider\Python Full Stack Development\Advanced Python\09_File_Handling\csv\01.csv", 'w') as a:
    b = csv.writer(a)
    b.writerows([[3, 4, 5, 6], [7, 8, 9, 10]])



'''
with open(r"X:\GitHub\QSpider\Python Full Stack Development\Advanced Python\09_File_Handling\csv\01.csv", "w", newline="") as a:
    b = csv.writer(a)
    b.writerow(["Name", "Age", "City"])
    b.writerow(["John", 25, "Mumbai"])
'''

with open(r"X:\GitHub\QSpider\Python Full Stack Development\Advanced Python\09_File_Handling\csv\01.csv", 'r') as a:
    b = csv.reader(a)
    print(list(b))
