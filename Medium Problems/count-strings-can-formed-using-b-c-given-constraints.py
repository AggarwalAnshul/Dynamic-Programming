#M.

"""
 Given a length n, count the number of strings of length n that can be made using ‘a’, ‘b’ and ‘c’
  with at-most one ‘b’ and two ‘c’s allowed.

Examples :

Input : n = 3
Output : 19
Below strings follow given constraints:
aaa aab aac aba abc aca acb acc baa
bac bca bcc caa cab cac cba cbc cca ccb

Input  : n = 4
Output : 39
Asked in Google Interview



[+]Temporal marker            :  Sun, 14:21 | Jan 05, 20
[+]Temporal marker untethered :  Sun, 14:26(R*) | Jan 05, 20
[+]Comments                   : *Solution devised in Record time
                                *DP Solution devised in acceptable time ~ Good
                                *Had some trouble on DP solution in python, as was incorrectly conceiving
                                *3D array. The code worked flawlessly in JAVA.
                                *Python code working fine after a brake.
                                *Singed Off: 16:10
[+]Level                      : 
[+]Tread speed                : 
[+]LINK                       : https://www.geeksforgeeks.org/count-strings-can-formed-using-b-c-given-constraints
"""

def findSolution(length, count_b, count_c, dp):
    if(length==0):
        return 1
    if(dp[length][count_b][count_c]==-1):
        a = findSolution(length-1, count_b, count_c, dp)
        b = findSolution(length-1, count_b-1, count_c, dp) if count_b>0 else 0
        c = findSolution(length-1, count_b, count_c-1, dp) if count_c>0 else 0
        dp[length][count_b][count_c] = a + b + c
    return dp[length][count_b][count_c]

def findSolutionRecursive(length, count_b, count_c):
    if(length==0):
        return 1
    a = findSolutionRecursive(length - 1, count_b, count_c)
    b = findSolutionRecursive(length - 1, count_b - 1, count_c) if count_b > 0 else 0
    c = findSolutionRecursive(length - 1, count_b, count_c - 1) if count_c > 0 else 0
    return a+b+c

if __name__ == "__main__":
    #lis = [length, count_b, count_c]
    lis = [4, 1, 2]
    lis = [3, 1, 2]

    dp = [[[-1 for i in range(lis[2]+1)] for j in range(lis[1]+1)] for slice in range(lis[0]+1)]
    print(findSolution(lis[0], lis[1], lis[2], dp))
    print(findSolutionRecursive(lis[0], lis[1], lis[2]))