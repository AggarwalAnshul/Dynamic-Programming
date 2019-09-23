# M.65

"""
Collect maximum coins before hitting a dead end
Given a character matrix where every cell has one of the following values.

'C' -->  This cell has coin

'#' -->  This cell is a blocking cell.
         We can not go anywhere from this.

'E' -->  This cell is empty. We don't get
         a coin, but we can move from here.
Initial position is cell (0, 0) and initial direction is right.

Following are rules for movements across cells.

If face is Right, then we can move to below cells

Move one step ahead, i.e., cell (i, j+1) and direction remains right.
Move one step down and face left, i.e., cell (i+1, j) and direction becomes left.
If face is Left, then we can move to below cells

Move one step ahead, i.e., cell (i, j-1) and direction remains left.
Move one step down and face right, i.e., cell (i+1, j) and direction becomes right.
Final position can be anywhere and final direction can also be anything. The target is to collect maximum coins.

Example:
example

[+]Temporal marker            :  Mon, 12:18                  | Sep 23, 19
[+]Temporal marker untethered :  Mon, 12:29(R*) | 13:34(DP*) | Sep 23, 19
[+]Observation                : *No matter how you traverse the matrix,
                                *Even rows will have right direction of traversal
                                    *Start counting from the left end(0 column)
                                *Odd Rows has left direction of traversal
                                    *Start counting from the right end(length-1 column)

[+]Comments                   : * Recursive solution in acceptable timeFrames(11Mins)
                                * Dp solution took some time
                                * Observation was caught after a considerable time
                                * The observation is correct and yields the correct result
                                * GFG doesn't have a pure DP Tabulization solution
[+]Level                      : Medium
[+]Tread speed                : Relaxed
[+]LINK                       : https://www.geeksforgeeks.org/collect-maximum-coins-before-hitting-a-dead-end
"""
def printMatrix(dp):
    for row in dp:
        for col in row:
            print(col, end="\t")
        print()

#Returns the direction of traversal for this row
def getDirection(row):
    if(row==0 or row%2==0):
        return "right"
    return "left"

#Add this cells value to the current computed value,
def include_this_cell_value(value, i, j, matrix):
    if (matrix[i - 1][j - 1] == "C"): #Cell contains coin
        return value+1
    elif (matrix[i - 1][j - 1] == "#"): #Cell contain obstacle
        return 0
    return value #Cell is empty

def findSolution(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    """ --- STRUCTURE OF DP ---
      rows+1
      cols+2
      X X X X X X X X
      X a b c d e f X
      X a b c d e f X
      X a b c d e f X

      """
    
    ans = 0
    dp = [[0]*(cols+2) for x in range(rows+1)]
    for i in range(1, rows+1):
        direction = getDirection(i-1)
        if(direction == "right"):
            for j in range(1, cols+1):
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                dp[i][j] = include_this_cell_value(dp[i][j], i, j, matrix)
                ans = max(ans, dp[i][j])
        else:
            for j in range(cols, -1, -1):
                dp[i][j] = max(dp[i][j+1], dp[i-1][j])
                dp[i][j] = include_this_cell_value(dp[i][j], i, j, matrix)
                ans = max(ans, dp[i][j])
    printMatrix(dp)
    return ans

def findSolutionRecursive(i, j, coins, dir, matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    print("i: "+str(i)+" j: "+str(j))
    if(not(i>=0 and i<rows and j>=0 and j<cols)):
        print("returning...")
        return coins
    if (matrix[i][j] == "#"):
        return coins
    if (matrix[i][j] == "C"):
        coins += 1
    if (dir == "left"):
        return max(findSolutionRecursive(i, j - 1, coins, dir, matrix),
                   findSolutionRecursive(i + 1, j, coins, "right", matrix))
    else:
        return max(findSolutionRecursive(i, j + 1, coins, dir, matrix),
                   findSolutionRecursive(i + 1, j, coins, "left", matrix))


if __name__ == "__main__":
    matrix = [['E', 'C', 'C', 'C', 'C'],
              ['C', '#', 'C', '#', 'E'],
              ['#', 'C', 'C', '#', 'C'],
              ['C', 'E', 'E', 'C', 'E'],
              ['C', 'E', '#', 'C', 'E']]

    matrix = [['C', 'C', 'C', 'C', 'C'],
              ['C', '#', 'C', '#', 'E'],
              ['#', 'C', 'C', '#', 'C'],
              ['C', 'E', 'E', 'C', 'E'],
              ['C', 'E', 'C', 'C', 'E']]

    print(findSolution(matrix))
    #print(findSolutionRecursive(0, 0, 0, "right", matrix))
