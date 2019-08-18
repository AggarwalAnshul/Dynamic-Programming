"""
Maximum sum increasing subsequence from a prefix and a given element after prefix is must
Given an array of n positive integers, write a program to find the maximum sum of increasing
subsequence from prefix till i-th index and also including a given kth element which is after i,
i.e., k > i .
Examples :

Input : arr[] = {1, 101, 2, 3, 100, 4, 5}
i-th index = 4 (Element at 4th index is 100)
K-th index = 6 (Element at 6th index is 5.)
Output : 11
So we need to calculate the maximum sum of subsequence (1 101 2 3 100 5) such that 5 is
necessarily included in the subsequence, so answer is 11 by subsequence (1 2 3 5).

Input : arr[] = {1, 101, 2, 3, 100, 4, 5}
i-th index = 2 (Element at 2nd index is 2)
K-th index = 5 (Element at 5th index is 4.)
Output : 7
So we need to calculate the maximum sum of subsequence (1 101 2 4) such that 4 is necessarily
included in the subsequence, so answer is 7 by subsequence (1 2 4).

LINK:https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-from-a-prefix-and-a-given-element-after-prefix-is-must/
Temporal marker: 16:00 Hours |  Aug18 Sunday
Temporal marker untethered: 16:17 Hours | Aug 18, Sunday

"""

#A Utility function that finds the maximum sum of increasing subsequence till i-th index
#and also including a given kth element which is after i, i.e., k > i .

#Paramtere: Array, iIndex(limiting Index), kIndex(The element that must be included)
#Returns: Maximum Length subsequence satisfying constraint in terms of integer|Numeral 
#Constraint: maximum sum of increasing subsequence from prefix till i-th index and also
#            including a given kth element which is after i
def findMaximumSumIncreasingSubsequenceUptoAnIndexIncludingKthIndexElement(array, iIndex, kIndex):
    length = len(array)
    dp = [0]*length
    for i in range(0, length):
        dp[i] = array[i]

    #Populating the dp array
    for i in range(1, iIndex+1):
        localMax = 0
        for j in range(0, i):
            if( array[j] < array[i] ):
                localMax = max(localMax, dp[j])
        dp[i] = max(localMax+dp[i], dp[i])
        for x in dp:
            print(x, end=" ")
        print()
    #Iterating to find the max length subseqence including k as a terminal element
    maximumSubsequenceLength = 0
    for i in range(0, iIndex+1):
        if(array[i]<array[kIndex]):
            maximumSubsequenceLength = max(maximumSubsequenceLength, dp[i])

    return (maximumSubsequenceLength + array[kIndex])


array = [1, 101, 2, 3, 100, 4, 5]
iIndex = 2
kIndex = 5
print( findMaximumSumIncreasingSubsequenceUptoAnIndexIncludingKthIndexElement(array, iIndex, kIndex) )
