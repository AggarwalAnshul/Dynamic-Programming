"""
#M.38
Longest alternating subsequence
A sequence {x1, x2, .. xn} is alternating sequence if its elements satisfy one of the following relations :
  x1 < x2 > x3 < x4 > x5 < …. xn or 
  x1 > x2 < x3 > x4 < x5 > …. xn 
Examples :
Input: arr[] = {1, 5, 4}
Output: 3
The whole arrays is of the form  x1 < x2 > x3 
Input: arr[] = {1, 4, 5}
Output: 2
All subsequences of length 2 are either of the form 
x1 < x2; or x1 > x2
Input: arr[] = {10, 22, 9, 33, 49, 50, 31, 60}
Output: 6
The subsequences {10, 22, 9, 33, 31, 60} or
{10, 22, 9, 49, 31, 60} or {10, 22, 9, 50, 31, 60}
are longest subsequence of length 6.
[+]Temporal marker            : N/A, | Saturday Sept14, 19
[+]Temporal marker untethered : 30/40 Mins  | Saturday Sept14, 19
[+]Comments                   : *Took a couple of hour
                                *Developed the DP(not so optimized) Algo on my own
                                *Algo looks good
                                *More optimized elegant DP Solution from GFG
                                *Uses the approach  that i discarded/not pursued enough
                                during brainstorming
                                *DPO Solution is vaguely understandable
                                *Problem is now closed
[+]Level                      : Medium
[+]Tread speead               : Relaxed / Paced
[+]LINK                       : https://www.geeksforgeeks.org/longest-alternating-subsequence/
"""
#S-Complexity: O(N) | T-Complexity: O(N*N)
def findSolutionDPO(lis):
    length = len(lis)
    dp = [[1]*length for x in range(2)]
    ans = 0
    for x in range(1, length):
        for y in range(x):
            if(lis[y]>lis[x]):
                dp[0][x] = max(dp[0][x], dp[1][y]+1)
            if(lis[y]<lis[x]):
                dp[1][x] = max(dp[1][x], dp[0][y]+1)
        ans = max(ans, dp[1][x], dp[0][x])
    return ans
    #import PrintMatrix as pm
    #pm.printss(dp, lis, [0,1])

#S-Complexity: O(N) | T-Complexity: O(N*N)
def findSolution(lis):
    length = len(lis)
    dp = [[1]*(length) for x in range(5)]
    dp[0][0] = 1 #polarity required in the next
    dp[1][0] = 1 #Count till now
    dp[3][0] = -1
    dp[4][0] = 1
    for x in range(1, length):
        ele = lis[x]
        localMax = 0
        localPol = 0
        for y in range(x):
            if(ele>lis[y] and dp[0][y]==1):
                if(localMax < dp[1][y]):
                    localMax = dp[1][y]
                    localPol = dp[0][y]
            elif(ele<lis[y] and dp[0][y]==-1):
                if(localMax < dp[1][y]):
                    localMax = dp[1][y]
                    localPol = dp[0][y]
        dp[0][x] = localPol*(-1)
        dp[1][x] = localMax+1
    for x in range(1, length):
        ele = lis[x]
        localMax = 0
        localPol = 0
        for y in range(x):
            if(ele<lis[y] and dp[3][y]==-1):
                if(localMax < dp[4][y]):
                    localMax = dp[4][y]
                    localPol = dp[3][y]
            elif(ele>lis[y] and dp[3][y]==1):
                if(localMax < dp[4][y]):
                    localMax = dp[4][y]
                    localPol = dp[3][y]
        dp[3][y] = localPol
        dp[4][y] = localMax+1
    import PrintMatrix as pm
    liss = [0]*5
    #pm.printss(dp, lis, [1,2,3,4,5])
    return max(max(dp[1]), max(dp[4]))
if __name__ == "__main__":
    lis = [1, 5, 4]
    lis = [10, 22, 9, 33, 49, 50, 31, 60]
    lis = [1, 4, 5]
    print(findSolutionDPO(lis))
    print(findSolution(lis)) 
