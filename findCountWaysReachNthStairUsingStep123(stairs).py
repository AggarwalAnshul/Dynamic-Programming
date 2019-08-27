"""
Count ways to reach the nth stair using step 1, 2 or 3
A child is running up a staircase with n steps and can hop either
1 step, 2 steps, or 3 steps at a time. Implement a method to count
how many possible ways the child can run up the stairs.

There are two methods to solve this problem
1. Recursive Method
2. Dynamic Programming

Examples :

Input : 4
Output : 7

Input : 3
Output : 4

[+]Temporal marker            : N/A, Couldn't solve
[+]Temporal marker untethered : N/A
[+]Tread speed                : Paced
[+]Comments                   : Referred to solution from GFG
[+]LINK : https://www.geeksforgeeks.org/count-ways-reach-nth-stair-using-step-1-2-3/

"""

def findCountWaysReachNthStairUsingStep123(stairs):
    dp = [0]*(stairs+1)
    dp[0] = 1
    dp[1]= 1
    dp[2] = 2

    for i in range(3, stairs+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    return dp[stairs]

stairs = 3
print(findCountWaysReachNthStairUsingStep123(stairs))
    
