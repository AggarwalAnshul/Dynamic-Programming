"""
Write a function that takes an unsigned integer and returns the number of 1 bits it has.

Example:

The 32-bit integer 11 has binary representation

00000000000000000000000000001011
so the function should return 3.

Note that since Java does not have unsigned int, use long for Java


[+]Temporal marker           : Fri, 12:34 | Feb 21, 20
[+]Temporal marker untethered: Fri, 12:34 | Feb 21, 20
[+]Comments                  : EASY
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(1)
[+]Level                     : EASY
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/number-of-1-bits
[+] Supplement Sources       : N/A
"""


def optimizedSolution(number):
    count = 0
    while number != 0:
        number &= number - 1
        count += 1
    return count


def findSolution(number):
    count = 0
    for i in range(33):
        if number & 1 << i:
            count += 1
    return count


if __name__ == "__main__":
    data = [32]
    for x in data:
        print("input: " + str(x) + " >> " + str(findSolution(x)))
