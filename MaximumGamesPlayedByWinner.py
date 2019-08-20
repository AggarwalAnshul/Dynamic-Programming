"""

+)This solution is not correct, testCase #5 was failed on codeforces
+)No Solution to the problem has been found yet
+)GeeksForGeeks Solution is incorrect, Check when n=8
+)Until further insight, this problem has been marked as incompleted|Pending

Temporal Maker: 11:21 Hours | Aug19, Monday
Temporal marketer untethered: 13:29 | Aug 19, Monday
"""

import math

def findSolution(n, lis):
    if( lis[n]==0 ):
        #comput the value
        #print("\t  Ceil for n: "+str(math.ceil(n/2)))
        lis[n] = findSolution(math.ceil(n/2), lis)+1
        return lis[n]
    else:
        return lis[n]



n = 50
lis = [0]*(n+1)
lis[2] = 1

#print("3: "+str(findSolution(3, lis)))
for x in range(4, n+1):
    a = findSolution(x, lis)
    print(str(x)+ " : " +str(a))
