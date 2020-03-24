"""
Letter Phone
Asked in:
Facebook
Epic systems
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



The digit 0 maps to 0 itself.
The digit 1 maps to 1 itself.

Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Make sure the returned strings are lexicographically sorted.


[+]Temporal marker           : 18:57 Hours | Tuesday 24, 2020
[+]Temporal marker untethered: 19:51 Hours | Tuesday 24, 2020
[+]Comments                  : >> The solution was easy per-se
                                >> the desecription was shitty!
                                >> it was literally though i was adding fix for all the corner cases
                                >> finally "12" gave me real idea, what was the expected output!
                                >> really pathetic description

[+]Space Complexity          : O(3^n)
[+]Time Complexity           : O(3^n)
[+]Level                     : EASY
[+]Tread Speed               : Paced
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A
"""

# Original, Accepted Solution
# @param number: number to be converted
# @return the list of char combination for number given
def letterCombinations_obsolete(number):

    def return_characters(num):
        if num == "0":
            return ["0"]
        elif num == "1":
            return ["1"]
        elif num == "7":
            return ['p', 'q', 'r', 's']
        elif num == "8":
            return ['t', 'u', 'v']
        elif num == "9":
            return ['w', 'x', 'y', 'z']
        num = int(num) - 1
        char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        return char[(num - 1) * 3: (num - 1) * 3 + 3]

    first = return_characters(number[0])
    number = number[1:]
    while number:
        temp = []
        second = return_characters(number[0])
        number = number[1:]
        for x in first:
            for y in second:
                temp.append(x+y)
        first = temp
    return sorted(first)

#EDITORIAL INSPIRED
# @param number: number to be converted
# @return the list of char combination for number given
def letterCombinations(number):
    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 6: 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '1': '1',
        '0': '0'
    }
    first = mapping[number[0]]
    number = number[1:]
    while number:
        second, number = mapping[number[0]], number[1:]
        first = [x+y for x in first for y in second]
    return first

if __name__ == '__main__':

    print(letterCombinations("23"))