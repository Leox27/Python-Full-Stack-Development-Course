                                                    #### Single-Level Inheritance ####

###This is the single level inheritance where the only the one parent will be there and only the single child.
##
class Mobile:
    tell_me='telle me'
    processor='Mediatek dimensiy'
    RAM='16 GB'
    ROM='256 GB'

    def __init__(self, Global):
        self.Global=Global

class Huawei(Mobile):
    color='Maroon'
    OS='Oxygen OS'

Obj1=Huawei('No')
Obj1.processor='SnapdragonGen7'
print(Mobile.tell_me, 'is Huawei company is global', Obj1.Global, Huawei.color, Huawei.OS, Obj1.processor)

#print(Obj1.processor)
#print(Mobile.RAM)


##Banking system
class Bank: #Parent class
    bank_name = "Indian bank"
    loc = "chennai"
    
    def __init__(self, name, ph_no, ac_no, pin, bal=1000):
        self.name = name
        self.phno = ph_no
        self.acno = ac_no
        self.pin = pin
        self.bal = bal

class ATM(Bank): #Child class
    @staticmethod
    def get_pin():
        pin = int(input("Enter pin: "))
        return pin
    
    def check_bal(self):
        pin = self.get_pin()
        
        if pin == self.pin:
            print(f"Available bal: Rs. {self.bal}")
        else:
            print("Incorrect Pin")
            
    def deposit(self):
        pin = self.get_pin()
        
        if pin==self.pin:
            amt = int(input("Enter amount: "))
            self.bal += amt 
            print(f"Amount of Rs. {amt} deposited successfully")
            print(f"Total current balance is {self.bal}.")
        else:
            print("Incorrect Pin")

    def withdraw(self):
        pin = self.get_pin()
        
        if pin == self.pin:
            amt = int(input("Enter amount: "))
            if amt<=self.bal:
                self.bal-=amt
                print(f"Amount of Rs. {amt} withdraw successfull")
                print(f"Total current balance is {self.bal}.")
            else:
                print("Insufficent funds ")
        else:
            print("Incorrect pin ")
    
c1 = ATM("Kashinath Date",9089788978,456789567890,2315)
c2 = ATM("Suraj Lohar",8990897889,234567456234,2007)

c1.check_bal()
c1.deposit()
c1.withdraw()
