                                                                    #### Constructor ####
###Creating Asus Company Employee details using the methos called '__init__'
class Asus:
    def __init__(self, e_id, e_name, project_completed): #constructor
        self.Employee_ID = e_id
        self.Employee_Name = e_name
        self.Employee_Project_Completed = project_completed

Emp1 = Asus('e01', 'Datta Gavali', 17)
print(Emp1.Employee_ID, Emp1.Employee_Name, Emp1.Employee_Project_Completed)
Emp2 = Asus('e02', 'Amar Bansode', 27)
print(Emp2.Employee_ID, Emp2.Employee_Name, Emp2.Employee_Project_Completed)
Emp3 = Asus('e03', 'Trimbak Jagtap', 100)
print(Emp3.Employee_ID, Emp3.Employee_Name, Emp3.Employee_Project_Completed)
