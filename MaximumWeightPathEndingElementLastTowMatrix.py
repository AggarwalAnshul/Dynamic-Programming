"""
Maximum weight path ending at any element of last row in a matrix
Given a matrix of integers where every element represents weight of the cell.
Find the path having the maximum weight in matrix [N X N]. Path Traversal Rules are:

It should begin from top left element.
The path can end at any element of last row.
We can move to following two cells from a cell (i, j).
Down Move : (i+1, j)
Diagonal Move : (i+1, j+1)
Examples:

Input : N = 5
        mat[5][5] = {{ 4, 2 ,3 ,4 ,1 },
                     { 2 , 9 ,1 ,10 ,5 },
                     {15, 1 ,3 , 0 ,20 },
                     {16 ,92, 41, 44 ,1},
                     {8, 142, 6, 4, 8} };
Output : 255
Path with max weight : 4 + 2 +15 + 92 + 142 = 255      

Temporal Maker: Nah lost track of the time!
                Recursive apporach was produced withing usual time frames
                Dynamic appraoch took some time, tbh watched 2 suits episodes, ate lunch,
                bathed. I Guess, it was acceptable timefram? Kinda!
LINK: https://www.geeksforgeeks.org/maximum-weight-path-ending-element-last-row-matrix/
"""

def findMaximumWeightPathEndingElementLastTowMatrixRecursive(matrix, i, j, sumCount):
    if(i==len(matrix)-1 or j>=len(matrix[0])):
        return sumCount
    return max( findMaximumWeightPathEndingElementLastTowMatrixRecursive(matrix, i+1, j+1, sumCount+matrix[i+1][j+1]),
                findMaximumWeightPathEndingElementLastTowMatrixRecursive(matrix, i+1, j, sumCount+matrix[i+1][j]))
                
def findMaximumWeightPathEndingElementLastTowMatrix(matrix, i, j, string):
    string+="\t"
    #print(string+" function for i: "+str(i)+" j: "+str(j))
    if(i==len(matrix)-1 or j>=len(matrix[0])):
        return matrix[i][j]

    if(dp[i][j]==0):
        branchDown = findMaximumWeightPathEndingElementLastTowMatrix(matrix,i+1,j, string)
        branchDiagonal = findMaximumWeightPathEndingElementLastTowMatrix(matrix,i+1, j+1, string)
        dp[i][j] = matrix[i][j] + max(branchDown, branchDiagonal)
        #print(string+"dp[i][j] is: "+str(dp[i][j]))
    #print(string+" returning: "+str(dp[i][j]))
    return dp[i][j]

"""
matrix = [ [ 4, 2 ,  3,  4 , 1 ],
           [ 2, 9 ,  1,  10, 5 ],
           [15, 1 ,  3,  0 ,  20],
           [16, 92,  41, 44, 1],
           [8 , 142, 6,  4,  8]
           ]"""
matrix = [ [4, 1 ,5 ,6 , 1], 
		[2 ,9 ,2 ,11 ,10], 
		[15,1 ,3 ,15, 2], 
		[16, 92, 41,4,3], 
		[8, 142, 6, 4, 8]] 
rows = len(matrix)
cols = len(matrix[0])
dp = [[0]*cols for x in range(rows)]
print(findMaximumWeightPathEndingElementLastTowMatrix(matrix,0,0,""))
print(findMaximumWeightPathEndingElementLastTowMatrixRecursive(matrix, 0, 0, 0)+matrix[0][0])
