#M.

"""
 
[+]Temporal marker            :  Mon, 10:55 | Sep 23, 19
[+]Temporal marker untethered :  Mon, 11:37 | Sep 23, 19
[+]Comments                   : *Granted not very elegant solution
                                *In parallel with the GFG DP Solution
                                *Can't think of a much more efficient solution
                                *Problem is now closed until further light
[+]Level                      : Medium
[+]Tread speed                : Relaxed
[+]LINK                       : https://www.geeksforgeeks.org/number-of-paths-with-exactly-k-coins

"""
#S|T Complexity: O(rows*cols*coins)
def findSolution(matrix, coins):
    rows = len(matrix)
    cols = len(matrix[0])

    #init
    dp = [[[] for x in range(cols)] for y in range(rows)]
    dp[0][0] = [matrix[0][0]]
    for j in range(1, cols):
        if(dp[0][j-1][0] + matrix[0][j] < coins):
            dp[0][j] = [dp[0][j-1][0] + matrix[0][j]]
    for i in range(1, rows):
        if(dp[i-1][0][0] + matrix[i][0] < coins):
            dp[i][0] = [dp[i-1][0][0] + matrix[i][0]]

    for i in range(1, rows):
        for j in range(1, cols):
            up = dp[i-1][j]
            left = dp[i][j-1]
            lis = [up, left]
            for k in lis:
                for el in k:
                    if(i==rows-1 and j==cols-1):
                        if(el + matrix[i][j] == coins):
                            dp[i][j].append(el + matrix[i][j])
                    else:
                        if(el + matrix[i][j] < coins):
                            dp[i][j].append(el + matrix[i][j])
    return len(dp[rows-1][cols-1])

if __name__ == "__main__":
    matrix = [[1,2,3], [4, 6, 5], [3, 2, 1]]
    print(findSolution(matrix, 12))