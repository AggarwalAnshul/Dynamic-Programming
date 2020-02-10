"""
Given the array of strings A,
you need to find the longest string S which is the prefix of ALL the strings in the array.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1
and S2.

For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".



Input Format

The only argument given is an array of strings A.
Output Format

Return longest common prefix of all strings in A.
For Example

Input 1:
    A = ["abcdefgh", "aefghijk", "abcefgh"]
Output 1:
    "a"
    Explanation 1:
        Longest common prefix of all the strings is "a".

Input 2:
    A = ["abab", "ab", "abcd"];
Output 2:
    "ab"
    Explanation 2:
        Longest common prefix of all the strings is "ab".

[+]Temporal marker           : Mon, 14:41 | Feb 10, 20
[+]Temporal marker untethered: Mon, 14:47 | Feb 10, 20
[+]Comments                  :DAMN!!! IDK How it was this easy
                             *It's a G-Problem
                             *Knew the approach, just coded and Boom!
[+]Level                     :EASY
[+]Tread Speed               :Fast
[+]LINK                      : https://www.interviewbit.com/problems/longest-common-prefix

"""


def longestCommonPrefix(lis):
    one = lis[0]
    for x in range(len(one)):
        char = one[x]
        for i in range(1, len(lis)):
            if x >= len(lis[i]) or lis[i][x] != char:
                return one[:x]
    return one


if __name__ == '__main__':
    lis = ["abcdefgh", "aefghijk", "abcefgh"]
    lis = ["abab", "ab", "abcd"]
    print(longestCommonPrefix(lis))
