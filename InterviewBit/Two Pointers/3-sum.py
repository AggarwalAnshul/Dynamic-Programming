"""

[+]Temporal marker           : Sat, 18:23 | Feb 22, 20
[+]Temporal marker untethered: Sat, 18:23 | Feb 22, 20
[+]Comments                  :
[+]Space Complexity          : O()
[+]Time Complexity           : O()
[+]Level                     :
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/3-sum
[+] Supplement Sources       : N/A
"""


def findSolution(lis, target):
    length = len(lis)
    chosen = []
    sum = 0
    print("target: "+str(target))
    for turn in range(0, 3):
        closest = abs(target - lis[0])
        temp = 0
        for i in range(length):
            if i not in chosen:
                if closest > abs(target - lis[i]):
                    temp = i
                    closest = abs(target - lis[i])
        chosen.append(temp)
        print('chosen is: '+str(lis[temp]))
        target -= lis[temp]
        sum += lis[temp]
    return sum


if __name__ == "__main__":
    data = [[[-1, 4, 2, 1], 5],
            [[-5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6, 0, -9, 5, 3, -9,
              -5, -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3], -1],
            [[-5, 1, 4, -7, 10],1]]
    for x in data:
        print("input: " + str(x) + " >> " + str(findSolution(x[0], x[1])))
