#M.58

"""
Given a sequence of n integers, you have to find out the non-decreasing subsequence of length k with minimum sum. If no sequence exists output -1.

Examples :

Input : [58 12 11 12 82 30 20 77 16 86],
        k = 3
Output : 39
{11 + 12 + 16}

Input : [58 12 11 12 82 30 20 77 16 86],
        k = 4
Output : 120
{11 + 12 + 20 + 77}

Input : [58 12 11 12 82 30 20 77 16 86],
        k = 5
Output : 206
 
[+]Temporal marker            :  Sun, 18:54 | Sep 22, 19
[+]Temporal marker untethered :  Sun, 21:10 | Sep 22, 19
[+]Comments                   : *Took about an hour
                                *Temporal marker distorted due to PCC
                                *Problem nwo closed 
[+]Level                      : 
[+]Tread speead               : 
[+]LINK                       : https://www.geeksforgeeks.org/non-decreasing-subsequence-of-size-k-with-minimum-sum
"""


import sys
def findSolution(lis, lim):
    length = len(lis)
    dp = [[sys.maxsize]*(length+1) for x in range(lim+1)]
    dp[1] = lis+[sys.maxsize]

    for i in range(2, lim+1):
        for j in range(length-i, -1, -1):
            localMax = sys.maxsize
            for k in range(j+1, length-i+2):
                if(k<=length-1 and lis[j]<lis[k]):
                    localMax = min(localMax, dp[i-1][k])
            if(localMax < sys.maxsize):
                dp[i][j] = lis[j] + localMax
            else:
                dp[i][j] = sys.maxsize

    ans = min(dp[lim])
    if(ans==sys.maxsize):
        return -1
    return ans

if __name__ == "__main__":
    lis = [[58, 12, 11, 12, 82, 30, 20, 77, 16, 86], 4]
    lis = [[58,12,11, 12,82, 30, 20, 77, 16, 86], 3]
    lis = [[58 ,12 ,11 ,12 ,82 ,30 ,20 ,77 ,16 ,86],5]
    print(findSolution(lis[0], lis[1]))