"""
Given two binary strings, return their sum (also a binary string).

Example:

a = "100"

b = "11"
Return a + b = “111”.

[+]Temporal marker           : Mon, 13:12 | Feb 17, 20
[+]Temporal marker untethered: Mon, 13:25 | Feb 17, 20
[+]Comments                  : EASY
[+]Space Complexity          : O(N)
[+]Time Complexity           : O(N)
[+]Level                     : EASY
[+]Tread Speed               : PACED
[+]LINK                      : https://www.interviewbit.com/problems/add-binary-strings
[+] Supplement Sources       : N/A
"""


def findSolution(one, two):
    if len(one) < len(two):
        return findSolution(two, one)

    # Equate the length of the string
    length_one = len(one)
    length_two = len(two)
    offset = length_one - length_two
    while offset > 0:
        two = "0" + two
        offset -= 1

    flag = 0
    ans = ""
    # add the numbers
    for i in range(length_one - 1, -1, -1):
        charOne = int(one[i])
        charTwo = int(two[i])
        add = charOne + charTwo + flag
        flag = 0
        if add < 2:
            ans = str(add) + ans
        else:
            flag = 1
            if add == 2:
                ans = "0" + ans
            else:
                ans = "1" + ans
    if flag == 1:
        return "1" + ans
    return ans


if __name__ == "__main__":
    data = [["1111", "1"]]
    for x in data:
        print("data: " + str(x) + " >> " + str(print(findSolution(x[0], x[1]))))
