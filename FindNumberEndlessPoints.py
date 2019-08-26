"""
Find number of endless points
Given a binary N x N matrix, we need to find the total number of matrix positions from which there is an endless path. Any position (i, j) is said to have an endless path if and only if all of the next positions in its row(i) and its column(j) should have value 1. If any position next to (i,j) either in row(i) or in column(j) will have 0 then position (i,j) doesn’t have any endless path.

Examples:

Input :  0 1 0
         1 1 1
         0 1 1
Output : 4
Endless points are (1, 1), (1, 2),
(2, 1) and (2, 2). For all other
points path to some corner is 
blocked at some point.
dp1

Input :  0 1 1
         1 1 0
         0 1 0
Output : 1
Endless point is (0, 2).

LINK : https://www.geeksforgeeks.org/find-number-endless-points/
"""
import PrintMatrix as pm
def findNumberEndlessPoints(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0]*cols for x in range(rows)]
    endlessPoints = 0
    for i in range(rows-1,-1,-1):
        for j in range(cols-1,-1,-1):
            if(i==rows-1 or (dp[i+1][j]==1 and matrix[i+1][j]==1)) :
                if(j==cols-1 or (dp[i][j+1]==1 and matrix[i][j+1]==1)):
                    if(matrix[i][j]==1):
                        dp[i][j] = 1
                        endlessPoints+=1
            pm.printMatrix(dp)
    return endlessPoints

#matrix = [[0,1,0], [1,1,1], [0,1,1]]
matrix = [[0,1,1], [1,1,0], [0,1,0]]
print(findNumberEndlessPoints(matrix))
