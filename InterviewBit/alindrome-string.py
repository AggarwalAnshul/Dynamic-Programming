"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:

"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

[+]Temporal marker           : Mon, 13:05 | Feb 10, 20
[+]Temporal marker untethered: Mon, 13:55 | Feb 10, 20
[+]Comments                  :Took some time to learn regex in python
                                The solution exceeded time limit
                                Devised a O(N) solution
                                Solution is accepted
                                Matter is closed now
[+]Level                     :EASY
[+]Tread Speed               :PACED
[+]LINK                      : https://www.interviewbit.com/problems/alindrome-string

"""
import re


def isPalindrome(A):
    length = len(A)
    if length == 1:
        return 1
    left = 0
    right = length - 1
    while left <= right:
        while left < length and not A[left].isalnum():
            left += 1
        while right >= 0 and not A[right].isalnum():
            right -= 1
        if left < length and length > right >= left:
            if A[left].casefold() != A[right].casefold():
                return 0
        left += 1
        right -= 1
    return 1


string = "A man, a plan, a canal: Panama"
string = ".,"
print(isPalindrome(string))
