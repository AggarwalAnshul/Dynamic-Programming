"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Given s = "Hello World",

return 5 as length("World") = 5.

Please make sure you try to solve this problem without using library functions. Make sure you only traverse the string once.

[+]Temporal marker           : Sun, 12:58 | Feb 16, 20
[+]Temporal marker untethered: Sun, 13:12 | Feb 16, 20
[+]Comments                  :EASY
                              Devised the more efficient solution after getting inspiration
                              from iB. Though, their editorial solution was incorrect.
                              Instead of progressing search from the beginning i started from the
                              end thus saving the traverse time. Although time complexity remains
                              the same more & less. Still it's good to cater this approach.
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     :EASY
[+]Tread Speed               :PACED
[+]LINK                      : https://www.interviewbit.com/problems/length-of-last-word
[+] Supplement Sources       : N/A
"""


# MOST EFFICIENT & EFFECTIVE SOLUTION
def findSolution(string):
    length_of_last_word = 0
    length = len(string)
    x = length - 1
    while x >= 0 and not string[x].isalpha():
        x -= 1

    while x >= 0 and string[x].isalpha():
        x -= 1
        length_of_last_word += 1
    return length_of_last_word


# FULL ACCEPTED SOLUTION
# def findSolution(string):
#     length = len(string)
#     ans = 0
#     for x in range(0, length):
#         # print("x "+ string[x])
#         char = "" + string[x]
#         if char.isalpha():
#             if x > 0:
#                 if not ("" + string[x - 1]).isalpha():  # previous is non alpha
#                     ans = 1
#                 else:  # previous is alphabet
#                     ans += 1
#             else:
#                 ans = 1
#     return ans


if __name__ == '__main__':
    string = "Hello World"
    string = "     "
    string = "ab bcejkdfj *&^$&*$&"
    string = "Hello World  "
    string = "     "
    string = "Hello World   "
    string = "ab bcejkdfj *&^$&*$&   "
    print(lengthOfLastWord(string))
    print(findSolution(string))
