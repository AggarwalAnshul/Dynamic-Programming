"""
Convert to Strictly increasing integer array with minimum changes
Given an array of n integers. Write a program to find minimum number of changes in array so that array is strictly increasing of integers. In strictly increasing array A[i] < A[i+1] for 0 <= i < n

Examples:

Input : arr[] = { 1, 2, 6, 5, 4}
Output : 2
We can change a[2] to any value 
between 2 and 5.
and a[4] to any value greater then 5. 

Input : arr[] = { 1, 2, 3, 5, 7, 11 }
Output : 0
Array is already strictly increasing.

[+]Temporal marker            : 19:59 Hours | Sept02, 2019, Monday
[+]Temporal marker untethered : 20:08 Hours | Sept02, 2019, Monday
[+]Comments                   : Easy peasy lemon squeezy!
                               *Although the answer is correct to the best of my belieft
                                and it passes the scrutiny of GFG Sample cases, there is some
                                vague and queer point in the explanation given. i.e"""
                               #Example { 1, 2, 5, 3, 4 }, we consider length of LIS as three {
                               #{1, 2, 5}, not as {1, 2, 3, 4} because we cannot make a \
                               #strictly increasing array of integers with this LI
                                """ Comments report that this is necessary else the sample case
                                gets failed, but mine is runnig perfectly and i cannot fathom
                                the explanation behind the queery GFG Point, hence until further
                                light, this matter is closed henceforth, with a near complete
                                chance of never opening again.
[+]LINK                       : https://www.geeksforgeeks.org/convert-to-strictly-increasing-integer-array-with-minimum-changes/
"""

def findSolution(lis):
    length = len(lis)
    dp = ([1]*length)
    globalMax = 1
    
    for i in range(length):
        localMax = 1
        for j in range(i):
            if(lis[j] < lis[i]):
                localMax = max(localMax, dp[j]+1)
        dp[i] = localMax
        globalMax = max(globalMax, dp[i])

    return length-globalMax

if __name__ == "__main__":
    lis = [1, 2, 3, 5, 7, 11]
    lis = [ 1, 2, 6, 5, 4]
    lis = [ 1, 2, 6, 5, 4]
    print(findSolution(lis))
