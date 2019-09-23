#M.59
"""
>>>>>>>>>>>>>>>>>>>>>> SHIFTED TO PYCHARM FROM IDE <<<<<<<<<<<<<<<<<<<<<
Longest Common Subsequence with at most k changes allowed
Given two sequence P and Q of numbers. The task is to find Longest Common Subsequence
of two sequence if we are allowed to change at most k element in first sequence to any value.

Examples:

Input : P = { 8, 3 }
        Q = { 1, 3 }
        K = 1
Output : 2
If we change first element of first
sequence from 8 to 1, both sequences
become same.

Input : P = { 1, 2, 3, 4, 5 }
        Q = { 5, 3, 1, 4, 2 }
        K = 1
Output : 3
By changing first element of first
sequence to 5 to get the LCS ( 5, 3, 4 }.

[+]Temporal marker            :  Mon, 9:47 | Sep 23, 19
[+]Temporal marker untethered :  Mon, 9:57 | Sep 23, 19
[+]Comments                   : * Had a clear approach in mind
                                * GFG has done some weird shit in O(N^3) complexity
                                * My Solution works in O(N^2) passes all the cases
                                * Conceptually looks good
                                * Closing the matter until further light on this matter
[+]Level                      : Easy
[+]Tread speead               : Paced
[+]LINK                       : https://www.geeksforgeeks.org/longest-common-subsequence-with-at-most-k-changes-allowed
"""
#S-Complexity: O(one*two) | T-Complexity: O(One*Two) | AuxSpace: NONE
def findSolution(one, two, k):
    lenOne = len(one)
    lenTwo = len(two)

    dp = [[0]*(lenTwo+1) for x in range(lenOne+1)]

    for i in range(1, lenOne+1):
        for j in range(1, lenTwo+1):
            if(one[i-1]==two[j-1]):
                dp[i][j] = dp[i-1][j-1]+1
            elif(k>0):
                dp[i][j] = dp[i-1][j-1]+1
                k-=1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    import PrintMatrix as pm
    pm.printss(dp, two, one)
    return dp[lenOne][lenTwo]

if __name__ == "__main__":
    #lis = [one, two, k]
    lis = [[8,3], [1, 3], 1]
    lis = [[1, 2, 3, 4, 5], [5, 3, 1, 4, 2], 1]
    lis = [[1, 2, 3, 4], [4, 5, 6, 7], 1]
    print(findSolution(lis[0], lis[1], lis[2]))