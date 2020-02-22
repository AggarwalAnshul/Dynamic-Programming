"""
Divide two integers without using multiplication, division and mod operator.
Return the floor of the result of the division.
Example:

5 / 2 = 2
Also, consider if there can be overflow cases. For overflow case, return INT_MAX.
Note: INT_MAX = 2^31 - 1


[+]Temporal marker           : Fri, 13:24 | Feb 21, 20
[+]Temporal marker untethered: Fri, 13:24 | Feb 21, 20
[+]Comments                  :Couldn't solve on my own
                              Solution straight from GFG
[+]Space Complexity          : log(dividend)
[+]Time Complexity           : O(N)
[+]Level                     : MEDIUM
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/divide-integers
[+] Supplement Sources       : https://www.geeksforgeeks.org/divide-two-integers-without-using-multiplication-division-mod-operator/
"""


def divide(dividend, divisor):
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    if divisor == 0 or (divisor == 1 and dividend >= INT_MAX):
        return INT_MAX
    if dividend <= INT_MIN and divisor == -1:
        return INT_MAX

    temp = 0
    mask = 0
    sign = -1
    if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
        sign = 1
    dividend = abs(dividend)
    divisor = abs(divisor)
    for bit in range(31, -1, -1):
        if (temp + (divisor << bit)) <= dividend:
            temp += divisor << bit
            mask ^= 1 << bit
    return sign * mask


if __name__ == "__main__":
    data = [[21, 4], [100, 3], [2147483647, 1], [-1, 1]]
    for x in data:
        print("input: " + str(x) + " >> " + str(divide(x[0], x[1])))
