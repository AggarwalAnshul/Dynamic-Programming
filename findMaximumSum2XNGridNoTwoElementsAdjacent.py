"""
Maximum sum in a 2 x n grid such that no two elements are adjacent
Given a rectangular grid of dimension 2 x n. We need to find out the maximum sum such that no two chosen numbers are adjacent, vertically, diagonally or horizontally.
Examples:

Input : 1 4 5
        2 0 0
Output : 7
If we start from 1 then we can add only 5 or 0. 
So max_sum = 6 in this case.
If we select 2 then also we can add only 5 or 0.
So max_sum = 7 in this case.
If we select from 4 or 0  then there is no further 
elements can be added.
So, Max sum is 7.

Input : 1 2 3 4 5
        6 7 8 9 10
Output : 24

[+]Temporal Marker:              18:41:14 Hours | Aug21, Wednesday
[+]Temporal marker untethered:   18:58:30 Hours | Aug21, Wednesday
[+]Tread Speed:                  Relaxed, could have done it way faster
[+]LINK: https://www.geeksforgeeks.org/maximum-sum-2-x-n-grid-no-two-elements-adjacent/
"""

#for print matrix utility
import PrintMatrix
"""def printMatrix(matrix):
    for row in matrix:
        print()
        for col in row:
            print(col, end=" ")
"""

"""--------------------------------------------------------------"""
def findMaximumSum2XNGridNoTwoElementsAdjacent(matrix):
    #no of columns
    cols = len(matrix[0])
    #Since there are only rows(2*n matrix)
    rows = 2

    #Auxillary matrix for saving solutions
    dp = [[0]*(cols) for x in range(2)]

    #Initializing the dp, Since to comeup with a value greater than element itself
    #there must be atleast 3 columns, hence the last 2 columns need not to be
    #computed. We start from the third last and move column by column
    #till we reach the column 
    for i in range(0, 2):
        for j in range(cols-2, cols):
            dp[i][j] = matrix[i][j]

    #Populating the matrix
    #Here for every column we only need to check the column second next to it,
    #since the adjacent column could not be used, hence the second next.
    #Also since we are storing the solutions, the second next column would contain
    #The maximum value that can be found after this, hence no need to do that again
    for j in range(cols-3, -1, -1):
        dp[0][j] = matrix[0][j] + max(dp[0][j+2], dp[1][j+2])
        dp[1][j] = matrix[1][j] + max(dp[0][j+2], dp[1][j+2])

    #PrintMatrix.printMatrix(dp)
    return max(dp[0][0], dp[1][0])
"""--------------------------------------------------------------"""


lis = [ [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]  ]
#lis = [   [1, 4, 5], [2, 0, 0] ]
print(findMaximumSum2XNGridNoTwoElementsAdjacent(lis))
    
