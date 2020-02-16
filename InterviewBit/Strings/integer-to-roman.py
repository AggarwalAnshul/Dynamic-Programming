"""

Please Note:
Another question which belongs to the category of questions which are intentionally stated vaguely.
Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.

Given an integer A, convert it to a roman numeral, and return a string corresponding to its roman numeral version

 Note : This question has a lot of scope of clarification from the interviewer. Please take a moment to think of all the needed clarifications and see the expected response using “See Expected Output” For the purpose of this question, https://projecteuler.net/about=roman_numerals has very detailed explanations.


Input Format

The only argument given is integer A.
Output Format

Return a string denoting roman numeral version of A.
Constraints

1 <= A <= 3999
For Example

Input 1:
    A = 5
Output 1:
    "V"

Input 2:
    A = 14
Output 2:
    "XIV"

[+]Temporal marker           : Sun, 15:15 | Feb 16, 20
[+]Temporal marker untethered: Sun, 19:50 | Feb 16, 20
[+]Comments                  : Was an intermediate solution
                              *Took almost 2.5 hours to come up with the fully accepted solution
                              *My Solution was too length and lacked elegance
                              *Editorial solution is too efficient & Elegant solution
                              *Was able to comprehend the editorial solution
                              *Implemented the solution on my own & it worked like a CHARM!
                              *MATTER IS OFFICIALLY CLOSED NOW!.
[+]Space Complexity          : O()
[+]Time Complexity           : O()
[+]Level                     : MEDIUM
[+]Tread Speed               : relaxed
[+]LINK                      : https://www.interviewbit.com/problems/integer-to-roman
[+] Supplement Sources       : https://www.mathsisfun.com/roman-numerals.html
"""


# THE EDITORIAL SOLUTION
def smallest_solution_to_numeral_to_roman(number):
    key = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    value = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_number = ""

    i = 0
    while number > 0:
        for x in range(number // key[i]):
            roman_number += value[i]
            number -= key[i]
        i += 1
    return roman_number


# MY SOLUTION USING THE EDITORIAL APPROACH
def numeral_to_roman(number):
    key = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    value = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_number = ""
    while number > 0:
        for i in range(len(key)):
            if number // key[i] > 0:
                break
        contender = key[i]
        division = number // contender
        mod = number % contender
        while division > 0:
            division -= 1
            roman_number += value[i]
        number = number % contender
    return roman_number


# MY ORIGINAL SOLUTION / SUCCESSFUL SUBMISSION
#
# def append(string, time):
#     ans = ""
#     for i in range(time):
#         ans += string
#     return ans
#
# def offset(contender):
#     if contender <= 10:
#         return 0
#     if contender <= 100:
#         return 10
#     if contender <= 1000:
#         return 100
#     return 1000
#
# def numeral_to_roman(num):
#     numberToRoman = {
#         1: "I",
#         2: "II",
#         3: "III",
#         4: "IV",
#         5: "V",
#         6: "VI",
#         7: "VII",
#         8: "VIII",
#         9: "IX",
#         10: "X",
#         50: "L",
#         100: "C",
#         500: "D",
#         1000: "M"}
#
#     lis = [1, 5, 10, 50, 100, 500, 1000]
#     if num in numberToRoman:
#         return numberToRoman[num]
#     for i in range(len(lis)):
#         if num < lis[i]:
#             break
#     contender = lis[i - 1]
#     next_contender = lis[i]
#     remainder = num % contender
#     major = num - remainder
#
#     if num > 1000:
#         return append(numeral_to_roman(1000), num // 1000) + numeral_to_roman(num % 1000)
#
#     if next_contender - offset(next_contender) <= num <= next_contender:
#         remainder = num + offset(next_contender) -next_contender
#         if remainder == 0:
#             return numeral_to_roman(offset(next_contender)) + numeral_to_roman(next_contender)
#         else:
#             return numeral_to_roman(offset(next_contender)) + numeral_to_roman(next_contender) + numeral_to_roman(remainder)
#     else:
#         if remainder == 0:
#             return append(numeral_to_roman(contender), num // contender)
#         else:
#             return numeral_to_roman(major) + numeral_to_roman(remainder)
# Editorial Solution

if __name__ == "__main__":
    data = [449, 19, 25, 34, 39, 40, 200, 11, 85, 89, 789, 1500]
    for value in data:
        print("value: " + str(value) + " >> " + str(numeral_to_roman(value)))
        print("value: " + str(value) + " >> " + str(smallest_solution_to_numeral_to_roman(value)))
