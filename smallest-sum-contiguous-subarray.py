"""
Smallest sum contiguous subarray
Given an array containing n integers. The problem is to find the sum of the elements of the contiguous subarray having the smallest(minimum) sum.

Examples:

Input : arr[] = {3, -4, 2, -3, -1, 7, -5}
Output : -6
Subarray is {-4, 2, -3, -1} = -6

Input : arr = {2, 6, 8, 1, 4}
Output : 1

[+]Temporal marker            : 11:16:47 Hours | Sept02, 2019
[+]Temporal marker untethered : 11:21:45 Hours | Sept02, 2019
[+]Comments                   : *Slight variation of maxSumContiguousSubarray Problem
                                *Knew kadane's algorithm, just implemented
                                *cameup with algo identical to kadane's on my own anyways,
                                 a long time ago, so it doesn't matter
[+]LINK                       : https://www.geeksforgeeks.org/smallest-sum-contiguous-subarray/
"""

#S-Complexity: O(1) | T-Complexity: O(n)
def findMaxSum(lis):
    minSumTillHere = lis[0]
    sumTillHere = lis[0]
    for element in lis:
        sumTillHere = min(sumTillHere+element, element)
        minSumTillHere = min(minSumTillHere, sumTillHere)
    return minSumTillHere

lis = [2, 6, 8, 1, 4]
lis = [-4, 2, -3, -1]
lis = [3, -4, 2, -3, -1, 7, -5]

print(findMaxSum(lis))
