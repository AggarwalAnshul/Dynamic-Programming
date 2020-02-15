"""
Given a string S, find the longest palindromic substring in S.

Substring of string S:

S[i...j] where 0 <= i <= j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.

Incase of conflict, return the substring which occurs first ( with the least starting index ).

Example :

Input : "aaaabaaa"
Output : "aaabaaa"

[+]Temporal marker           : Wed, 23:21 | Feb 12, 20
[+]Temporal marker untethered: Sat, 10:45 | Feb 15, 20
[+]Comments                  :Finally this question is sloved.
                                *Had encountered it previously on GFG, but had writted a partially correct answer
                                *This time the solution is 100% correct
                                *Man it took me some real time to come up to solution
                                *Read teh solution approach form iB but couldn't comprehend
                                *Finally saw a YT Video and it's one liner struck the approach in me.
                                *coded the solution at the very instant and the solution was fully correct
                                *Matter is closed now
                                *Might embark to reduce the space complexity to O(1)
                                *Devised the O(1) Space complexity solution
                                *Had help from GFG looked the approach and code
                                *Wrote the code and got submitted in the first attempt
                                *This approach worked like a CHARM!
[+]Space Complexity          :O(N*N) | O(N*N)
[+]Time Complexity           :O(1)  | O(N*N)
[+]Level                     :MEDIUM
[+]Tread Speed               :RELAXED
[+]LINK                      : https://www.interviewbit.com/problems/longest-palindromic-substring
[+]Supporting Sources         : https://youtu.be/UflHuQj6MVA

"""
import math


# Trying an O(1) Space complexity Approach
# Solution is up and rollin!
def findSolution(string):
    length = len(string)
    maxLength = 1
    palindromestart = 0

    for i in range(0, length):
        pivot = i

        # finding for odd length palindromes
        left = pivot - 1
        right = pivot + 1
        while left >= 0 and right < length and string[left] == string[right]:
            if maxLength < right - left + 1:
                maxLength = right - left + 1
                palindromeStart = left
            left -= 1
            right += 1

        # Looking for even length palindromes
        left = i - 1
        right = i
        while left >= 0 and right < length and string[left] == string[right]:
            if maxLength < right - left + 1:
                maxLength = right - left + 1
                palindromeStart = left
            left -= 1
            right += 1
    print(maxLength)
    return string[palindromeStart : palindromeStart + maxLength]


# Improving Solution with O(N) Space requirements
# T-complexity: O(N*N)
# S-complexity: O(N)
# def findSolution(string):
#     length = len(string)
#     dp = [0 for x in range(length)]
#     dp[length - 1] = 1
#     ans, maxi, maxj = 0, 0, 0
#
#     print(dp)
#     for i in range(length - 2, -1, -1):
#         for j in range(length - 1, i - 1, -1):
#             if i == j:
#                 dp[j] = 1
#             else:
#                 if string[i] == string[j]:
#                     if dp[j - 1] != -1:
#                         dp[j] = dp[j - 1] + 2
#                         if ans <= dp[j]:
#                             maxi, maxj = i, j
#                             ans = dp[j]
#                     else:
#                         dp[j] = -1
#                 else:
#                     dp[j] = -1
#         print(dp)
#     print('ans: ' + str(ans))
#     return string[maxi: maxj + 1]


# -----------Working Solution O(N*N) | O(N*N)
# def findSolution(string):
#     length = len(string)
#     # dp = [[0 for x in range(length)] for y in range(length)]
#     dp = [-1 for x in range(length)]
#     ans = 0
#     maxi, maxj = 0, 0
#     dp[length-1][length-1] = 1
#     for i in range(length - 2, -1, -1):
#         for j in range(length - 1, i-1, - 1):
#             #print('i: '+str(i)+"j: "+str(j)+" "+string[i]+" : "+string[j])
#             if i == j:
#                 dp[i][j] = 1
#             else:
#                 if string[i] == string[j]:
#                     #print('its a match i:'+string[i]+" : "+string[j])
#                     if dp[i + 1][j - 1] != -1:
#                         dp[i][j] = dp[i + 1][j - 1] + 2
#                         if ans <= dp[i][j]:
#                             ans = dp[i][j]
#                             maxi = i
#                             maxj = j
#                     else:
#                         dp[i][j] = -1
#                 else:
#                     dp[i][j] = -1
#
#     for slice in dp:
#         print()
#         for x in slice:
#             print(x, end=" ")
#     print(string[maxi: maxj+1])
#     return ans


if __name__ == '__main__':
    string = "abacdfgacabd"
    string = "caccbcbaabacabaccacaaccaccaaccbbcbcbbaacabccbcccbbacbbacbccaccaacaccbbcc"
    string = "abacdfgacabd"
    string = "abacdgfdcaba"
    string = "abbcccbbbcaaccbababcbcabca"
    string = 'forgeeksskeegfor'
    string = "sibb"
    string = "abacdgfdcaba"
    string = "aaaabaaa"
    print(findSolution(string))
