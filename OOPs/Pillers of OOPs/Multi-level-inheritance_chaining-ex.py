###Resume Exapmle

class Resume10th:
    Rname="10th Resume"

    def __init__(self, name, phno, email, address, ten_yop, ten_marks):
        self.name=name
        self.phno=phno
        self.email=email
        self.address=address
        self.ten_yop=ten_yop
        self.ten_marks=ten_marks

    def display(self):
        print("Name: ", self.name)
        print("Phone No.: ", self.phno)
        print("Email: ", self.email)
        print("Address: ", self.address)
        print("10th YOP: ", self.ten_yop)
        print("10th Marks: ", self.ten_marks)

class Resume12th(Resume10th):

    def __init__(self, name, phno, email, address, ten_yop, ten_marks, twelve_yop, twelve_marks):
        super().__init__(name, phno, email, address, ten_yop, ten_marks)
        self.twelve_yop=twelve_yop
        self.twelve_marks=twelve_marks

    def display(self):
        super().display()
        print("12th YOP: ", self.twelve_yop)
        print("12th Marks: ", self.twelve_marks)

class ResumeBtech(Resume12th):

    def __init__(self, name, phno, email, address, ten_yop, ten_marks, twelve_yop, twelve_marks, btech_yop, btech_marks):
        super().__init__(name, phno, email, address, ten_yop, ten_marks, twelve_yop, twelve_marks)
        self.btech_yop=btech_yop
        self.btech_marks=btech_marks

    def display(self):
        super().display()
        print("Btech YOP: ", self.btech_yop)
        print("Btech Marks: ", self.btech_marks)

student1=ResumeBtech("Mayur Jadhav", 8999057123, "mayur@gmail.com", "Degaon Solapur", 2020, 79.60, 2022, 50.33, 79.07, 2026)
student1.display()

'''
>>>
Name:  Mayur Jadhav
Phone No.:  8999057123
Email:  mayur@gmail.com
Address:  Degaon Solapur
10th YOP:  2020
10th Marks:  79.6
12th YOP:  2022
12th Marks:  50.33
Btech YOP:  79.07
Btech Marks:  2026
'''