if __name__ == '__main__':
    n = int(input())
    i=0
    while i<n:
        print(i*i)
        i += 1

'''
Task

The provided code stub reads an integer, n, from STDIN. For all non-negative integers
i < n, print i2.

Example
n=3

The list of non-negative integers that are less than n = 3 is [0, 1, 2]. Print the square of
each number on a separate line.
0
1
4

Input Format
The first and only line contains the integer, n.

Constraints
1<n≤20

Output Format
Print n lines, one corresponding to each i.

Sample Input O
5

Sample Output O
0
1
4
9
16
'''