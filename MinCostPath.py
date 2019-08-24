"""
Min Cost Path | DP-6
Given a cost matrix cost[][] and a position (m, n) in cost[][], write a
function that returns cost of minimum cost path to reach (m, n) from (0, 0).
Each cell of the matrix represents a cost to traverse through that cell.
Total cost of a path to reach (m, n) is sum of all the costs on that path
(including both source and destination). You can only traverse down,
right and diagonally lower cells from a given cell, i.e.,
from a given cell (i, j), cells (i+1, j), (i, j+1) and (i+1, j+1)
can be traversed. You may assume that all costs are positive integers.

For example, in the following figure, what is the minimum cost path to (2, 2)?


The path with minimum cost is highlighted in the following figure. The path is
(0, 0) –> (0, 1) –> (1, 2) –> (2, 2). The cost of the path is 8 (1 + 2 + 2 + 3).

Temporal Marker:
Temporal Marker Untethered: Lost Track, acceptable time frame, coded to the solution without much
                            fluke
Tread Speed               : Relaxed
LINK:
"""
import sys
import PrintMatrix

def findMinCostPath(matrix, m, n):
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0]*cols for x in range(rows)]

    #init
    dp[0][0] = matrix[0][0]
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + matrix[0][j]
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
    #PrintMatrix.printMatrix(dp)

    for i in range(1, m+1, 1):
        for j in range(1, n+1, 1):
            dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        #PrintMatrix.printMatrix(dp)

    return dp[m][n]

def findMinCostPathRecursiveDP(matrix, dp, m, n, i, j):
    if(i>m or j>n):
        return sys.maxsize
    if(i==m and j==n):
        return matrix[i][j]
    if(dp[i][j]== None):
        dp[i][j] = matrix[i][j]  + min(findMinCostPathRecursiveDP(matrix, dp, m, n, i+1, j),
                                       findMinCostPathRecursiveDP(matrix, dp, m, n, i, j+1),
                                       findMinCostPathRecursiveDP(matrix, dp, m, n, i+1, j+1))
    return dp[i][j]

matrix = [[1,2,3], [4,8,2], [1,5,3]]
m = 2
n= 1
rows = len(matrix)
cols = len(matrix[0])
dp = [[None]*cols for x in range(rows)]
print(findMinCostPath(matrix, m, n))
print("Min cost path to destinatoin is: " + str( findMinCostPathRecursiveDP(matrix, dp, m, n, 0, 0)) )
#PrintMatrix.printMatrix(dp)
