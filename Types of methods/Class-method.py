                                                        #### Class Method ####
###Accessing & Modifying the Class Properties or members

##Accessing the class members
class School:
    s_name = 'BMIT'
    s_loc = 'Solapur'
    
    def __init__(self, name, rollno): #Constructor
        self.name = name
        self.rollno = rollno
        
    def display(self): #Accessing the object members
        print(self.name, self.rollno)

    @classmethod #classmethod to "access" the class members
    def displayclass(cls):
        print(cls.s_name, cls.s_loc)  
        
Stu1=School('Datta Gavali', 101)
Stu2=School('Kashinaath Date', 102)

Stu1.display() #calling perticular object
Stu2.display() #calling perticular object
School.displayclass()
'''
>>>
Datta Gavali 101
Kashinaath Date 102
BMIT Solapur
'''


##Modifying the class properties
class School:
    s_name = 'BMIT'
    s_loc = 'Solapur'
    def __init__(self, name, rollno): #Constructor
        self.name = name
        self.rollno = rollno
        
    def display(self): 
        print(self.name, self.rollno)

    def mod(self, new_name): 
        self.name = new_name

    @classmethod #classmethod to "access" the class members
    def displayclass(cls):
        print(cls.s_name, cls.s_loc)
        
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
'''
>>>
Datta Gavali 101
Kashinaath Date 102
Sanjay Shinde 101
BMIT Solapur
Z. P. Degaon
'''
