"""
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example :

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 5]

Output : [3 5]
 NOTE : For the purpose of this problem ( as also conveyed by the sample case ), assume
 that elements that appear more than once in both arrays should be included multiple times
  in the final output.

[+]Temporal marker           : Sat, 13:55 | Feb 22, 20
[+]Temporal marker untethered: Sat, 14:00 | Feb 22, 20
[+]Comments                  : EASY
[+]Space Complexity          : O(N)
[+]Time Complexity           : O(N)
[+]Level                     : EASY
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/intersection-of-sorted-arrays
[+] Supplement Sources       : N/A
"""


def findSolution(one, two):
    pointer_one, pointer_two = 0, 0
    length_one = len(one)
    length_two = len(two)
    lis = []

    while pointer_two < length_two and pointer_one < length_one:
        # print("PointerOne: "+str(pointer_one)+" PointerTwo: "+str(pointer_two))
        if one[pointer_one] < two[pointer_two]:
            # print("one < two")
            pointer_one += 1
        elif one[pointer_one] > two[pointer_two]:
            # print("one > two")
            pointer_two += 1
        else:
            # print('added to the lis')
            lis.append(one[pointer_one])
            pointer_two += 1
            pointer_one += 1
    return lis


if __name__ == "__main__":
    data = [[[1, 2, 3, 3, 4, 5, 6], [3, 3, 5]],
            [[1,2,3,4,45],[8,443]]]
    for x in data:
        print("input: " + str(x) + " >> " + str(findSolution(x[0], x[1])))
