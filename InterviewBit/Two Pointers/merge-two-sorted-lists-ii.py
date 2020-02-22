"""
Given two sorted integer arrays A and B, merge B into A as one sorted array.

 Note: You have to modify the array A to contain the merge of A and B. Do not output anything in your code.
TIP: C users, please malloc the result into a new array and return the result.
If the number of elements initialized in A and B are m and n respectively, the resulting size of array A after your code is executed should be m + n

Example :

Input :
         A : [1 5 8]
         B : [6 9]

Modified A : [1 5 6 8 9]


[+]Temporal marker           : Sat, 13:24 | Feb 22, 20
[+]Temporal marker untethered: Sat, 13:24 | Feb 22, 20
[+]Comments                  :
[+]Space Complexity          : O()
[+]Time Complexity           : O()
[+]Level                     :
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/merge-two-sorted-lists-ii
[+] Supplement Sources       : N/A
"""


def merge(one, two):
    pointer_one = 0
    pointer_two = 0
    length_one = len(one)
    length_two = len(two)
    lis = []
    for x in range(length_one + length_two):
        if pointer_one < length_one and pointer_two < length_two:
            if one[pointer_one] <= two[pointer_two]:
                lis.append(one[pointer_one])
                pointer_one += 1
            else:
                lis.append(two[pointer_two])
                pointer_two += 1
        elif pointer_one < length_one:
            lis.append(one[pointer_one])
            pointer_one += 1
        else:
            lis.append(two[pointer_two])
            pointer_two += 1
    for x in lis:
        print(x, end=" ")
    return lis


if __name__ == "__main__":
    data = [[[1, 5, 8], [6, 9]], [[-4, 3], [-2, -2]]]
    for x in data:
        print("input: " + str(x) + " >> " + str(merge(x[0], x[1])))
