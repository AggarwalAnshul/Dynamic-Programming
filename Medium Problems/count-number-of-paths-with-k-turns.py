#M.69

"""
Count number of paths with at-most k turns
Given a “m x n” matrix, count number of paths to reach bottom right from top left
 with maximum k turns allowed.

What is a turn? A movement is considered turn, if we were moving along row and now move
 along column. OR we were moving along column and now move along row.

There are two possible scenarios when a turn can occur
at point (i, j):

Turns Right: (i, j)  ->  (i+1, j)  ->  (i+1, j+1)
                      Down        Right

Turns Down:  (i, j)  ->  (i, j+1)  ->  (i+1, j+1)
                     Right        Down
Examples:

Input:  m = 3, n = 3, k = 2
Output: 4
See below diagram for four paths with
maximum 2 turns.

Input:  m = 3, n = 3, k = 1
Output: 2
pathswithkturns


[+]Temporal marker            :  Tue, 18:20 | Sep 24, 19
[+]Temporal marker untethered :  Tue, 18:33(R*) 20:21(DP*) | Sep 24, 19
[+]Comments                   : *Recursive solution devised in acceptable timeFrame
                                *Took some to develop the DP Solution
                                *Took more than an hour before the idea could be incepted
                                *GFG has used memory storage in Recursive solution to make it DP
[+]Level                      : Medium
[+]Tread speed                : Relaxed
[+]LINK                       : https://www.geeksforgeeks.org/count-number-of-paths-with-k-turns
"""

#PURE DP Approach
#Space Complexity: O(m*n*count) | T-Complexity: O(m*n*count)
def findSolutionDP(m, n, count):
    dp = [[[[], []] for x in range(n+1)] for y in range(m+1)]
    dp[1][1][0]  = [0]
    dp[1][1][1] = [0]
    for i in range(1, m+1):
        for j in range(1, n+1):
            #left passage
            if(len(dp[i][j-1][0]) > 0):
                dp[i][j][0] += dp[i][j-1][0]
            #top passage
            if(len(dp[i-1][j][1]) > 0):
                dp[i][j][1] += dp[i-1][j][1]
            #turning passage
                #left passage
            for x in dp[i-1][j-1][1]:
                dp[i][j][0].append(x+1)
                #top passage
            for x in dp[i-1][j-1][0]:
                dp[i][j][1].append(x+1)

    ans = 0
    for x in dp[m][n][0]:
        if(x<=count):
            ans+=1
    for x in dp[m][n][1]:
        if(x<=count):
            ans+=1
    return ans


#RECURSIVE SOLUTION
#S-Complexity: O(M*N) | T-Complexity: Exponetitial
def findSolutionRecursive(i, j, direction, count, m, n):
    if(i>=m or j>=m or i<0 or j<0):
        return 0
    if(i==m-1 and j==n-1):
        return 1
    turn = 0
    straight = 0
    if(count>0):
        if(direction=="right"):
            turn = findSolutionRecursive(i+1, j+1, "down", count-1, m, n)
        else:
            turn = findSolutionRecursive(i+1, j+1, "right", count-1, m, n)
    if(direction=="right"):
        straight = findSolutionRecursive(i, j+1, "right", count, m, n)
    else:
        straight = findSolutionRecursive(i+1, j, "down", count, m, n)
    return turn+straight


if __name__ == "__main__":
    lis = [3, 3, 1]
    lis = [3, 3, 2]
    lis = [8, 4, 1]
    print(findSolutionDP(lis[0], lis[1], lis[2]))
    print("computing using recursive solution....")
    print(findSolutionRecursive(0, 0, "right", lis[2], lis[0], lis[1])+
          findSolutionRecursive(0, 0, "down", lis[2], lis[0], lis[1]))
