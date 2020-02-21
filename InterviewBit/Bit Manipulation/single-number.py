"""

[+]Temporal marker           : Fri, 18:56 | Feb 21, 20
[+]Temporal marker untethered: Fri, 18:30 | Feb 21, 20
[+]Comments                  : Couldn't found the optimized solution on my own.
                                Though still devised a O(N) SOlution.
                                Matter is closed now.
[+]Space Complexity          : O()
[+]Time Complexity           : O()
[+]Level                     : MEDIUM
[+]Tread Speed               : Intermittent
[+]LINK                      : https://www.interviewbit.com/problems/single-number
[+] Supplement Sources       : N/A
"""


def editorial(lis):
    from functools import reduce
    return reduce(lambda a, b: a ^ b, lis)


def optimizedSolution(lis):
    answer = 0
    for element in lis:
        answer ^= element
    return answer


# TLE
def findSolution(lis):
    mask = 0
    temp = 0
    for element in lis:
        if mask & 1 << element:
            temp -= element
        else:
            temp += element
        mask ^= 1 << element
    return temp


if __name__ == "__main__":
    data = [[1, 2, 2, 3, 1]]
    for x in data:
        print("input: " + str(x) + " >> " + str(findSolution(x)) +
              " optimized: " + str(optimizedSolution(x)) +
              "editorial: "+ str(editorial(x)))
