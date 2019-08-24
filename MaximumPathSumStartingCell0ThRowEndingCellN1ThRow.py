"""

Maximum path sum that starting with any cell of 0-th row and ending with any cell of (N-1)-th row
Given a N X N matrix Mat[N][N] of positive integers. There are only three possible moves from a cell (i, j)

(i+1, j)
(i+1, j-1)
(i+1, j+1)
Starting from any column in row 0, return the largest sum of any of the paths up to row N-1.

Examples:

Input : mat[4][4] = { {4, 2, 3, 4},
                      {2, 9, 1, 10},
                      {15, 158, 3, 0},
                      {16, 92, 41, 44} };
Output :120
path : 4 + 9 + 15 + 92 = 120 
Asked in: Amazon interview 

LINK: https://www.geeksforgeeks.org/maximum-path-sum-starting-cell-0-th-row-ending-cell-n-1-th-row/
"""

import sys
import PrintMatrix
def findMaximumPathSumStartingCell0ThRowEndingCellN1ThRow(dp, matrix, i, j):

    if(i==len(matrix)-1):
        dp[i][j] = matrix[i][j]
    elif(j==len(matrix)):
        return 0
    elif(dp[i][j] == (-100)):
            dp[i][j] = matrix[i][j]+max(findMaximumPathSumStartingCell0ThRowEndingCellN1ThRow(dp, matrix, i+1, j-1),
                        findMaximumPathSumStartingCell0ThRowEndingCellN1ThRow(dp, matrix, i+1, j),
                        findMaximumPathSumStartingCell0ThRowEndingCellN1ThRow(dp, matrix, i+1, j+1))
    return dp[i][j]


matrix = [[4, 2, 3, 4],
                      [2, 9, 1, 10],
                      [15, 158, 3, 44],
                      [16, 92, 410, 44]]

rows = len(matrix)
cols = len(matrix[0])
dp = [[(-100)]*cols for x in range(rows)]

maxValue = 0
for x in range(0, len(matrix[0])):
    maxValue = max(maxValue,  findMaximumPathSumStartingCell0ThRowEndingCellN1ThRow(dp, matrix, 0, x))
print(maxValue)
#PrintMatrix.printMatrix(dp)
