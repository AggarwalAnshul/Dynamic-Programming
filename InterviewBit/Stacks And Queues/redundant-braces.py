"""
Redundant Braces
Asked in:
Amazon
Given a string A denoting an expression. It contains the following operators ’+’, ‘-‘, ‘*’, ‘/’.

Chech whether A has redundant braces or not.

Return 1 if A has redundant braces, else return 0.

Note: A will be always a valid expression.



Input Format

The only argument given is string A.
Output Format

Return 1 if string has redundant braces, else return 0.
For Example

Input 1:
    A = "((a + b))"
Output 1:
    1
    Explanation 1:
        ((a + b)) has redundant braces so answer will be 1.

Input 2:
    A = "(a + (a + b))"
Output 2:
    0
    Explanation 2:
        (a + (a + b)) doesn't have have any redundant braces so answer will be 0.


[+]Temporal marker           : Tue, 20:18 | Mar 17, 20
[+]Temporal marker untethered: Tue, 20:41 | Mar 17, 20
[+]Comments                  : Devised solution is accepted and on par, though not the most elegant
                                > devised the editorial solution on my own after some more thought
                                > optimized the originally devised solution too
                                > matter is closed now
[+]Space Complexity          : O(N)
[+]Time Complexity           : O(N)
[+]Level                     : EASY
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/redundant-braces
[+] Supplement Sources       : N/A
"""


def findSolution(string):
    stack = []
    for char in string:
        if not char == ")":
            stack.append(char)
        else:
            expression_length = 0
            while stack[-1] != "(":
                expression_length += 1
                stack.pop()
            stack.pop() # remove the corresponding (
            if expression_length <= 1:
                return 1
            stack.append('tempAnswer') # answer of the expression
    return 0

def editorial(A):
    stack = []
    for i in range(len(A)):
        char = A[i]
        if A[i] in '(+-/*':
            stack.append(A[i])
        elif A[i] == ')':
            if stack.pop() == '(':
                return 1
            stack.pop()
    return 0

if __name__ == "__main__":
    test_cases = [
        "(a+(a+b+c+d))",
        "((a+b))",
        "(())",
        "()",
        "(a+b+c+(d))"
    ]
    for test_case in test_cases:
        print("input >> " + str(test_case) + " output: >> " + str(editorial(test_case)))
