"""

[+]Temporal marker           : Wed, 21:29 | Feb 12, 20
[+]Temporal marker untethered: Wed, 21:29 | Feb 12, 20
[+]Comments                  :
[+]Level                     :
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/stringoholics

"""


def calculateTime(string):
    length = len(string)
    count = 1
    rev = string[1:] + string[0]
    temp = string
    while rev != string:
        count += 1
        step = count % length
        #print('step: ' + str(step))
        rev = rev[step:] + rev[:step]
        #print(string + "--->" + rev)
    return count


def findHCF(a, b):
    if a == 0:
        return b
    return findHCF(b % a, a)


def findLCM(a, b):
    ans = a * b
    return int(ans / findHCF(a, b))


def findSolution(lis):
    fallback = 1
    ans = 1
    for x in lis:
        t = calculateTime(x)
        ans = findLCM(fallback%(10**9+7), t%(10**9+7))
        fallback = ans
    return ans%(10**9+7)


if __name__ == '__main__':
    lis = ["a", "ababa", "aba"]
    print(findSolution(lis))
    print(calculateTime("ababa"))
    print(findHCF(8, 4))