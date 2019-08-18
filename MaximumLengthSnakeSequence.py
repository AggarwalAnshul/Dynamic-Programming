"""
Find maximum length Snake sequence
Given a grid of numbers, find maximum length Snake sequence and print it. If multiple snake sequences exists with the maximum length, print any one of them.

A snake sequence is made up of adjacent numbers in the grid such that for each number, the number on the right or the number below it is +1 or -1 its value. For example, if you are at location (x, y) in the grid, you can either move right i.e. (x, y+1) if that number is ± 1 or move down i.e. (x+1, y) if that number is ± 1.

For example,

9, 6, 5, 2
8, 7, 6, 5
7, 3, 1, 6
1, 1, 1, 7

In above grid, the longest snake sequence is: (9, 8, 7, 6, 5, 6, 7)

Below figure shows all possible paths –

LINK: https://www.geeksforgeeks.org/find-maximum-length-snake-sequence/
Temporal maker: 17:04 Hours | Aug18, Sunday
Temporal Marker Untethered: 17:34 Hours | Aug18, Sunday
"""

#A utility function that prints a matrix
#Paramter: a 2D Matrix
#Returns: None
def printMatrix(matrix):
    for x in matrix:
        for y in x:
            print(str(y)+" ", end=" ")
        print()


#A utility function that finds maximum length Snake sequence and print it
#Paramter: a 2D Matrix
#Returns: Maximum Lengthed Snake Sequence
def findMaximumLengthSnakeSequence(array):
    rows = len(array)
    cols = len(array[0])
    snakeLength = 0

    dp = [[1]*(cols) for x in range(rows)]
    #printMatrix(dp)
                    
    for i in range(rows-1, -1, -1):
        for j in range(cols-1, -1, -1):
            #print("i: "+str(i)+" j: "+str(j))
            branchRight = 0
            branchBottom = 0
            if(j<cols-1 and abs(array[i][j+1]-array[i][j])==1):
                branchRight = dp[i][j+1]+1
            if(i<rows-1 and abs(array[i][j]-array[i+1][j])==1):
                branchBottom = dp[i+1][j]+1
            dp[i][j] = max(dp[i][j], branchRight, branchBottom)
            snakeLength = max(snakeLength, dp[i][j])
            #printMatrix(dp)

    #Returns the answer
    return snakeLength
       

grid =[[9, 6, 5, 2],[
8, 7, 6, 5],[
7, 3, 1, 6],[
1, 1, 1, 7]]
        
print(findMaximumLengthSnakeSequence(grid))
