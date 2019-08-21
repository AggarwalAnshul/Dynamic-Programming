"""
Maximum number of segments of lengths a, b and c
Given a positive integer N, find the maximum number of segments of lengths a, b and c that can be formed from N .

Examples :

Input : N = 7, a = 5, b, = 2, c = 5 
Output : 2 
N can be divided into 2 segments of lengths
2 and 5. For the second example,

Input : N = 17, a = 2, b = 1, c = 3 
Output : 17 
N can be divided into 17 segments of 1 or 8 
segments of 2 and 1 segment of 1. But 17 segments
of 1 is greater than 9 segments of 2 and 1.

LINK: https://www.geeksforgeeks.org/maximum-number-segments-lengths-b-c/
"""

import math
import sys

def printMatrix(dp):
    i = 0
    for x in dp:
        print(str(i)+" : ", end=" ")
        for y in x:
            print(y, end=" " )
        print()
        i+=1

def findMaximumNumberOfSegmentsRecursive(n, lis, segments):
    if(n<0):
        return (-sys.maxsize -1)
    if(n==0):
        return segments
    return max(findMaximumNumberOfSegmentsRecursive(n-lis[0], lis, segments+1),
                findMaximumNumberOfSegmentsRecursive(n-lis[1], lis, segments+1),
               findMaximumNumberOfSegmentsRecursive(n-lis[2], lis, segments+1))

def findMaximumNumberOfSegments(n, lis):
    dp = [(-sys.maxsize-1)]*(n+1)
    dp[0] = 1
    choiceA = 0
    choiceB = 0
    choiceC = 0
    for i in range(1, n+1):
        if(i-lis[0]>=0):
            choiceA = dp[i-lis[0]]+1
        if(i-lis[1] >= 0):
            choiceB = dp[i-lis[1]]+1
        if(i-lis[2] >= 0):
            choiceC = dp[i-lis[2]]+1
        dp[i] = max(0, choiceA, choiceB, choiceC)
    #print(dp)
    return dp[n]-1;

"""
def findMaximumNumberOfSegments(n, lis):
    length = n
    dp = [[0]*4 for x in range(n+1)]
    dp[0] = [1]*4
    temp = 0
      
    for i in range(1, length+1):
        for j in range(1, 4):
            #print(i,j)
            temp = 0
            if(dp[i%lis[j-1]][j-1]!=0):
                temp = math.floor(i/lis[j-1]) + dp[i%lis[j-1]][j-1]
            dp[i][j]  = max(dp[i][j-1], temp)

    printMatrix(dp)
    return dp[length][3]-1
    """

n = 1756
a = 8
b = 2
c = 5
lis = [a,b,c]

#print(findMaximumNumberOfSegmentsRecursive(n, lis, 0))
print(findMaximumNumberOfSegments(n, lis))
