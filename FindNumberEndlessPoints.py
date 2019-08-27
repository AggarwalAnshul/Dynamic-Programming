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

Temporal marker            : Didn't Tether, ~90mins
Temporal marker untethered : N/A
Tread speed                : Relaxed
Comments                   : had to put in time, took break of 12 hours, but managed to solve
                             GFG is also to be blame, incorrect problem constraint desc
                             It was not mentioned that the element would also has to be 1
                             in order to qualify for endless path points beside having endless
                             path row and endless path column, Already put in a request to
                             approve my correction, Pushing to git now in 3,2,1..!
LINK                       : https://www.geeksforgeeks.org/find-number-endless-points/
"""
import PrintMatrix as pm

def findNumberofEndlessPoints(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    countMax = 0
    dp = [[0]*(cols+1) for x in range(rows+1)]

    #init
    for x in range(cols+1):
        dp[rows][x] = 2
    for x in range(rows+1):
        dp[x][cols] = 1

    #population
    for i in reversed(range(rows)):
        for j in reversed(range(cols)):
            #checking for rows
            if(dp[i][j+1]==1 or dp[i][j+1]==3):
                if(matrix[i][j]==1):
                    dp[i][j] = 1 #marks the row path as clear for endless path
            #checking for column
            if(dp[i+1][j]==2 or dp[i+1][j]==3):
                if(matrix[i][j] == 1):
                    if(dp[i][j]==1): #when both row and col are clear for endless path
                        dp[i][j] = 3
                    else:
                        dp[i][j] = 2 #marks the col path as clear for endless path
            if(dp[i][j] == 3):  #counts the toatl number of endless points
                countMax+=1
            #pm.printMatrix(dp) #DEBUG: Prints the matrix
    return countMax


#matrix = [[0,1,0], [1,1,1], [0,1,1]]
matrix = [[0,1,1], [1,1,0], [0,1,0]]
matrix =  [[1, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1],[0, 1, 1, 0]] 
print(findNumberofEndlessPoints(matrix))
