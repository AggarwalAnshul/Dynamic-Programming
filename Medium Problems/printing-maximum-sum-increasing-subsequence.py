"""
#M.47

Printing Maximum Sum Increasing Subsequence
The Maximum Sum Increasing Subsequence problem is to find the maximum sum
subsequence of a given sequence such that all elements of the subsequence are
sorted in increasing order.

Examples:

Input:  [1, 101, 2, 3, 100, 4, 5]
Output: [1, 2, 3, 100]

Input:  [3, 4, 5, 10]
Output: [3, 4, 5, 10]

Input:  [10, 5, 4, 3]
Output: [10]

Input:  [3, 2, 6, 4, 5, 1]
Output: [3, 4, 5]

[+]Temporal marker            : 11:24, | Friday Sept20, 19
[+]Temporal marker untethered : 11:36  | Friday Sept20, 19
[+]Comments                   : *Easy peasy lemon squeezy!
[+]Level                      : Basic
[+]Tread speead               : Relaxed / Paced
[+]LINK                       : https://www.geeksforgeeks.org/printing-maximum-sum-increasing-subsequence/
"""
def printLIS(dp, index, lis):
    ans = []
    while(index>=0):
        ans.insert(0, lis[index])
        index = dp[index][1]
    return ans
        
def findSolution(lis):
    length = len(lis)
    localMax = [0,-1]
    ans = 0
    dp = [[0,-1] for x in range(length)]
    dp[0] = [lis[0], -1]
    for i in range(1, length):
        localMax[0] = 0
        localMax[1] = -1
        for j in range(i):
            if(lis[j]<lis[i]):
                if(dp[j][0]>localMax[0]):
                    localMax[0] = dp[j][0]
                    localMax[1] = j
        dp[i][0] = localMax[0]+lis[i]
        dp[i][1] = localMax[1]
        if(dp[ans][0] < dp[i][0]):
            ans = i
        #print(dp)
        #print(ans)
    return(printLIS(dp, ans, lis))
if __name__ == "__main__":
    lis = [10, 5, 4, 3]
    lis = [3, 4, 5, 10]
    lis = [3, 2, 6, 4, 5, 1]
    lis = [1, 101, 2, 3, 100, 4, 5]

    print(findSolution(lis))
    
