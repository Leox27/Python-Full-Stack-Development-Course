##Banking system

class Bank: #Parent class
    bank_name = "Indian bank"
    loc = "Chennai"
    
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

c2.check_bal()
c2.deposit()
c2.withdraw()
'''
>>>
Enter pin: 2007
Available bal: Rs. 1000
Enter pin: 2007
Enter amount: 3000
Amount of Rs. 3000 deposited successfully
Total current balance is 4000.
Enter pin: 2007
Enter amount: 3000
Amount of Rs. 3000 withdraw successfull
Total current balance is 1000.
'''