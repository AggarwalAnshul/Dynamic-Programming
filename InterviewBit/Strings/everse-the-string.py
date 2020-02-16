"""
Given a string A.

Return the string A after reversing the string word by word.

NOTE:

A sequence of non-space characters constitutes a word.

Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.

If there are multiple spaces between words, reduce them to a single space in the reversed string.



Input Format

The only argument given is string A.
Output Format

Return the string A after reversing the string word by word.
For Example

Input 1:
    A = "the sky is blue"
Output 1:
    "blue is sky the"

Input 2:
    A = "this is ib"
Output 2:
    "ib is this"


[+]Temporal marker           : Sun, 13:28 | Feb 16, 20
[+]Temporal marker untethered: Sun, 13:39 | Feb 16, 20
[+]Comments                  : EASY
[+]Space Complexity          : O(N)
[+]Time Complexity           : O(N)
[+]Level                     : EASY
[+]Tread Speed               : PACED
[+]LINK                      : https://www.interviewbit.com/problems/everse-the-string
[+] Supplement Sources       : N/A
"""


def editorial_solution(data):
    return " ".join(data.strip().split()[::-1])

def findSolution(data):
    data = data.strip()  # this handles trailing & leading whitespaces
    length = len(data)
    ans = ""
    word = ""
    for x in range(length + 1):
        if x == length or data[x] == " ":
            if len(ans) == 0:
                ans = word
            else:
                ans = word + " " + ans
            word = ""
        else:
            word += data[x]
    return ans


if __name__ == "__main__":
    data = " the sky is pink "
    data = "   "
    data = "   the word is big &*&*( "
    print(findSolution(data))
    print(editorial_solution(data))
