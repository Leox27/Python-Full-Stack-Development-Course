
###Iterator

'''
#syntax
try:
    // code
except TypeOfError:
    // display
'''

##
l1 = [1, 2, 3, 4]
a = iter(l1)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
'''
>>>
1
2
3
4
Traceback (most recent call last):
  File "x:\GitHub\QSpider\04_Iterator\01_Iterator.py", line 17, in <module>
    print(next(a))
          ~~~~^^^
StopIteration
'''

