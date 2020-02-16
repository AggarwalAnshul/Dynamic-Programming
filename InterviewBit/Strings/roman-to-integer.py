"""
Given a string A representing a roman numeral.
Convert A into integer.

A is guaranteed to be within the range from 1 to 3999.

NOTE: Read more
details about roman numerals at Roman Numeric System



Input Format

The only argument given is string A.
Output Format

Return an integer which is the integer verison of roman numeral string.
For Example

Input 1:
    A = "XIV"
Output 1:
    14

Input 2:
    A = "XX"
Output 2:
    20


[+]Temporal marker           : Sun, 14:44 | Feb 16, 20
[+]Temporal marker untethered: Sun, 15:08 | Feb 16, 20
[+]Comments                  :EASY, Took the time to only learn how to read the characters
                                Code accepted in one iteration.
                                Matter is closed now.
[+]Space Complexity          : O(N)
[+]Time Complexity           : O(1)
[+]Level                     :EASY
[+]Tread Speed               :Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/roman-to-integer
[+] Supplement Sources       : 1)"Whenever a letter with lesser value precedes a letter of higher value, it means its value has to be added as negative of that letter’s value."
                               2)https://www.wikihow.com/Read-Roman-Numerals
"""


def findSolution(string):
    dict = {"I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000, }
    ans = 0
    length = len(string)
    for i in range(0, length):
        # print("For: "+str(string[i]))
        char = string[i]
        if i < length - 1 and dict[char] < dict[string[i + 1]]:
            # print('subtracting...'+str(dict[char]))
            ans -= dict[char]
        else:
            ans += dict[char]
            # print('adding...'+str(dict[char]))
        # print("\t>> "+str(ans))
    return ans


if __name__ == "__main__":
    data = ["MMCDMI", "XXXIX", "CCXLVI", "DCCLXXXIX", "MMCDXXI", "CLX", "CCVII", "MIX",
            "MLXVI", "MDCCLXXVI", "MMXX","IVL","XXXXII","XXCV","DCCXIC","IIIC","MCD"]
    for value in data:
        print("input: " + value + " >> " + str(findSolution(value)))
