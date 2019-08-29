#86
"""Counts paths from a point to reach Origin
You are standing on a point (n, m) and you want to go to origin (0, 0) by
taking steps either left or down i.e. from each point you are allowed to move
either in (n-1, m) or (n, m-1). Find the number of paths from point to origin.

Examples:

Input : 3 6
Output : Number of Paths 84

Input : 3 0
Output : Number of Paths 1

[+]Temporal marker            : 11:08Hours             | Aug29, 2019
[+]Temporal marker untethered : 11:13(R)* >< 11:24(DP)*| Aug29, 2019
[+]Tread speed                : Relaxed 
[+]Comments                   : Easy, knew the approach, just implemented soln 
[+]LINK : https://www.geeksforgeeks.org/counts-paths-point-reach-origin/
"""

#S-Complexity: O(n) | T-Complexity: O(n)
def findSolutionDP(i, j):
    dp = [[0]*(j+1) for x in range(i+1)]
    for x in range(j+1):
        dp[0][x] = 1
    for x in range(i+1):
        dp[x][0] = 1
    for i in range(1,i+1):
        for j in range(1,j+1):
            up = dp[i][j-1]
            left = dp[i-1][j]
            dp[i][j] = left + up
    return dp[i][j]
#T-Complexity: Polynomial | S-Complexity:Polynomial
def findSolution(i, j, count):
    if(i==0 and j==0):
        return 1
    if(i<0 or j<0):
        return 0
    return findSolution(i-1,j,count)+findSolution(i, j-1, count)


n = 3
m = 6
n = 0
m = 2
print(findSolution(n, m, 0))
print(findSolutionDP(n, m))
    



