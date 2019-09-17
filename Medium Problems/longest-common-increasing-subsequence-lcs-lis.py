"""
#M.44

Longest Common Increasing Subsequence (LCS + LIS)
Prerequisites : LCS, LIS

Given two arrays, find length of the longest common increasing subsequence [LCIS] and print one of such sequences (multiple sequences may exist)

Suppose we consider two arrays –
arr1[] = {3, 4, 9, 1} and
arr2[] = {5, 3, 8, 9, 10, 2, 1}

Our answer would be {3, 9} as this is the longest common subsequence which is increasing also.


[+]Temporal marker            : 12:00, | Tuesday Sept17, 19
[+]Temporal marker untethered : 12:40(R*) 11:30(DP*)  | Tuesday Sept17, 19
[+]Comments                   : *Knew the appraoch
                                *Didn't Why took so much time
                                *Combination of LCS AND LIS
                                *was skeptical of the earlier approach
                                *Fairly confident of this new approach
                                *Matter is closed now
[+]Level                      : Easy
[+]Tread speead               : Relaxed / Paced
[+]LINK                       : https://www.geeksforgeeks.org/longest-common-increasing-subsequence-lcs-lis/
"""
import sys
def findSolutionDP(one, two):
    lenOne = len(one)
    lenTwo = len(two)
    dp = [[0]*(lenTwo+1) for x in range(lenOne+1)]
    table = [None]*(lenTwo)
    
    for j in range(1, lenTwo+1):
        for i in range(1, lenOne+1):
            if(two[j-1]==one[i-1]):
                table[j-1] = two[j-1]
                break
    return printLIS(table)
                

def printLIS(lis):
    #print("finding lis from : "+str(lis))
    length = len(lis)
    LIS = []
    dp = [[1,-1] for x in range(length)]
        
    ans = 0
    for i in range(1, length):
        if(lis[i]!=None):
            localMax = [0, i]
            for j in range(i):
                if (lis[j]!=None and lis[j]<lis[i]):
                    if(dp[j][0]>localMax[0]):
                        localMax[0] = dp[j][0]
                        localMax[1] = j
            dp[i][0] = localMax[0]+1
            dp[i][1] = localMax[1]
            if(dp[i][0]>dp[ans][0]):
                ans = i
    count = dp[ans][0]
    while(count>0):
        LIS.insert(0, lis[ans])
        ans = dp[ans][1]
        count-=1
    return LIS

def printLCS(dp, one, two):
    i = len(dp)-1
    j = len(dp[0])-1
    lcs = []
    while(i>0 and j>0):
        if(one[i-1]==two[j-1]):
            lcs.insert(0, one[i-1])
            #print(one[i-1], end="\t")
            i-=1
            j-=1
        elif dp[i-1][j]>dp[i][j-1]:
            i-=1
        else:
            j-=1
    print("LCS is: " + str(lcs))
    return lcs
def findSolution(one, two):
    lenOne = len(one)
    lenTwo = len(two)
    dp = [[0]*(lenTwo+1) for x in range(lenOne+1)]

    for i in range(1, lenOne+1):
        for j in range(1, lenTwo+1):
            if(one[i-1]==two[j-1]):
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    import PrintMatrix as pm
    pm.printss(dp, two, one)
    return( printLIS(printLCS(dp, one, two)) )

if __name__ == "__main__":
    lis = [[3, 4, 9, 1], [5, 3, 8, 9, 10, 2, 1]]
    print("LCIS is: "+str(findSolutionDP(lis[0], lis[1])) )
    print("finding through different approach...")
    print("LCIS: "+str(findSolution(lis[0], lis[1])))
