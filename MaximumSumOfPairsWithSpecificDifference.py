"""
Maximum sum of pairs with specific difference
Given an array of integers and a number k. We can pair two number
of array if difference between them is strictly less than k. The task is
to find maximum possible sum of disjoint pairs. Sum of P pairs is sum of
all 2P numbers of pairs.

Examples:

Input  : arr[] = {3, 5, 10, 15, 17, 12, 9}, K = 4
Output : 62
Then disjoint pairs with difference less than K are,
(3, 5), (10, 12), (15, 17)    
So maximum sum which we can get is 3 + 5 + 12 + 10 + 15 + 17 = 62
Note that an alternate way to form disjoint pairs is,
(3, 5), (9, 12), (15, 17), but this pairing produces lesser sum.

Input  : arr[] = {5, 15, 10, 300}, k = 12
Output : 25

Temporal marker:  14:58 Hours | Aug20, Tuesday
Temporal Marker untethered: 15:10 Hours | Aug20, Tuesday
LINK: https://www.geeksforgeeks.org/maximum-sum-pairs-specific-difference/

T-Complexity: O(nLogn) | Sorting
S-Complexity: No Aux space used | only for sorting purpose
"""

def findMaximumSumOfPairsWithSpecificDifference(lis, k):
    lis.sort()
    length = len(lis)
    count = 0
    print(lis)
    x = length-1
    while(x>0):
        #print("x: "+str(x)+" : "+str(lis[x]))
        if(lis[x]-lis[x-1] < k):
            count+=lis[x]+lis[x-1]
            x-=2
        else:
            x-=1
        #print("count: "+str(count)+" x: "+str(x))
    print(count)

#lis = [3, 5, 10, 15, 17, 12, 9]
lis = [5, 15, 10, 300]
findMaximumSumOfPairsWithSpecificDifference(lis, 12)
        
