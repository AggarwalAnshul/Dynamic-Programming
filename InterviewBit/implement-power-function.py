"""

[+]Temporal marker           : Thu, 22:15 | Feb 06, 20
[+]Temporal marker untethered: Thu, 22:15 | Feb 06, 20
[+]Comments                  :
[+]Level                     :
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/implement-power-function

"""


def findSolution(n, p, d):
    if(n==0):
        return 0
    if(p==0):
        return 1
    lis = [1]
    num = n
    temp = num % d
    while temp != lis[0]:
        lis.append(temp)
        num *= 3
        temp = num % d
        # print('num: '+str(num))
    repeat = len(lis)
    return lis[(p % repeat)]


data = [1234567, 546578, 254]
data = [0, 0, 1]
data = [213, 231, 1]
data = [ 71045970, 41535484, 64735492]
print(findSolution(data[0], data[1], data[2]))
"""
for x in range(1, 100000):
    # print('checking for x: '+str(x))
    count: int = 0
    if (data[0]**x)%data[2] != findSolution(data[0], x, data[2]):
        # print('false for the case: ', x)
        count+=1
print('wrong count is: '+str(count))
"""