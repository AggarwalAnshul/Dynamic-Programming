"""

[+]Temporal marker           : Mon, 15:4 | Feb 10, 20
[+]Temporal marker untethered: Mon, 15:30 | Feb 10, 20
[+]Comments                  :easy
[+]Level                     :easy
[+]Tread Speed               :fast
[+]LINK                      : https://www.interviewbit.com/problems/count-and-say

"""


def generate(string):
    print('requesting for '+string)
    length = len(string)
    element = string[0]
    pointer = 1
    count = 1
    new = ""
    while pointer < length:
        if string[pointer] != element:
            print('appending...' + str(count) + " for " + str(element))
            new += "" + str(count) + str(element)
            count = 1
            element = string[pointer]
            pointer += 1
        else:
            count += 1
            pointer += 1
    new += "" + str(count) + str(element)
    return new


def findSolution(n):
    ans = ["1"]
    for x in range(1, n):
        ans.append(generate(ans[x - 1]))
        print(ans)
    return ans

print(generate("21"))
#rint(findSolution(4))
