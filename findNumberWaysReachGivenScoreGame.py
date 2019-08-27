"""
Count number of ways to reach a given score in a game
Consider a game where a player can score 3 or 5 or 10 points
in a move. Given a total score n, find number of ways to reach the given score.

Examples:

Input: n = 20
Output: 4
There are following 4 ways to reach 20
(10, 10)
(5, 5, 10)
(5, 5, 5, 5)
(3, 3, 3, 3, 3, 5)

Input: n = 13
Output: 2
There are following 2 ways to reach 13
(3, 5, 5)
(3, 10)
[+]Temporal marker            : 19:08 Hours | Aug27, 2019
[+]Temporal marker untethered : 19:18 Hours | Aug27, 2019
[+]Tread speed                : Paced
[+]Comments                   : Easy peasy lemon squeezy! Disguised coin change problem
[+]LINK : https://www.geeksforgeeks.org/count-number-ways-reach-given-score-game/
"""
def findNumberWaysReachGivenScoreGameS(score):
    dp  = [0]*(score+1)
    dp[0] = 1

    for i in range(3, score+1):
        dp[i] = dp[i-3]
    for i in range(5, score+1):
        dp[i] += dp[i-5]
    for i in range(10, score+1):
        dp[i] += dp[i-10]
    return dp[score]

def findNumberWaysReachGivenScoreGame(score):
    lis = [3,5,10]
    dp = [[0]*4 for x in range(score+1)]
    maxWays = 0
    for x in range(4):
        dp[0][x] = 1

    for i in range(1, score+1):
        for j in range(1, 4):
            if(i<lis[j-1]):
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-lis[j-1]][j] + dp[i][j-1]
                #print(dp[i][j])
            maxWays = max(maxWays, dp[i][j])
            #import PrintMatrix as pm
            #pm.printMatrix(dp)
    return maxWays

score = 13
print(findNumberWaysReachGivenScoreGame(score))
print(findNumberWaysReachGivenScoreGameS(score))
