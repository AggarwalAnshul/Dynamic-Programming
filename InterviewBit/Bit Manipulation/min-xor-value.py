"""
Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.

Input Format:

    First and only argument of input contains an integer array A
Output Format:

    return a single integer denoting minimum xor value
Constraints:

2 <= N <= 100 000
0 <= A[i] <= 1 000 000 000
For Examples :

Example Input 1:
    A = [0, 2, 5, 7]
Example Output 1:
    2
Explanation:
    0 xor 2 = 2
Example Input 2:
    A = [0, 4, 7, 9]
Example Output 2:
    3


[+]Temporal marker           : Fri, 12:11 | Feb 21, 20
[+]Temporal marker untethered: Fri, 12:24 | Feb 21, 20
[+]Comments                  :EASY
[+]Space Complexity          : O(N)
[+]Time Complexity           : O(NlogN)
[+]Level                     :
[+]Tread Speed               : Intermittent
[+]LINK                      : https://www.interviewbit.com/problems/min-xor-value
[+] Supplement Sources       : N/A
"""


def findSolution(A):
    import sys
    ans = sys.maxsize
    length = len(A)
    A.sort()
    for i in range(length):
        for j in range(i + 1, length):
            ans = min(ans, A[i] ^ A[j])
    return ans


def optimizedSolution(lis):
    import sys
    ans = sys.maxsize
    length = len(lis)
    for i in range(1, length):
        ans = min(ans, lis[i] ^ lis[i - 1])
    return ans


if __name__ == "__main__":
    data = [[0, 2, 5, 7]]
    for x in data:
        print("input: " + str(x) + " >> " + str(findSolution(x)))
        print("input: " + str(x) + " >> " + str(optimizedSolutin(x)))
