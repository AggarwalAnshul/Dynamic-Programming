"""
Reverse the bits of an 32 bit unsigned integer A.

Input Format:

    First and only argument of input contains an integer A
Output Format:

    return a single unsigned integer denoting minimum xor value
Constraints:

0 <= A < 2^32
For Examples :

Example Input 1:
    A = 0
Example Output 1:
    0
Explanation 1:
        00000000000000000000000000000000
=>      00000000000000000000000000000000
Example Input 2:
    A = 3
Example Output 2:
    3221225472
Explanation 2:
          00000000000000000000000000000011
=>        11000000000000000000000000000000
Since java does not have unsigned int, use long

Seen this questi


[+]Temporal marker           : Fri, 13:02 | Feb 21, 20
[+]Temporal marker untethered: Fri, 13:15 | Feb 21, 20
[+]Comments                  : EASY
[+]Space Complexity          : O(N)
[+]Time Complexity           : O(1)
[+]Level                     : EASY
[+]Tread Speed               : Intermittent
[+]LINK                      : https://www.interviewbit.com/problems/reverse-bits
[+] Supplement Sources       : N/A
"""


def findSolution(num):
    ans = 0
    for i in range(0, 16):
        left = i
        right = 31 - i
        if num & (1 << left):
            ans |= (1 << right)
        if num & (1 << right):
            ans |= (1 << left)
    return ans


if __name__ == "__main__":
    data = [3]
    for x in data:
        print("input: " + str(x) + " >> " + str(findSolution(x)))
