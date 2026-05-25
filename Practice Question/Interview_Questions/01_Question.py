
from typing import List
"""
Question 1:
Rotate the elements of an array by k positions.
	* You are given an array of integers.
	* Ask the user to input:
	* The direction of rotation (`left` or `right`)
	* The number of positions `k`
	* If the direction is left, shift the elements towards the left by `k` positions.
	* If the direction is right, shift the elements towards the right by `k` positions.
	* The rotation should be circular, meaning elements shifted out from one side should reappear on the other side.

Input:
numbers = [1, 2, 3, 4, 5]
direction = right
k = 2

Output:
[4, 5, 1, 2, 3]

Input:
numbers = [1, 2, 3, 4, 5]
direction = left
k = 2

Output:
[3, 4, 5, 1, 2]

Constraints:
* Do not use `while` loops
* Use only `for` loops for iteration
* Do not use inbuilt rotation functions
"""

def rotate(numbers: List[int], direction: str, k: int) -> List[int]:
    if direction == 'right':
        for i in range(k):
            pop = numbers.pop()
            numbers.insert(0, pop)
    elif direction == 'left':
        for i in range(k):
            pop = numbers.pop(0)
            numbers.append(pop)
    return numbers
print(rotate([1, 2, 3, 4, 5], 'right', 2))
print(rotate([1, 2, 3, 4, 5], 'left', 2))
'''
>>>
[4, 5, 1, 2, 3]
[3, 4, 5, 1, 2]
'''


'''
Question 2:
Find all the leaders in an array.
	* A leader is an element that is greater than or equal to all the elements to its right.
	* You are given an array of integers.
	* Traverse the array to identify all such leader elements.
	* A leader should satisfy the condition:
	* It must be greater than or equal to every element on its right side.
	* Store all the leader elements in a list and display the result.

Input:
arr = [9, 10, 2, 4, 8, 5]

Output:
[10, 8, 5]

Input:
arr = [16, 17, 4, 3, 5, 2]

Output:
[17, 5, 2]

Constraints:
	* Use only loops for traversal
	* Do not use unnecessary extra variables like flags
	* Avoid using built-in functions for direct computation
	* The solution should correctly check all elements to the right of each element
'''

def Leaders(arr: List[int]) -> List[int]:
    o_list = []
    for i in range(len(arr)):
        count = 0
        for k in range(i+1, len(arr)):
            if arr[k] > arr[i]:
                count += 1
        if count == 0:
            o_list.append(arr[i])
    return o_list
print(Leaders([9, 10, 2, 4, 8, 5]))
print(Leaders([16, 17, 4, 3, 5, 2]))
'''
>>>
[10, 8, 5]
[17, 5, 2]
'''

