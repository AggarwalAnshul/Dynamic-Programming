
#87
"""
Count number of ways to cover a distance
Given a distance ‘dist, count total number of ways to cover the distance
with 1, 2 and 3 steps.

Examples :

Input:  n = 3
Output: 4
Below are the four ways
 1 step + 1 step + 1 step
 1 step + 2 step
 2 step + 1 step
 3 step

Input:  n = 4
Output: 7

[+]Temporal marker            : 11:45 Hours | Aug29, 2019
[+]Temporal marker untethered : 11:50 Hours | Aug29, 2019
[+]Tread speed                : Relaxed 
[+]Comments                   : Easy, knew the approach, just implemented soln 
[+]LINK : https://www.geeksforgeeks.org/count-number-of-ways-to-cover-a-distance/
"""

#S-Complexity: O(n) | T-Complexity-O(n)
def countTotalWaysToCoverDistance(dis):
    dp = [0]*(dis+3)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, dis+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    return dp[dis]

dis = 3
dis = 4
dis = 22
print(countTotalWaysToCoverDistance(dis))

