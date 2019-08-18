"""
Longest subsequence such that difference between adjacents is one
Given an array of n size, the task is to find the longest subsequence such that difference between adjacents is one.

Examples:

Input :  arr[] = {10, 9, 4, 5, 4, 8, 6}
Output :  3
As longest subsequences with difference 1 are, "10, 9, 8", 
"4, 5, 4" and "4, 5, 6"

Input :  arr[] = {1, 2, 3, 2, 3, 7, 2, 1}
Output :  7
As longest consecutive sequence is "1, 2, 3, 2, 3, 2, 1"
Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution.
This problem is based upon the concept of Longest Increasing Subsequence Problem.

Let arr[0..n-1] be the input array and 
dp[i] be the length of the longest subsequence (with
differences one) ending at index i such that arr[i] 
is the last element of the subsequence.

Then, dp[i] can be recursively written as:
dp[i] = 1 + max(dp[j]) where 0 < j < i and 
       [arr[j] = arr[i] -1  or arr[j] = arr[i] + 1]
dp[i] = 1, if no such j exists.

To find the result for a given array, we need 
to return max(dp[i]) where 0 < i < n.

LINK: https://www.geeksforgeeks.org/longest-subsequence-such-that-difference-between-adjacents-is-one/

"""

def findLongestSubsequenceSuchThatDifferenceBetweenAdjacentsIsOne(array):
    length = len(array)
    dp = [0]*length
    longestSubsequence = 0

    #populating the dp array
    for i in range(1, length):
        localMax = 0
        for j in range(0, i):
            if( abs(array[i] - array[j]) == 1 ):
                localMax = max(localMax, dp[j]+1)
        dp[i] = localMax
        longestSubsequence = max(longestSubsequence, dp[i])

    #returning the answer
    return (longestSubsequence+1) #1 is added to consider the last element having this length in dp

#array = [1, 2, 3, 2, 3, 7, 2, 1]
array = [10, 9, 4, 5, 4, 8, 6]
print( findLongestSubsequenceSuchThatDifferenceBetweenAdjacentsIsOne(array) )

