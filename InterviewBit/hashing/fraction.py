"""
Programming Hashing Fraction
Fraction
Asked in:  
Amazon
Microsoft
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example :

Given numerator = 1, denominator = 2, return "0.5"
Given numerator = 2, denominator = 1, return "2"
Given numerator = 2, denominator = 3, return "0.(6)"

"""
"""
[+]Temporal marker            :2001 Hours | Tuesday 07, 2020
[+]Temporal marker Untethered :1410 Hours | Tuesday 08, 2020
[+]Comments                   : The implementation per se was pretty easy
                                The tough task was to crack the mathematical logic
                                Couldn't solve on my own, 
                                Breakthrough was iB Solution Approach that gave the mathematical logic
                                Almost flashed the implementation
                                solution is closed now
[+]Space Complexity           : O()
[+]Time Complexity            : O()
[+]Level                      : MEDIUM
[+]Tread Speed                : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/fraction.py
[+] Supplement Sources       : N/A

"""

# ACCEPTED
# Solution at par with the editorial solution
def fractionToDecimal(numerator, denominator):
    # handle the negative input
    flag = "-" if numerator * denominator < 0 else ""
    numerator = numerator * -1 if numerator < 0 else numerator
    denominator = denominator * -1 if denominator < 0 else denominator

    #find the integer part
    integer = numerator // denominator
    remainder = numerator % denominator

    #incept the hashmap
    seen, quotient, index = {}, "", 0
    seen[remainder] = 0

    #driver meat
    while remainder != 0:
        temp_quotient, remainder = divmod(remainder * 10, denominator)
        quotient += str(temp_quotient)
        if remainder in seen:
            start = seen[remainder]
            return flag + str(integer) + "." + quotient[:start] + "(" + str(quotient[start:]) + ")"
        index += 1
        seen[remainder] = index

    quotient = '.'+quotient if quotient else quotient
    return flag + str(integer) + quotient


if __name__ == "__main__":
    test_cases = [
        [7, 12],
        [22, 7],
        [1, 2],
        [2, 1],
        [2, 3],
        [0, -1],
    ]
    for index in range(len(test_cases)):
        test_case = test_cases[index]
        print("input: "+str(test_case)+"\n\tOUTPUT: :" +
              str(fractionToDecimal(test_case[0], test_case[1])))
