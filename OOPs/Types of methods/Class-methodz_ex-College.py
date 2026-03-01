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

    ##classmethod--> Accessing
    @classmethod
    def class_display(cls):
        print(cls.clg_name, cls.clg_loc, cls.principal)
    
    ##classmethod--> Modifying the Location
    @classmethod
    def class_mod_loc(cld, new_loc):
        cld.clg_loc = new_loc

S1 = College("Datta Gavali", 337, "Data Analysis", 7878898909)
S2 = College("Amar Bansode", 305, "Robitics", 8978907845)

S1.display()
S2.display()

print()

print("Before modifying the Output is -")
S1.class_display()
S2.class_display()

print()

print("After modifying the Output is -")
S2.class_mod_loc("Mumbai")
S2.class_display()

S1.class_mod_loc("Latur")
S1.class_display()

'''
>>>
Datta Gavali 337 Data Analysis 7878898909
Amar Bansode 305 Robitics 8978907845

Before modifying the Output is -
Sambhajirao Shinde Arta & Commerce Jr. College Solapur Chabukswar
Sambhajirao Shinde Arta & Commerce Jr. College Solapur Chabukswar

After modifying the Output is -
Sambhajirao Shinde Arta & Commerce Jr. College Mumbai Chabukswar
Sambhajirao Shinde Arta & Commerce Jr. College Latur Chabukswar
'''