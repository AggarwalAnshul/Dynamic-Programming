"""
Minimum number of jumps to reach end
Given an array of integers where each element represents the max number of steps that can be made forward from that element. Write a function to return the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then cannot move through that element.

Example:

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 8 ->9)
First element is 1, so can only go to 3. Second element is 3, so can make at most 3 steps eg to 5 or 8 or 9.

Temporal marker: 12:42 Hours | Aug24, Saturday
Temporal Marker: 12:48 Hours | Aug24, Saturday
Tread speed    : Relaxed
LINK           : https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/
"""
import sys

def findMinimumNumberOfJumpsToReachEndOfAGivenArray(lis):
    length = len(lis)
    dp = [0]*length
    dp[length-1] = lis[length-1]

    for x in range(length-2, -1, -1):
        maxJumpsFromHere = lis[x]
        elementsTillEnd = length-x-1
        if(maxJumpsFromHere > elementsTillEnd):
            dp[x] = 1
        else:
            localMin = sys.maxsize
            for y in range(x+1, x+maxJumpsFromHere+1):
                localMin = min(dp[y], localMin)
            dp[x] = localMin+1
    return dp[0]

#lis = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
lis = [1, 3, 6, 3, 2,3, 6, 8, 9, 5]
print(findMinimumNumberOfJumpsToReachEndOfAGivenArray(lis))
