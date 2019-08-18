"""

Maximum length subsequence with difference between adjacent elements as either 0 or 1
Given an array of n integers. The problem is to find maximum length of the subsequence with difference between adjacent elements as either 0 or 1.

Examples:

Input : arr[] = {2, 5, 6, 3, 7, 6, 5, 8}
Output : 5
The subsequence is {5, 6, 7, 6, 5}.

Input : arr[] = {-2, -1, 5, -1, 4, 0, 3}
Output : 4
The subsequence is {-2, -1, -1, 0}.
Source: Expedia Interview Experience | Set 12

Time: 15:42 Hours
EXIT Time: 15:55 Hours

LINK: https://www.geeksforgeeks.org/maximum-length-subsequence-difference-adjacent-elements-either-0-1/

"""

#A Utility function that returns the Maximum length subsequence with difference between adjacent
#elements as either 0 or 1 in terms of interger|Number
#parameter: Input Array
#Returns: maximumLength of subsequence satisfying constraint
#Constraint: difference between adjacent elements is either 0 or 1 in
def findMaximumLengthSubsequenceWithDifferenceBetweenAdjacentElementsAs1Or0(array):
    length = len(array)
    dp = [0]*length
    maximumLengthSubsequence = 0

    #populating the dp list
    for i in range(1, length):
        localMax = 0
        for j in range(0, i):
            if( abs(array[i]-array[j]) ==  1  or array[i]==array[j]):
                localMax = max(localMax, dp[j]+1)
        dp[i] = localMax
        """for x in dp:
            print(x, end=" ")
        print()""" #Debug info
        maximumLengthSubsequence = max(maximumLengthSubsequence, dp[i])

    return(maximumLengthSubsequence+1)
    

array = [-2, -1, 5, -1, 4, 0, 3]
print( findMaximumLengthSubsequenceWithDifferenceBetweenAdjacentElementsAs1Or0(array) )
