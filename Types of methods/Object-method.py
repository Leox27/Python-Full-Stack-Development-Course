                                                       #### Object Meethod ####

###Accessing & Modifying the object proprties or members

##Accessing the object properties
class School:
    def __init__(self, name, rollno): #Constructor
        self.name = name
        self.rollno = rollno
        
    def display(self): #Accessing the object members
        print(self.name, self.rollno)
        
Stu1=School('Datta Gavali', 101)
Stu2=School('Kashinaath Date', 102)

Stu1.display() #calling perticular object
Stu2.display() #calling perticular object
#print(Stu1.name, Stu1.rollno)
#print(Stu2.name, Stu2.rollno)
'''
>>>
Datta Gavali 101
Kashinaath Date 102
'''

##Modifying the object properties
class School:
    def __init__(self, name, rollno): #Constructor
        self.name = name
        self.rollno = rollno
        
    def display(self): #Accessing the object members
        print(self.name, self.rollno)

    def mod(self, new_name): #Modifying the object members
        self.name = new_name
        
Stu1=School('Datta Gavali', 101)
Stu2=School('Kashinaath Date', 102)

Stu1.display() #calling perticular object
Stu2.display() #calling perticular object
Stu1.mod('Sanjay Shinde')
Stu1.display()
'''
>>>
Datta Gavali 101
Kashinaath Date 102
Sanjay Shinde 101
'''













