"""
Minimum steps to minimize n as per given condition
Given a number n, count minimum steps to minimize it to 1 according to the following criteria:

If n is divisible by 2 then we may reduce n to n/2.
If n is divisible by 3 then you may reduce n to n/3.
Decrement n by 1.
Examples:

Input : n = 10
Output : 3

Input : 6
Output : 2

[+]Temporal marker             : 19:30 Hours | Aug24, Friday
[+]Temporal marker untethered  : 20:00 Hours | Aug24, Friday
[+]Tread speed                 : relaxed, waster tonnes of time due to incorrect GFG solution
                              during cross verification OX
[+]LINK: https://www.geeksforgeeks.org/minimum-steps-minimize-n-per-given-condition/
"""

import sys

def findMinimumStepMinimizeNPerCondition(n):
    dp = [0]*(n+1)

    #population of dp array | Tabulization
    for i in range(2,n+1):
        solutionByDivision = sys.maxsize

        if(i%3==0 and i%2==0):
            solutionByDivision = min(dp[int(i/3)], dp[int(i/2)])
        elif(i%3==0):
            solutionByDivision = dp[int(i/3)]
        elif(i%2==0):
            solutionByDivision = dp[int(i/2)]

        dp[i] = min(solutionByDivision, dp[i-1])+1
    return dp[n]

n = 689
print(findMinimumStepMinimizeNPerCondition(n))
