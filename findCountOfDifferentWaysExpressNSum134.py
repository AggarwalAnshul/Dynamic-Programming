"""
Count of different ways to express N as the sum of 1, 3 and 4
Given N, count the number of ways to express N as sum of 1, 3 and 4.

Examples:

Input :  N = 4
Output : 4 
Explanation: 1+1+1+1 
             1+3
             3+1 
             4 

Input : N = 5 
Output : 6
Explanation: 1 + 1 + 1 + 1 + 1
             1 + 4
             4 + 1
             1 + 1 + 3
             1 + 3 + 1
             3 + 1 + 1
[+]Temporal marker            : 09:47 Hours | Aug28, 2019
[+]Temporal marker untethered : 09:55 Hours | Aug28, 2019
[+]Tread speed                : Relaxed
[+]Comments                   : Similar to coin change problem with repetition
[+]LINK : https://www.geeksforgeeks.org/count-ofdifferent-ways-express-n-sum-1-3-4/
"""

#S-complexity: O(n) | T-Complexity: O(n)
def findCountOfDifferentWaysExpressNSum134(n):
    lis = [1,3,4]
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    
    for x in range(4, n+1):
        dp[x] = dp[x-1]+dp[x-3]+dp[x-4]
    return dp[n]

if __name__ == "__main__":
    print(findCountOfDifferentWaysExpressNSum134(5))

        
