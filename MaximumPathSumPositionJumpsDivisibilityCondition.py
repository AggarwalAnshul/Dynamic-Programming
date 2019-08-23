"""
Maximum path sum for each position with jumps under divisibility condition
Given an array of n positive integers. Initially we are at first position. We can jump to position y (1 <= x <= n) from position x (1 <= x <= n) if x divides y and x < y. The task is to print maximum sum path ending at every position x.

Note : Since first element is at position 1, we can jump to any position from here as 1 divides all other position numbers.

Examples :

Input :  arr[] = {2, 3, 1, 4, 6, 5}
Output : 2 5 3 9 8 10
Maximum sum path ending with position 1 is 2.
For position 1, last position to visit is 1 only.
So maximum sum for position 1 = 2.

Maximum sum path ending with position 2 is 5.
For position 2, path can be jump from position 1 
to 2 as 1 divides 2.
So maximum sum for position 2 = 2 + 3 = 5.

For position 3, path can be jump from position 1 
to 3 as 1 divides 3.
So maximum sum for position 3 = 2 + 3 = 5.

For position 4, path can be jump from position 1
to 2 and 2 to 4.
So maximum sum for position 4 = 2 + 3 + 4 = 9.

For position 5, path can be jump from position 1 
to 5.
So maximum sum for position 5 = 2 + 6 = 8.

For position 6, path can be jump from position 
1 to 2 and 2 to 6 or 1 to 3 and 3 to 6.
But path 1 -> 2 -> 6 gives maximum sum for
position 6 = 2 + 3 + 5 = 10.

Temporal Marker               : 10:06:33 Hours | Aug23, Friday
Tempral Marker Untethered     : 1019:39 Hours | Aug23, Friday
Tread Speed                   : Relax, could have done way faster, talked to Dad amidst!
LINK: https://www.geeksforgeeks.org/maximum-path-sum-position-jumps-divisibility-condition/
"""

import math
def findMaximumPathSumPositionJumpsDivisibilityCondition(lis):
    length = len(lis)
    dp = [0]*(length)
    dp[0] = lis[0]

    print("The orignal list is: "+str(lis))
    for i in range(0, length):
        localMax = 0
        for j in range(0, i):
            if((i+1)%(j+1)==0):
                localMax = max(localMax, dp[j])
        dp[i] = lis[i]+localMax
        print(dp[i], end=" ")
        
lis = [2, 3, 1, 4, 6, 5]
findMaximumPathSumPositionJumpsDivisibilityCondition(lis)
