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
number = int(input("Enter a number that is smaller than 10"))
nums = range(1, number)
tnum = 1
onum = int(1)
fnum = int(0)
for x in nums:
    onum = str(onum)
    onum = onum + "1"
    onum = int(onum)
    fnum = fnum + onum
fnum = fnum + 1
fnum = str(fnum)
print("the sum of the series is " + fnum)
