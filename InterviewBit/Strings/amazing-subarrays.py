"""
Amazing Subarrays
You are given a string S, and you have to find all the amazing substrings of S.

Amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).

Input

Only argument given is string S.
Output

Return a single integer X mod 10003, here X is number of Amazing Substrings in given string.
Constraints

1 <= length(S) <= 1e6
S can have special characters
Example

Input
    ABEC

Output
    6

Explanation
	Amazing substrings of given string are :
	1. A
	2. AB
	3. ABE
	4. ABEC
	5. E
	6. EC
	here number of substrings are 6 and 6 % 10003 = 6.

[+]Temporal marker           : Tue, 9:11 | Feb 11, 20
[+]Temporal marker untethered: Tue, 9:51 | Feb 11, 20
[+]Comments                  :EASY
[+]Level                     :EASY
[+]Tread Speed               :Paced | intermittent
[+]LINK                      : https://www.interviewbit.com/problems/amazing-subarrays

"""
import re

#Accepted Solution
def solve(self, string):
    import re
    length = len(string)
    ans = 0
    last = 0
    for i in range(length - 1, -1, -1):
        last = last + 1
        if re.match("^[a|e|i|o|u]$", string[i].lower()):
            # print('its a match')
            ans += last
    return ans % 10003

# # THE SOLUTION IS TLE ONE
# def findSolution(string):
#     import re
#     def solve(self, string):
#         import re
#         length = len(string)
#         dp = [[0 for x in range(length + 1)] for x in range(length + 1)]
#
#         ans = 0
#         last = 0
#         for i in range(length - 1, -1, -1):
#             for j in range(length - 1, i - 1, -1):
#                 if j == i:
#                     last = last + 1
#                     if re.match("^[a|e|i|o|u]$", string[j].lower()):
#                         # print('its a match')
#                         ans += last
#         return ans % 10003
#
#
# # THIS SOLUTION IS CORRECT BUT EXCEEDS THE MEMORY LIMIT
# def findSolution(string):
#     length = len(string)
#     dp = [[0 for x in range(length + 1)] for x in range(length + 1)]
#
#     ans = 0
#
#     for i in range(length - 1, -1, -1):
#         for j in range(length - 1, i - 1, -1):
#             if j > i and i + 1 < length:
#                 dp[i][j] = dp[i + 1][j]
#             if j == i:
#                 dp[i][j] += dp[i][j + 1] + 1
#                 if re.match("^[a|e|i|o|u]$", string[j].lower()):
#                     # print('its a match')
#                     ans += dp[i][j]
#     return ans


print(findSolution("ABED"))
print(findSolution("ABCD"))
print(findSolution("AB'SD"))
