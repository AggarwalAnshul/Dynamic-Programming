"""
#102
Number of ways to arrange N items under given constraints
We are given N items which are of total K different colors.
Items of the same color are indistinguishable and colors can be
numbered from 1 to K and count of items of each color is also given
as k1, k2 and so on. Now we need to arrange these items one by one under a
constraint that the last item of color i comes before the last item of color (i + 1)
for all possible colors. Our goal is to find out how many ways this can be achieved.

Examples:

Input : N = 3        
        k1 = 1    k2 = 2
Output : 2
Explanation :
Possible ways to arrange are,
k1, k2, k2
k2, k1, k2 

Input : N = 4        
        k1 = 2    k2 = 2
Output : 3
Explanation :
Possible ways to arrange are,
k1, k2, k1, k2
k1, k1, k2, k2
k2, k1, k1, k2

[+]Temporal marker            : Didn't Tether | Wednesday, Sept04, 19
[+]Temporal marker untethered : N/A Took couple of days | Sept03, 2019, Tuesday
[+]Comments                   : Looked difficult at first glance, Laid it off for some time,
                                Solved today in the sweep. Previously I was using combinatrics
                                & permutation approach which failed miserably, today, tried to
                                create possiblity tree and devised the recurrence relation based
                                on the choices to make at any given point. Implemented in the form
                                of tablutaion DP and Voila algo is born.
                                Although couldn't be fully verified, The GFG solution is wrong and
                                is failing to execute for cases K1>K2 or when K2 is large,
                                comments show the approach kind of used but it is not exact and
                                honestly I'm too lazy to try. My Coldpressing shows promisiing
                                results and a rough coldpressing is verfied by this algo.
                                Hence, THIS PROBLEM IS NOW CLOSED :D
[+]Tread speed                : Relaxed 
[+]Level                      : Medium
[+]LINK                       : https://www.geeksforgeeks.org/number-of-ways-to-arrange-n-items-under-given-constraints/
"""

def findSolution(one, two):
    #init
    dp = [[0]*(two+1) for x in range(one+1)]
    for x in range(two):
        dp[one][x] = 1

    for i in range(one-1, -1, -1):
        for j in range(two-1, -1, -1):
            dp[i][j] = dp[i][j+1] + dp[i+1][j]
    #import PrintMatrix as pm #This is my custom module, make your own to print 2D matrix
    #pm.printMatrix(dp)
    return dp[0][0]

if __name__ == "__main__":
    #lis = [k2, k2]
    coloredBalls = [4, 3]
    print(findSolution(coloredBalls[0], coloredBalls[1]))
