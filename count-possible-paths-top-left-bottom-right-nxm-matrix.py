"""
#91
Count all possible paths from top left to bottom right of a mXn matrix
The problem is to count all the possible paths from top left to bottom right
of a mXn matrix with the constraints that from each cell you can either move only
to right or down

Examples :

Input :  m = 2, n = 2;
Output : 2
There are two paths
(0, 0) -> (0, 1) -> (1, 1)
(0, 0) -> (1, 0) -> (1, 1)

Input :  m = 2, n = 3;
Output : 3
There are three paths
(0, 0) -> (0, 1) -> (0, 2) -> (1, 2)
(0, 0) -> (0, 1) -> (1, 1) -> (1, 2)
(0, 0) -> (1, 0) -> (1, 1) -> (1, 2)

[+]Temporal marker            : 10:35 Hours | Sept02, 2019
[+]Temporal marker untethered : 10:54 Hours | Sept02, 2019
[+]Comments                   : *Recursive solution produced in record time
                                *idk why but dp solution took quite a time
                                *later realized the solution was staring right at
                                 my face, recusive formula was to be used! DAMN!
[+]LINK                       : https://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/
"""

#S-Complexity: O(mn) | T-Complexity: O(mn)
def findTotalWaysDP(rows, cols):
    dp = [[1]*(cols+1) for x in range(rows+1)]
    for row in range(1, rows):
        for col in range(1, cols):
            dp[row][col] = dp[row][col-1] + dp[row-1][col]
    return dp[rows-1][cols-1]

#S-Complexity: Exponential | T-Complexity: Exponential
def findTotalWaysRecursive(m, n, i, j, count):
    if(i==m-1 and j==n-1):
        return count+1
    if(i<0 or j<0 or j>=n or i>=m):
        return 0
    down  = findTotalWaysRecursive(m, n, i+1, j, count)
    right = findTotalWaysRecursive(m, n, i, j+1, count)
    return down + right

if __name__ == "__main__":
    lis = [2, 2]
    lis = [3, 3]
    lis = [10, 18]
    print(findTotalWaysDP(lis[0], lis[1]))
    print("computing using recursive solution...")
    print(findTotalWaysRecursive(lis[0], lis[1], 0, 0, 0))
    


