#M.

"""
73
Count all triplets whose sum is equal to a perfect cube
Given an array of n integers, count all different triplets whose sum is equal to the perfect cube i.e, for any i, j, k(i < j < k) satisfying the condition that a[i] + a[j] + a[j] = X3 where X is any integer. 3 ≤ n ≤ 1000, 1 ≤ a[i, j, k] ≤ 5000
Example:

Input:
N = 5
2 5 1 20 6
Output:
3
Explanation:
There are only 3 triplets whose total sum is a perfect cube.
Indices  Values SUM
0 1 2    2 5 1   8
0 1 3    2 5 20  27
2 3 4    1 20 6  27
Since 8 and 27 are prefect cube of 2 and 3.


[+]Temporal marker            :  Wed, 10:30 | Sep 25, 19
[+]Temporal marker untethered :  Wed, 11:40 | Sep 25, 19
[+]Comments                   : *Naive solution is working
                                *Laying off DP Solution for the time being
                                *
[+]Level                      :
[+]Tread speed                :
[+]LINK                       : https://www.geeksforgeeks.org/count-triplets-whose-sum-equal-perfect-cube
"""
import math
def is_perfect_cube(num):

    cube_root = 2**(1/3*(math.log(num, 2)))
    if( round(cube_root, 0)**3 == num):
        return True
    return False

#S-Complexity: O(N*N*2) | T-Complexity: O(N*N*N)
def findSolution(lis):
    length = len(lis)
    dp = [[[0]*length for x in range(length)]for y in range(2)]

    #1D matrix computation
    for i in range(length):
        dp[0][i][i] = lis[i]
        for j in range(i+1, length):
            dp[0][i][j] = lis[i]+lis[j]
    print(dp[0])

    count = 0
    for i in range(length):
        print("Checking for: "+str(lis[i]))
        for j in range(i+1, length):
            print("\tChecking for: "+str(lis[j]))
            for k in range(j+1, length):
                print("\t\tChecking for: "+str(lis[k]))
                if( is_perfect_cube(dp[0][i][j]+lis[k])==True):
                    count+=1
                    #print(str(lis[i])+" "+str(lis[j])+" "+str(lis[k]))
    return count
if __name__ == "__main__":
    lis = [2, 5, 1, 20, 6]
    print(findSolution(lis))
