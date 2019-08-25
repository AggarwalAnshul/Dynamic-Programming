"""
Minimum removals from array to make max – min <= K
Given N integers and K, find the minimum number of elements that should be removed such that Amax-Amin<=K. After removal of elements, Amax and Amin is considered among the remaining elements.
Examples:

Input : a[] = {1, 3, 4, 9, 10, 11, 12, 17, 20} 
          k = 4 
Output : 5 
Explanation: Remove 1, 3, 4 from beginning 
and 17, 20 from the end.

Input : a[] = {1, 5, 6, 2, 8}  K=2
Output : 3
Explanation: There are multiple ways to 
remove elements in this case.
One among them is to remove 5, 6, 8.
The other is to remove 1, 2, 5

[+]Temporal marker            : Record time, not tethered initially
[+]Temporal marker untethered : N/A
[+]Tread speed                : Relaxed
LINK: https://www.geeksforgeeks.org/minimum-removals-array-make-max-min-k/
"""

def findMinimumRemovalsArrayMakeMaxMinK(lis, k):
    length = len(lis)
    dp = [length-1]*length

    minRemovals = length
    for x in range(1, length):
        localMin = length
        for y in range(0, x):
            if(lis[x]-lis[y]<=k):
                localMin = min(localMin, dp[y])
        dp[x] = localMin-1
        minRemovals = min(dp[x], minRemovals)
    print(dp)
    return minRemovals
    
    
#lis =1, 3, 4, 9, 10, 11, 12, 17, 20
lis = 1, 5, 6, 2, 8
k = 3
print(findMinimumRemovalsArrayMakeMaxMinK(lis, k))
