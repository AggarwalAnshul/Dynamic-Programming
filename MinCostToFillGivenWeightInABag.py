"""
Minimum cost to fill given weight in a bag
You are given a bag of size W kg and you are provided costs of packets different weights of oranges in array cost[] where cost[i] is basically cost of ‘i’ kg packet of oranges. Where cost[i] = -1 means that ‘i’ kg packet of orange is unavailable

Find the minimum total cost to buy exactly W kg oranges and if it is not possible to buy exactly W kg oranges then print -1. It may be assumed that there is infinite supply of all available packet types.

Note : array starts from index 1.
Examples:

Input  : W = 5, cost[] = {20, 10, 4, 50, 100}
Output : 14
We can choose two oranges to minimize cost. First 
orange of 2Kg and cost 10. Second orange of 3Kg
and cost 4. 

Input  : W = 5, cost[] = {1, 10, 4, 50, 100}
Output : 5
We can choose five oranges of weight 1 kg.

Input  : W = 5, cost[] = {1, 2, 3, 4, 5}
Output : 5
Costs of 1, 2, 3, 4 and 5 kg packets are 1, 2, 3, 
4 and 5 Rs respectively. 
We choose packet of 5kg having cost 5 for minimum
cost to get 5Kg oranges.

Input  : W = 5, cost[] = {-1, -1, 4, 5, -1}
Output : -1
Packets of size 1, 2 and 5 kg are unavailable
because they have cost -1. Cost of 3 kg packet 
is 4 Rs and of 4 kg is 5 Rs. Here we have only 
weights 3 and 4 so by using these two we can  
not make exactly W kg weight, therefore answer 
is -1.

Temporal Marker           : 16:26 Hours | Aug24, Saturday
Temporal Marker untethered: 15:30 Hours | Aug24, Saturday
Tread speed               : Relaxed, Istalled Flatscreen Amidst :D
LINK                      : https://www.geeksforgeeks.org/minimum-cost-to-fill-given-weight-in-a-bag/
"""
import PrintMatrix as pm
import sys
def findMinCostToFillGivenWeightInABag(lis, W):
    length = len(lis)
    dp = [[0]*(length+1) for x in range(W+1)]

    #init
    for j in range(0, length+1):
        dp[0][j] = 0
    for i in range(0, W+1):
        dp[i][0] = 0

    #Population
    for i in range(1, W+1):
        localMin = sys.maxsize
        for j in range(1, length+1):
            if(i>=j and lis[j-1]!=-1):
                if(dp[i-j]!=sys.maxsize  or i-j==0):#When this weight can be used
                    dp[i][j] = lis[j-1] + dp[i-j][j]
                    if(dp[i][j]!=-1):
                        localMin = min(localMin, dp[i][j])
            dp[i][j] = localMin
        #pm.printMatrix(dp)

    if(dp[W][length]==sys.maxsize):
        return -1
    return dp[W][length]

#lis = [-1, -1, 4, 5, -1]
#lis = [1, 2, 3, 4, 5]
#lis = [1, 10, 4, 50, 100]
lis = [20, 10, 4, 50, 100]
W = 5
print(findMinCostToFillGivenWeightInABag(lis, W))





""
