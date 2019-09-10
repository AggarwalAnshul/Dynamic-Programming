"""
#M.27
Longest Bitonic Subsequence | DP-15
Given an array arr[0 … n-1] containing n positive integers, a subsequence of arr[] is called Bitonic if it is first increasing, then decreasing. Write a function that takes an array as argument and returns the length of the longest bitonic subsequence.
A sequence, sorted in increasing order is considered Bitonic with the decreasing part as empty. Similarly, decreasing order sequence is considered Bitonic with the increasing part as empty.

Examples:

Input arr[] = {1, 11, 2, 10, 4, 5, 2, 1};
Output: 6 (A Longest Bitonic Subsequence of length 6 is 1, 2, 10, 4, 2, 1)

Input arr[] = {12, 11, 40, 5, 3, 1}
Output: 5 (A Longest Bitonic Subsequence of length 5 is 12, 11, 5, 3, 1)

Input arr[] = {80, 60, 30, 40, 20, 10}
Output: 5 (A Longest Bitonic Subsequence of length 5 is 80, 60, 30, 20, 10)


[+]Temporal marker            : 15:33  Hours, | Tuesday Sept10, 19
[+]Temporal marker untethered : 15:40  Hours  | Tuesday Sept10, 19
[+]Comments                   : *Approach was clear what to do
                                *Just implemented
[+]Tread speed                : Paced
[+]Level                      : Easy
[+]LINK                       : https://www.geeksforg eeks.org/longest-bitonic-subsequence-dp-15/
"""

#S-Complexity: O(n) | T-Complexity: O(n)
def findSolution(lis):
    length = len(lis)
    dp = [[1]*(length) for x in range(2)]
    #increasing
    for x in range(1, length):
        localMax = 0
        for j in range(x):
            if(lis[j]<lis[x]):
                localMax = max(localMax, dp[0][j])
        dp[0][x] = localMax+1
    #Decreasing
    for x in range(length-2, -1, -1):
        for j in range(x+1, length, 1):
            if(lis[j]<lis[x]):
                localMax = max(localMax, dp[1][j])
        dp[1][x] = localMax+1
    localMax  = 0
    #Analyzing
    for x  in range(length):
        localMax = max(localMax, dp[0][x]+dp[1][x])
    import PrintMatrix as pm
    pm.printss(dp)
    return localMax-1


if __name__ == "__main__":
    lis = [12, 11, 40, 5, 3, 1]
    lis = [80, 60, 30, 40, 20, 10]
    lis = [1, 11, 2, 10, 4, 5, 2, 1]
    print(findSolution(lis))
