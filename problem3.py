#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""

x=input("Input a number that is smaller than 10: ")
x=int(x)
y=range(1,x)
w=int(1)
z=int(0)
for o in y:
    w=str(w)
    w=w+"1"
    w=int(w)
    z=z+w
z=z+1
z=str(z)
print("the sum of the series is "+z)