"""
Maximum Length Chain of Pairs | DP-20
You are given n pairs of numbers. In every pair, the first number is always
smaller than the second number. A pair (c, d) can follow another pair (a, b)
if b < c. --> (a,b)-->(c,d)
Chain of pairs can be formed in this fashion. Find the longest chain which
can be formed from a given set of pairs.
Source: Amazon Interview | Set 2

For example, if the given pairs are {{5, 24}, {39, 60}, {15, 28}, {27, 40}, {50, 90} }, then the longest chain that can be formed is of length 3, and the chain is {{5, 24}, {27, 40}, {50, 90}}

Temporal Marker: 10:48:20 Hours | Aug20 Tuesday
Temporal Marker untethered: 11:45 Hours | Aug20 Tuesday

LINK: https://www.geeksforgeeks.org/print-maximum-length-chain-of-pairs/
"""

def findMaximumLengthChainOfPairs(lis):
    length = len(lis)
    lis.sort()  #sorting on the basis of first element
    localMax =[[0]*2] 
    dp = [[0,-1] for x in range(length)] #Creating a dp aux space 
    globalMax = 0 #Variable for tracking max length or last element of max chain
    
    for x in range(1, length):
        localMax[0][0] = 0
        localMax[0][1] = -1
        for y in range(0, x):
            if(lis[y][1] < lis[x][0]):
                #condition satisfied
                if(dp[y][0]+1 > localMax[0][0]):
                    localMax[0][0] = dp[y][0]+1
                    localMax[0][1] = y
        dp[x][0] = localMax[0][0]
        dp[x][1] = localMax[0][1]
        if(dp[globalMax][0] < dp[x][0]):
            globalMax = x


    print('The longest pair chain length is:'+str(dp[globalMax][1]+1))
    #Printing the lis
    index = globalMax
    while(index!=-1):
        print(lis[index], end=" ")
        index = dp[index][1]
    

#lis = [[5, 24], [39, 60], [15, 28], [27, 40], [50, 90]]
lis =[[11, 20], [10, 40], [45, 60], [39, 40]]
findMaximumLengthChainOfPairs(lis)
