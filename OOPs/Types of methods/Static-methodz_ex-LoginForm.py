###Login Form

class LoginForm:
    def __init__(self, name, rollno, phno, email):
        self.Name = name
        self.RollNo = rollno
        self.PhNo = phno
        self.Email = email

    # staticmethod for valid Phone no
    @staticmethod
    def valid_phno(phno):
        str_phno = str(phno)
        if len(str_phno) == 10:
            if '6'<=str_phno[0]<='9':
                return True            
            else:
                return False
        else:
            return False

    # staticmethod for valid email
    @staticmethod
    def valid_email(email):
        if '@gmail.com' in email:
            return True
        else:
            return False
    
    def static_display(self):
        if self.valid_phno(self.PhNo) == False and self.valid_email(self.Email) == False:
            print(f"Invalid Phone number {self.PhNo} and Invalid Email {self.Email} of {self.Name}")
        elif self.valid_phno(self.PhNo) == False:
            print(f"Invalid Phone number {self.PhNo} of {self.Name}")
        elif self.valid_email(self.Email) == False:
            print(f"Invalid Email {self.Email} of {self.Name}")
        else:
            print(self.Name, self.RollNo, self.PhNo, self.Email)

user1 = LoginForm("Vishwas Vedpathak", 324, 9309344770, "vishwas@gmail.com")
user1.static_display()
print()

user2 = LoginForm("Mayur Jadhav", 321, +918999027124, "Mayurx27@gmail.com")
user2.static_display()
print()

user3 = LoginForm("varun Mane", 344, 9120344556, "varungmail.com")
user3.static_display()

'''
>>>
Vishwas Vedpathak 324 9309344770 vishwas@gmail.com

Invalid Phone number 918999027124 of Mayur Jadhav

Invalid Email varungmail.com of varun Mane
'''