###Restaurant Example

class Restaurant:  # Parent class
    R_name = "Thalapakatti"
    menu = {
        "thalapakatti biriyani": 250,
        "mutton biriyani": 300,
        "chicken biriyani": 200, 
        "veg biriyani": 150,
        "paneer tikka": 110,
        "coke": 80,
        "chocolate ice cream": 100
    }

    @classmethod
    def disp_menu(cls):
        print("!--- Menu ---$")
        for item, price in cls.menu.items():
            print(item, ":", price)

class Swiggy(Restaurant):  # Child class 1
    def __init__(self, name, addr, phno):
        self.name = name
        self.addr = addr
        self.phno = phno
        self.cart = {}

    def order(self): #Object method
        Restaurant.disp_menu()

        print("Reply with 'Done' when you done with order 🙌")
        while True:
            item = input("Enter item: ")
            if item in Restaurant.menu: #Accessing class-properties using class-name
                self.cart[item] = Restaurant.menu[item]
                print(f"{item} added to cart")
            elif item=='Done':
                break
            else:
                print(f"{item} is not available")
        
    def disp_cart(self): #Object method
        print("---- Your Cart ----")
        print(self.cart)

    def total_bill(self): #Object method
        total = 0
        for item in self.cart:
            total += self.cart[item]

        print("Total bill: Rs.", total)

class Zomato(Restaurant):  # Child class 2
    def __init__(self, name, addr, phno):
        self.name = name
        self.addr = addr
        self.phno = phno
        self.cart = {}

    def order(self): #Object method
        Restaurant.disp_menu()

        print("Reply with 'Done' when you done with order 🙌")
        while True:
            item = input("Enter item: ")
            if item in Restaurant.menu: #Accessing class-properties using class-name
                self.cart[item] = Restaurant.menu[item]
                print(f"{item} added to cart")
            elif item=='Done':
                break
            else:
                print(f"{item} is not available")

    def disp_cart(self): #Object method
        print("---- Your Cart ----")
        print(self.cart)

    def total_bill(self): #Object method
        total = 0
        for item in self.cart:
            total += self.cart[item]

        print("Total bill: Rs.", total)

# Objects
cust1 = Swiggy("Rajesh", "Chennai", 8990897889)
cust1.order()
cust1.disp_cart()
cust1.total_bill()

print("Enter 'Next' to move to Zomato")
next = input("Enter: ")
if next == 'Next':
    print("Moving to Zomato")

cust2 = Zomato("Boopesh", "Bangalore", 9089908978)
cust2.order()
cust2.disp_cart()
cust2.total_bill()

'''
>>>
!--- Menu ---$
thalapakatti biriyani : 250
mutton biriyani : 300
chicken biriyani : 200
veg biriyani : 150
paneer tikka : 110
coke : 80
chocolate ice cream : 100
Reply with 'Done' when you done with order 🙌
Enter item: paneer tikka
paneer tikka added to cart
Enter item: coke
coke added to cart
Enter item: Done
---- Your Cart ----
{'paneer tikka': 110, 'coke': 80}
Total bill: Rs. 190
Enter 'Next' to move to Zomato
Enter: Next
Moving to Zomato
!--- Menu ---$
thalapakatti biriyani : 250
mutton biriyani : 300
chicken biriyani : 200
veg biriyani : 150
paneer tikka : 110
coke : 80
chocolate ice cream : 100
Reply with 'Done' when you done with order 🙌
Enter item: veg biriyani
veg biriyani added to cart
Enter item: chocolate ice cream
chocolate ice cream added to cart
Enter item: Done
---- Your Cart ----
{'veg biriyani': 150, 'chocolate ice cream': 100}
Total bill: Rs. 250
'''