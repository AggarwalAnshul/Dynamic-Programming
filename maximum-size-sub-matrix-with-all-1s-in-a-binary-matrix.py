"""
#102
Maximum size square sub-matrix with all 1s
Given a binary matrix, find out the maximum size square sub-matrix with all 1s.

For example, consider the below binary matrix.
maximum-size-square-sub-matrix-with-all-1s

[+]Temporal marker            : 16:35 Hours | Thursday, Sept05, 19
[+]Temporal marker untethered : 16:45 Hours | Thursday, Sept05, 19
[+]Comments                   : Couldn't solve in the first attempt,
                                *Laid it off
                                *Retried in the sweep
                                *Suprisingly the approach struck me withing 5 minutes of perusal
                                *coldpress in another 5 minutes
                                *Next thing I knew was algo derived within 10 minutes
                                *Approach identical to GFG
                                *Damn! I'm growing man :D
[+]Tread speed                : Relaxed 
[+]Level                      : Medium
[+]LINK                       : https://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/
"""

import PrintMatrix as pm
def findSolution(matrix):
    rowIndex = len(matrix)-1
    colIndex = len(matrix[0])-1
    maxCount = 0
    for i in range(rowIndex-1, -1, -1):
        for j in range(colIndex-1, -1, -1):
            if(matrix[i][j]>0):
                right = matrix[i][j+1]
                bottom = matrix[i+1][j]
                bottomRight = matrix[i+1][j+1]
                if(right>0 and bottom>0 and bottomRight>0):
                    if(right == bottom and bottom == bottomRight):
                        matrix[i][j] = right+1
                    else:
                        matrix[i][j] = max(right, bottomRight, bottom)
                maxCount = max(maxCount, matrix[i][j])
    #pm.printMatrix(matrix)
    return maxCount
i
f __name__ == "__main__":
    matrix =[[0, 1, 1, 0, 1], 
    [1, 1, 0, 1, 0], 
    [0, 1, 1, 1, 0], 
    [1, 1, 1, 1, 0], 
    [1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0]]

    print(findSolution(matrix))
