                                                                 #### Constructor ####
###Creating Asus Company Employee details using the methos called '__init__'
class Asus:
    def __init__(self, e_id, e_name=None, project_completed=None, post=None):
        self.Employee_ID = e_id
        self.Employee_Name = e_name
        self.Employee_Project_Completed = project_completed
        self.Post = post
        
CEO = Asus('e00')
CEO.CEO_Name = 'Mayur Jadhav'
CEO.post = 'CEO'
print(CEO.Employee_ID, CEO.CEO_Name, CEO.post)

Emp1 = Asus('e01', 'Datta Gavali', 17)
Emp1.Post = 'MD'
print(Emp1.Employee_ID, Emp1.Employee_Name, Emp1.Employee_Project_Completed, Emp1.Post)
Emp2 = Asus('e02', 'Amar Bansode', 27, 'Employee')
print(Emp2.Employee_ID, Emp2.Employee_Name, Emp2.Employee_Project_Completed, Emp2.Post)
Emp3 = Asus('e03', 'Trimbak Jagtap', 100, 'Employee')
print(Emp3.Employee_ID, Emp3.Employee_Name, Emp3.Employee_Project_Completed, Emp3.Post)
