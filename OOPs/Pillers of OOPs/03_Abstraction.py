###Abstraction

from abc import ABC, abstractmethod

class A(ABC):    
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class F_Car(A):
    def start(self):
        print('Fuel car has started')
    # def stop(self):
    #     print('Fuel car has stopped')

class E_Car(A):
    def start(self):
        print('Electric car has started')
    def stop(self):
        print('Electric car has stopped')

obj1 = F_Car()
obj1.start()
obj1.stop()

obj2 = E_Car()
obj2.start()
obj2.stop()
'''
>>>
Traceback (most recent call last):
  File "x:\GitHub\QSpider\Python Full Stack Development\OOPs\Pillers of OOPs\03_Abstraction.py", line 25, in <module>
    obj1 = F_Car()
TypeError: Can't instantiate abstract class F_Car without an implementation for abstract method 'stop'
'''
# we can not create object of abstract class and we can not create object of child class if it does not implement all the abstract methods of parent class.

# In case of E_Car, we can create object because it implements all the abstract methods of parent class.
# In case of F_Car, we can not create object because it does not implement all the abstract methods of parent class.
    
    