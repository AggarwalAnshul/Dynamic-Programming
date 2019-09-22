"""
#M.54
Find all distinct subset (or subsequence) sums of an array
Given a set of integers, find distinct sum that can be generated from the subsets of the given sets and print them in an increasing order. It is given that sum of array elements is small.

Examples:

Input  : arr[] = {1, 2, 3}
Output : 0 1 2 3 4 5 6
Distinct subsets of given set are
{}, {1}, {2}, {3}, {1,2}, {2,3}, 
{1,3} and {1,2,3}.  Sums of these
subsets are 0, 1, 2, 3, 3, 5, 4, 6
After removing duplicates, we get
0, 1, 2, 3, 4, 5, 6  

Input : arr[] = {2, 3, 4, 5, 6}
Output : 0 2 3 4 5 6 7 8 9 10 11 12 
         13 14 15 16 17 18 20

Input : arr[] = {20, 30, 50}
Output : 0 20 30 50 70 80 100
 
[+]Temporal marker            : 09:05, | Saturday Sept21, 19
[+]Temporal marker untethered : 24:48(R*)  | Saturday Sept21, 19
[+]Comments                   : O(N^3) Solution in record 13 mins
                                Looking for something more optimized
                                XXXProblem is now closedXX
[+]Level                      : Medium
[+]Tread speead               : Paced
[+]LINK                       : https://www.geeksforgeeks.org/find-distinct-subset-subsequence-sums-array/
"""
#S-Complexity: O(Sum(N)) | T-Complexity: O(N*sum(N))
def findSolution(lis):
    length = len(lis)
    ans = [0]
    #O(N) To Calculate the sum
    rows = sum(lis)
    col = []
    for x in range(1, rows+1):
        col.append(x)
    dp = [[0]*(length+1) for x in range(rows+1)]
    dp[0] = [1]*(length+1)

    #O(N*N) to populate the matrix
    for i in range(1, rows+1):
        for j in range(1, length+1):
            dp[i][j] += dp[i][j-1]
            if(i>=lis[j-1]):
                if(dp[i-lis[j-1]][j-1]>0):
                    dp[i][j] = 1
        if(dp[i][j]==1):
            ans.append(i)
    import PrintMatrix as pm
    #pm.printss(dp, lis, col)
    return ans

if __name__ == "__main__":
    lis = [1, 2, 3]
    lis = [2, 3, 4, 5, 6]
    lis = [20, 30, 50]
    print(findSolution(lis))

    
