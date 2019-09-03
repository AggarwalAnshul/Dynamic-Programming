"""
#103
Probability of reaching a point with 2 or 3 steps at a time
A person starts walking from position X = 0, find the probability to reach exactly on X = N if she can only take either 2 steps or 3 steps. Probability for step length 2 is given i.e. P, probability for step length 3 is 1 – P.

Examples :

Input : N = 5, P = 0.20
Output : 0.32
Explanation :-
There are two ways to reach 5.
2+3 with probability = 0.2 * 0.8 = 0.16
3+2 with probability = 0.8 * 0.2 = 0.16
So, total probability = 0.32.
There is only one obstacle in the middle.
[+]Temporal marker            : 17:58 Hours | Sept03, 2019, Tuesday
[+]Temporal marker untethered : 18:05 Hours |Sept03, 2019, Tuesday
[+]Comments                   : Recognized it as a coin change varation with rep
                                at the first glance, just implemented the soln
                                and performed necessary modifications
[+]Level                      : Easy                               
[+]LINK                       : https://www.geeksforgeeks.org/probability-reaching-point-2-3-steps-time/
"""
def findSolution(distance, P):
    dp = [[0]*2 for x in range(distance+1)]
    dp[0] = [1,1]
    
    for x in range(1, distance+1):
        if(x>=2):
            dp[x][0]+=dp[x-2][0]
            dp[x][1]+=dp[x-2][1]*P
        if(x>=3):
            dp[x][0]+=dp[x-3][0]
            dp[x][1] += dp[x-3][1]*(1-P)
    return round(dp[distance][1], 2)

if __name__ == "__main__":
    n = 5
    P = 0.20
    print(findSolution(n, P))
