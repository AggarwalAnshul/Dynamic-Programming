"""
#M.53

Largest sum Zigzag sequence in a matrix
Given a matrix of size n x n, find sum of the Zigzag sequence with the largest sum. A zigzag sequence starts from the top and ends at the bottom. Two consecutive elements of sequence cannot belong to same column.
Examples:

Input : mat[][] = 3  1  2
                  4  8  5
                  6  9  7
Output : 18
Zigzag sequence is: 3->8->7
Another such sequence is 2->4->7

Input : mat[][] =  4  2  1
                   3  9  6
                  11  3 15
Output : 28
 
[+]Temporal marker            : 21:35, | Saturday Sept21, 19
[+]Temporal marker untethered : 24:48(R*)  | Saturday Sept21, 19
[+]Comments                   : O(N^3) Solution in record 13 mins
                                Looking for something more optimized
                                XXXProblem is now closedXX
[+]Level                      : Medium
[+]Tread speead               : Paced
[+]LINK                       : https://www.geeksforgeeks.org/largest-sum-zig-zag-sequence-in-a-matrix/
"""

#S-Complexity: O(N) | T-Complexity: O(N*N)
def findSolution(matrix):
    length = len(matrix)

    for i in range(1, length):
        for j in range(length):
            maxUntilNow = 0
            for k in range(length):
                if(j!=k):
                    maxUntilNow = max(maxUntilNow, matrix[i-1][k])
            matrix[i][j] += maxUntilNow
        #print(matrix)
    return max(matrix[length-1])

if __name__ == "__main__":
    matrix =[[3, 1, 2],[4, 8, 5],[6, 9, 7]]
    matrix = [[4, 2, 1], [3, 9, 6], [11, 3, 15]]
    print(findSolution(matrix))

    
