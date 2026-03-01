###College exapmle

class College:
    clg_name = "Sambhajirao Shinde Arta & Commerce Jr. College"
    clg_loc = "Solapur"
    principal = "Chabukswar"

    def __init__(self, name, rollno, dept, phno):
        self.Name = name
        self.RollNo = rollno
        self.Dept = dept
        self.PhNo = phno

    # Object method --> Accessing 
    def display(self):
        print(self.Name, self.RollNo, self.Dept, self.PhNo)

    # Object method --> Modifying the RollNo
    def ch_rollno(self, new_rollno):
        self.RollNo = new_rollno

    # Object method --> Modifying the Dept
    def ch_dept(self, new_dept):
        self.dept = new_dept

S1 = College("Suraj Lohar", 301, "R & D", 7745877124)
S2 = College("Mayur Jadhav", 302, "IT", 7218734567)

S1.display()
S2.display()

S1.ch_rollno(321)
S1.display()

S2.ch_dept(" R & D")
S2.display()

'''
>>>
Suraj Lohar 301 R & D 7745877124
Mayur Jadhav 302 IT 7218734567
Suraj Lohar 321 R & D 7745877124
Mayur Jadhav 302 IT 7218734567
'''