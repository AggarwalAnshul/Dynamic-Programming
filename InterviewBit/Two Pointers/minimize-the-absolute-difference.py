"""
Minimize the absolute difference
Asked in:
Microsoft
Problem Setter: ganeshk2 Problem Tester: dhruvi
Given three sorted arrays A, B and Cof not necessarily same sizes.

Calculate the minimum absolute difference between the maximum and minimum number
 from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively.
i.e. minimize | max(a,b,c) - min(a,b,c) |.

Example :

Input:

A : [ 1, 4, 5, 8, 10 ]
B : [ 6, 9, 15 ]
C : [ 2, 3, 6, 6 ]
Output:

1
Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.


[+]Temporal marker           : Sat, 14:16 | Feb 22, 20
[+]Temporal marker untethered: Sat, 19:28 | Feb 22, 20
[+]Comments                  : Great Problem
                               Couldn't solve on my own
                              Saw solution approach from iB
                              It now makes sense
                              implementation accepted in first attempt
                              I hope i remember this approach
                              Matter is closed now
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     : MEDIUM
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/minimize-the-absolute-difference
[+] Supplement Sources       : N/A
"""


def findSolution(lis):
    one, two, three = lis[0], lis[1], lis[2]
    pointer = [len(one) - 1, len(two) - 1, len(three) - 1]
    triplet = [one[pointer[0]], two[pointer[1]], three[pointer[2]]]
    ans = max(triplet) - min(triplet)
    maxIndex = 0
    while True:
        for index in range(3):
            if triplet[index] > triplet[maxIndex]:
                maxIndex = index
        if pointer[maxIndex] > 0:
            pointer[maxIndex] -= 1
            triplet[maxIndex] = lis[maxIndex][pointer[maxIndex]]
            ans = min(ans, max(triplet) - min(triplet))
        else:
            break
    return ans


if __name__ == "__main__":
    data = [
        [[1, 4, 5, 8, 10], [6, 9, 15], [2, 3, 6, 6]]

    ]
    for x in data:
        print("input: " + str(x) + " >> " + str(findSolution(x)))
