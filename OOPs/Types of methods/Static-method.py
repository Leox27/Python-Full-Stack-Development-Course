                                                       #### Static Method ####
###Static method have access of both object & class
class School:
    s_name = 'BMIT'
    s_loc = 'Solapur'
    def __init__(self, name, rollno): #Constructor
        self.name = name
        self.rollno = rollno
        
    def display(self): 
        print(self.name, self.rollno)
        self.info()
        
    def mod(self, new_name): 
        self.name = new_name
        self.info()

    @staticmethod # decorator of staticmethod
    def info():
        print("Static can here object as well as class")
        
    @classmethod #classmethod to "access" the class members
    def displayclass(cls):
        print(cls.s_name, cls.s_loc)
        cls.info()
        
    @classmethod #classmethod to "modify" the class members
    def mod_class(cld, new_school_name, new_loc): ##Modifying the class members
        cld.s_name = new_school_name
        cld.s_loc = new_loc
        
Stu1=School('Datta Gavali', 101)
Stu2=School('Kashinaath Date', 102)

Stu1.display() #calling perticular object
Stu2.display() #calling perticular object
Stu1.mod('Sanjay Shinde')
Stu1.display()


School.displayclass() #calling display class 
School.mod_class('Z. P.', 'Degaon') #modified the class member
School.displayclass() #calling again for display class
