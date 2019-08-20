"""
Path with maximum average value
Given a square matrix of size N*N, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells which starts from the top left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.
Examples:

Input : Matrix = [1, 2, 3
                  4, 5, 6
                  7, 8, 9]
Output : 5.8
Path with maximum average is, 1 -> 4 -> 7 -> 8 -> 9
Sum of the path is 29 and average is 29/5 = 5.8

LINK: https://www.geeksforgeeks.org/path-maximum-average-value/

Temporal marker: 13:43 Hours | Aug19, Monday
Temporal marker untetherd: 15:06 Hours | Aug19, Monday
Took time in printing the sequence
logic devising was on track

"""

def printMatrix(dp):
    for x in dp:
        for y in x:
            print(str(y)+" ", end=" ")
        print()
        
def findMaximumAverageValue(matrix):

    #Creating a 2D DP Matrix
    length = len(matrix)
    dp = [[0 for i in range(length)] for y in range(length)]
    
    #Populating the dp matrix
    for i in range(length-1, -1, -1):
        for j in range(length-1, -1, -1):
            branchRight = 0
            branchBottom = 0
            if(j+1<=length-1):
                branchRight = dp[i][j+1]
            if(i+1<=length-1):
                branchBottom = dp[i+1][j]
            dp[i][j] = matrix[i][j] + max(branchRight, branchBottom)

    return(dp[0][0]/((2*length)-1))

    
matrix= [[1, 2, 3], [4, 5, 6], [7, 8, 9] ]
print(findMaximumAverageValue(matrix))
