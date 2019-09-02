"""
Largest Sum Contiguous Subarray
Write an efficient program to find the sum of contiguous subarray within a
one-dimensional array of numbers which has the largest sum.
kadane-algorithm


[+]Temporal marker            : 11:07:47 Hours | Sept02, 2019
[+]Temporal marker untethered : 11:11:15 Hours | Sept02, 2019
[+]Comments                   : *Knew kadane's algorithm, just implemented
                                *cameup with algo identical to kadane's on my own anyways,
                                 a long time ago, so it doesn't matter
[+]LINK                       : https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
"""

def findMaxSum(lis):
    maxSumTillHere = 0
    sumTillHere = 0
    for element in lis:
        sumTillHere += element
        if(sumTillHere > maxSumTillHere):
            maxSumTillHere = sumTillHere
        if(sumTillHere < 0):
            sumTillHere = 0
    return maxSumTillHere

lis = [-2, -3, 4, -1, -2, 1, 5, -3]
print(findMaxSum(lis))
