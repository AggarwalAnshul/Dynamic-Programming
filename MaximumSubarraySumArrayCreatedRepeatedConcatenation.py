"""
Maximum subarray sum in an array created after repeated concatenation
Given an array and a number k, find the largest sum of contiguous array in the modified array which is formed by repeating the given array k times.

Examples :

Input  : arr[] = {-1, 10, 20}, k = 2
Output : 59
After concatenating array twice, we 
get {-1, 10, 20, -1, 10, 20} which has 
maximum subarray sum as 59.

Input  : arr[] = {-1, -2, -3}, k = 3
Output : -1
Temporal marker:               11:13 Hours | Aug23, Friyay
Temporal Marker Untethered:    11:39 Hours | Aug23, Friyay
Tread Speed               :    Relaxed, Talked to dad admist!
LINK: https://www.geeksforgeeks.org/maximum-subarray-sum-array-created-repeated-concatenation/
"""

import sys
def findMaximumSubarraySumArrayCreatedRepeatedConcatenation(arr, k):
    length = len(arr)
    elements = length*k

    start = 0
    end = 0
    maxSumCount = -sys.maxsize-1
    currSumCount = 0

    for i in range(0, elements):
        index = i%length
        #print("on index: "+str(arr[index]))
        currSumCount += arr[index]
        if(maxSumCount < currSumCount):
            maxSumCount = currSumCount
            end = i

        if(currSumCount <=0):
            currSumCount = 0
            start = i
        #print("currSumCount: "+str(currSumCount))
    print("max sum is: "+str(maxSumCount))

arr = [-1, 10, 20]
#arr = [-1, -1, -1]
k = 2
findMaximumSubarraySumArrayCreatedRepeatedConcatenation(arr, k)
