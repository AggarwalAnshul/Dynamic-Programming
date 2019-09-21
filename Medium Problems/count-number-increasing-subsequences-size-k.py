"""
#M.49
Count number of increasing subsequences of size k
Given an array arr[] containing n integers. The problem is to count number of increasing subsequences in the array of size k.

Examples:

Input : arr[] = {2, 6, 4, 5, 7}, 
            k = 3
Output : 5
The subsequences of size '3' are:
{2, 6, 7}, {2, 4, 5}, {2, 4, 7},
{2, 5, 7} and {4, 5, 7}.

Input : arr[] = {12, 8, 11, 13, 10, 15, 14, 16, 20}, 
            k = 4
Output : 39

[+]Temporal marker            : 11:00, | Saturday Sept21, 19
[+]Temporal marker untethered : 11:24  | Saturday Sept21, 19
[+]Comments                   : *Easy peasy lemon squeezy!
                                *Had a clear approach in my worked that worked flawlessly
                                *saw a much more elegant solution from GFG
                                *Based on the same approach
                                *Was able to implement on my own.
                                *Problem is now closed
[+]Level                      : Basic
[+]Tread speead               : Relaxed / Paced
[+]LINK                       : https://www.geeksforgeeks.org/count-number-increasing-subsequences-size-k/
"""

def findSolution(lis, lim):
    length = len(lis)
    dp = [[0]*(length) for x in range(lim)]
    dp[0] = [1]*(length)
    for i in range(1, lim):
        for j in range(length):
            for k in range(j):
                if(lis[k]<lis[j]):
                   dp[i][j] += dp[i-1][k]
        dp[i][j] += dp[i][j-1]
    print(dp[lim-1])
    return dp[lim-1][length-1]
             
if __name__ == "__main__":
    lis = [[2, 6, 4, 5, 7],3]
    lis = [[12, 8, 11, 13, 10, 15, 14, 16, 20], 4]
    
    print(findSolution(lis[0], lis[1]))
    
