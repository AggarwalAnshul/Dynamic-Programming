"""

[+]Temporal marker           : Wed, 19:49 | Feb 26, 20
[+]Temporal marker untethered: Wed, 19:49 | Feb 26, 20
[+]Comments                  :
[+]Space Complexity          : O()
[+]Time Complexity           : O()
[+]Level                     :
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/array-3-pointers
[+] Supplement Sources       : N/A
"""

def findSolution(lis):
    one = lis[0]
    two = lis[1]
    three = lis[2]
    pointerOne = len(one)-1
    pointerTwo = len(two)-1
    pointerThree = len(three)-1
    ans = lis[0][-1]

    while True:
        if one[pointerOne] > two[pointerTwo]:
            if pointerOne > 0:
                pointerOne -=1
            else:
                break
        else:
            if pointerTwo > 0:
                pointerTwo -=1
            else:
                break
        ans = min(ans, max(abs(one[pointerOne] - two[pointerTwo]),
                        abs(two[pointerTwo]-three[pointerThree]),
                        abs(one[pointerOne] - three[pointerThree])))

        if two[pointerTwo] > three[pointerThree]:
            if pointerTwo > 0:
                pointerTwo -=1
            else:
                break
        else:
            if pointerThree > 0:
                pointerThree -=1
            else:
                break

        ans = min(ans, max(abs(one[pointerOne] - two[pointerTwo]),
                        abs(two[pointerTwo]-three[pointerThree]),
                        abs(one[pointerOne] - three[pointerThree])))

        if one[pointerOne] > three[pointerThree]:
            if pointerOne > 0:
                pointerOne -= 1
            else:
                break
        else:
            if pointerThree > 0:
                pointerThree -= 1
            else:
                break
        ans = min(ans, max(abs(one[pointerOne] - two[pointerTwo]),
                        abs(two[pointerTwo]-three[pointerThree]),
                        abs(one[pointerOne] - three[pointerThree])))
    return min(ans, max(abs(one[pointerOne] - two[pointerTwo]),
                        abs(two[pointerTwo]-three[pointerThree]),
                        abs(one[pointerOne] - three[pointerThree])))



if __name__ == "__main__":
    data = [
        [[1, 4, 10], [2, 15, 20], [10, 12]]
]
    for x in data:
        print("input: " + str(x) + " >> " + str(findSolution(x)))