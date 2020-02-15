"""

[+]Temporal marker           : Sat, 11:41 | Feb 15, 20
[+]Temporal marker untethered: Sat, 11:49  + (10 Minutes of approach hunting)| Feb 15, 20
[+]Comments                  : Devised the approach in 10 mintues
                             *The solution was contingent on a legal LongestPalindromeSubstring solution
                             *Used the same solution and tweaked it to suit this problem
                             *EASY PEASY LEMON SQUEEZY!
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N*N)
[+]Level                     : Medium
[+]Tread Speed               : Paced
[+]LINK                      : https://www.interviewbit.com/problems/minimum-characters-required-to-make-a-string-palindromic
[+] Supplement Sources       : N/A
"""


def findSolution(string):
    length = len(string)
    palindromeStart = 0
    maxLength = 1

    for i in range(0, length):
        pivot = i
        # looking for odd palindromes
        left = i - 1
        right = i + 1
        while left >= 0 and right < length and string[left] == string[right]:
            if maxLength < right - left + 1 and left == 0:
                palindromeStart = left
                maxLength = right - left + 1
            left -= 1
            right += 1
        # looking for even length palindrome substrings
        left = pivot - 1
        right = pivot
        while left >= 0 and right < length and string[left] == string[right]:
            if maxLength < right - left + 1 and left == 0:
                maxLength = right - left + 1
                palindromeStart = left
            left -= 1
            right += 1
    print("string: " + string)
    print("palindrome: " + string[palindromeStart:palindromeStart + maxLength])
    print("string length: " + str(length))
    if palindromeStart != 0:
        return length - 1
    return length - maxLength


if __name__ == '__main__':
    string = "abc"
    string = "AACECAAAA"
    string = "mmtatbdzqsoemuvnpppsu"
    print("Answer >> " + str(findSolution(string)))
