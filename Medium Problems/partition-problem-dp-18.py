"""
#M.22

Partition problem | DP-18
Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is same.
Examples:

arr[] = {1, 5, 11, 5}
Output: true 
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false 
The array cannot be partitioned into equal sum sets.

[+]Temporal marker            : 16:00    Hours, | Monday Sept09, 19
[+]Temporal marker untethered : 15:04:05 Hours  | Monday Sept09, 19
[+]Comments                   : Knew the approach, just implemented 
[+]Tread speed                : Paced
[+]Level                      : Easy
[+]LINK                       : https://www.geeksforgeeks.org/partition-problem-dp-18/
"""

#S-Complexity: O(sum*lis size) | T-Complexity: O(sum*lis size)
def findSolution(lis):
    halfSum = 0
    for x in lis:
        halfSum += x
    if(halfSum%2!=0):
        return False
    halfSum = int(halfSum/2)
    length = len(lis)
    dp = [[0]*(length+1) for x in range(halfSum+1)]
    dp[0] = [1]*(length+1)

    for i in range(1, halfSum+1):
        for j in range(1, length+1):
            dp[i][j] = dp[i][j-1]
            if(i>=j):
                dp[i][j] += dp[i-j][j]
    import PrintMatrix as pm
    pm.printss(dp)
    if (dp[halfSum][length]>=1):
        return True

if __name__ == "__main__":
    lis = [1,5,3]
    lis = [1, 5, 11, 5]
    lis = [3, 1, 1, 2, 2, 1]
    print(findSolution(lis))
