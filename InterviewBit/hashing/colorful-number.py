'''
Programming Hashing Colorful Number
Colorful Number
Asked in:
Epic systems
For Given Number N find if its COLORFUL number or not

Return 0/1

COLORFUL number:

A number can be broken into different contiguous sub-subsequence parts.
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
Example:

N = 23
2 3 23
2 -> 2
3 -> 3
23 -> 6
this number is a COLORFUL number since product of every digit of a sub-sequence are different.

Output : 1


[+]Temporal marker           : 10:23 Hours | Tuesday 31, 2020
[+]Temporal marker untethered: 10:44 Hours | Tuesday 31, 2020
[+]Comments                  : EASY
[+]Space Complexity          : O(N*N)
[+]Time Complexity           : O(N*N)
[+]Level                     : EASY
[+]Tread Speed               : Intermittent
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A

'''

#ACCEPTED
def colorful(number):
    length = len(number)
    dict = {}
    for pairLength in range(1, length+1):
        for index in range(length):
            product = 1
            if index+pairLength > length:
                continue
            for subsequence in range(index, min(length, index+pairLength)):
                product *= int(number[subsequence])
            if product in dict:
                return 0
            dict[product] = 0
    return 1
if __name__ == '__main__':
    print(colorful("111"))