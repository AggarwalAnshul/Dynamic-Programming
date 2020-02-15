"""

[+]Temporal marker           : Sat, 12:7 | Feb 15, 20
[+]Temporal marker untethered: Sat, 12:20 | Feb 15, 20
[+]Comments                  : EASY
[+]Space Complexity          : O(N*N)
[+]Time Complexity           : O(N*N)
[+]Level                     :EASY
[+]Tread Speed               :PACED
[+]LINK                      : https://www.interviewbit.com/problems/implement-strstr
[+] Supplement Sources       : N/A
"""


def findSolution(string, sub):
    lenSub = len(sub)
    lenString = len(string)
    if lenSub == 0 or lenString == 0:
        return -1

    dp = [[0 for x in range(lenString + 1)] for y in range(lenSub + 1)]

    for i in range(1, lenSub + 1):
        for j in range(1, lenString + 1):
            # print("i: "+str(i)+" J: "+str(j))
            if sub[i - 1] == string[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
    ans = -1
    for i in range(1, lenString + 1):
        # print("i: "+str(i))
        if dp[lenSub][i] == lenSub:
            ans = i
            # print("ans: "+str(ans))
            break

    print("string: " + string)
    print("sub: " + sub)
    if ans == -1:
        return ans
    return ans - lenSub


if __name__ == '__main__':
    data = ["abaa", "aabaababa"]
    data = ["abaa", "d"]
    data = ["b", "baba"]
    print("index at: " + str(findSolution(data[0], data[1])))
